title: Oh kernel, my kernel
date: 2015-12-10
slug: oh-kernel-my-kernel
category: misc
tags: Android, kernel, linux
summary: So you're a geek and get your hands on the newest Android goodness (say, a Nexus 6P or 5X), install a terminal emulator - you're a geek, remember - and then run `uname -r` only to be surprised at running a kernel that's a couple of years old. Why is that?

#Upstream fast and large, Android slow

One of the most cited reasons for this is that Android kernels still carry a lot of custom patches which are not available in the upstream kernel.

Say that an upstream developer introduces an API change; the first step he should do after this is to check that all existing code compiles and works without regressions. However, he's not obligated to take custom kernel modules (like grsecurity, rt or Android) into account, nor is he responsible for third party drivers.

As such, all of the workload of bringing in upstream changes to the Android kernel lays solely on Google developers, and considering the fast pace of kernel development this task is time consuming.

---

#:fa-exclamation:Except that's not it

The problem is that all of the above simply isn't that accurate. For example, for an Android device running Linux 3.18, there are only 700 patches to Android-ify your kernel (adding modules like cpufreq_interactive, binder, SElinux fixes, etc.). You can see the list of kernel branches supported [here][1] to get an idea on how much, or little, they differ from upstream.

One of the reasons might be that SoC vendor brings up the kernel on a new chip (so Qualcomm for example ensures that everything is working on the SD808/810). The vendor invests and a lot of time and money in making sure everything is stable. The issue here is that the kernel changes a lot of hands: upstream (Linus) provides the base kernel, Google provides the core Android patches on top of a specific version (3.10, 3.14, 3.18, 4.1), the SoC vendor brings up their chip with their own set of patches, and then the actual device OEM will apply the final changes on top to support a specific device.

This means that SoC vendors don't really have an incentive to bring new kernels to an existing chip. Also note that the development time from when a SoC starts getting worked on and when it's released is pretty long, so your kernel might have actually been not that old when it was selected. It's much easier from a SoC vendor perspective to deal with a new kernel when you're working on bringup for a new SoC. Likewise, even if the SoC vendor upgrades a kernel, the OEM would have to pick that up, rebase their device-specific patches on top o it, then go through all the testing and bug fixing that entails.

Realistically that won't happen though, as the SoC vendor is already doing bringup on the next generation of chips, and the OEM is working on their next devices.

---

#Does it matter though?

Well, it doesn't really matter if you're running 3.10 when upstream is at 4.4. If you're on a desktop and there are bugfixes or new drivers that improve some piece of hardware in your system, great, a new kernel might improve your life significantly. For your phone though, the kernel has been developed specifically for your device because the hardware isn't interchangeable.

If there are better drivers or bugfixes from 4.4, they've probably been backported to your device on 3.10 - and yes, those will come in with your standard OTAs. You don't need a full kernel version bump to take advantage of those.

In fact you don't want a full kernel version bump because all of your device and SoC specific code can break in mysterious ways. Watch as some mmc refactoring upstream randomly breaks your wifi driver! Missed one armv8 patch? Boom, random SIMD register corruption that causes programs to randomly segfault. People are especially sensitive to kernel stability on their phones, so the kernels need to be rock solid. Backporting patches to a kernel the SoC vendor has spent a lot of time on making stable is always the safer route.

---

#But what about PCs?

The only reason that this is agnostic to Android devices, and not say, desktop PC's, is because of how drivers/modules are implemented on Android.

Because there is no standardized bootloader on Android, the kernel cannot go about detecting hardware on the platform, and drivers need to be baked into the kernel itself (and thus, loses modularity). This is why it's such an intensive process to upgrade the kernel, as drivers are statically written in, rather than dynamically being linked.

In short, this would be much less of a problem if there were a standardized bootloader, and easy hardware detection in Android Kernel. Once that happens, dynamic linking of modules could be implemented, and much less customization would need to be done to the kernel itself.

In theory, implementing dynamic linking would also be the gateway for Google to provide universal updates to Android devices. It is because of these deep, inflexible changes that Google cannot even begin to push universal updates.

---

#Read more

If you've reached this point and still want more, then you can read [Running a mainline kernel on a cellphone][2] by Jonathan Corbet on the strugles and fun you'd have to face in having the latest and greatest.

[1]: https://android.googlesource.com/kernel/common.git/+refs/ "Refs - kernel/common.git - Git at Google"
[2]: https://lwn.net/Articles/662147/ "Running a mainline kernel on a cellphone"
