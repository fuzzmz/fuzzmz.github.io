title: Debugging fun
date: 2014-02-07
slug: debugging-fun
category: debug
tags: arm, linux

There are days when the universe seems to conspire against you. Playing with an ARM-embedded Linux system I consistently managed to make it hang, which meant that I had to get my hard-hat and pickaxe and go deeper.

After reproducing it a couple of times, I see it's not just a hang, but a complete CPU deadlock. To boot, the misbehaving CPU core literally falls off the JTAG bus rendering debugging impossible. Running SMP Linux both cores disappear, but if just one core is used the other remains accessible. Through it I can see memory, but still have no idea what happened to the core that went AWOL.

So the next steps are to:

* extract the most recently reported program counter value from the missing core from 'icepick' device via JTAG. This is normally used for non-invasive profiling but in my case the (hopefully recent) snapshot is all the insight we could get into the CPU's internal state.
* get an execution trace, and convince the debugger NOT to look up corresponding memory addresses for disassembly on the target. Remember; the target is ignoring the debugger and it times-out -- nastily.

So, with a trace on file the flow is:

* Core 0: programs a peripheral not to issue any more interrupts
* Core 0: Proceeds to power down the peripheral
* Core 1: Handles an interrupt from the device that was pending from before and was delayed
* Core 1: Writes some registers on the device; issues an Instruction Synchronization Barrier (isb) to sync.
* Device is unpowered - no ack/nack to the transaction on the memory bus. Apparently no timeout from the bus itself either :(
* ISB never completes - core 1 is deadlocked
* presumably, normal cache-coherence traffic propagates the deadlock to the other core.

Objdumping the .ko module for the device, I notice that it fails to call the standard linux API disable_irq() which pretty much targets this exact race scenario: is SMP safe, clears any pending interrupts, notes to ignore future spurious ones.

Basically this whole headache can be fixed by updating the device driver by inserting the appropriate API calls to actually enable and disable interrupts properly.

Now, the problem is explaining why it works fine before integration with my stuff but not after; well, as I found out it's because of my tendency to optimize everything: this race is normally dormant but I jiggled the timing of certain code paths just enough that it become possible for the chance of the race causing issues raises from 'never reliably observed' to 'always after several minutes of running test app'.

Theory-crafting a scenario where the same race could potentially occur helped -- essentially an unfortunately timed high-priority IRQ that is long running (such as maybe a touchscreen event and corresponding i2c work) can keep the RQ in the pending queue long enough for the device to be turned off underneath it.

On the downside, I still have no idea why accessing the powered-down device didn't result in an asynch external abort, like ususally happens when clocking or power-domain code goes wrong. Could be a chipset bug and the controller for whatever memory bus this device hangs off didn't timeout. That wouldn't have solved the issue, but at least we could have traced back from a very visible linux kernel panic.

And people ask me why I love managed environments...
