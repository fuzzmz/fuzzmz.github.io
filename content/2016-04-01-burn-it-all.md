title: Burn it all
date: 2016-04-01
slug: burn-it-all
category: misc
tags: design, wtf
summary: It is a known fact that some of the hardware we sell gets either a bit too hot, or a bit too loud, but I never until now thought that we're throwing out money in the (cooler) wind...
og_image: images/burn-it-all/server-on-fire.jpg


It is a known fact that some of the hardware we sell gets either a bit too hot, or a bit too loud, but I never until now thought that we're throwing out money in the (cooler) wind... at least until we received the following email from one of our field engineers, the people who are in direct contact with our customers and help diagnose their issues.

What follows is a sanitized email from one of them, published with consent and sanitized.

---

> All,
>
> I'd like to share a small story that currently ends with one experimental, somewhat incomplete,
> uncalibrated, but possibly helpful line of cryptic U-Boot environment to keep the suspense going:
>
> > `silentfan=i2c mw 2f 0.1 80; i2c mw 2f 58.1 1; i2c mw 2f 0.1 82; i2c mw 2f 10.1 34; i2c mw 2f 11.1
34; i2c mw 2f 7.1 3f; i2c mw 2f 1.1 f; i2c mw 2f 2.1 f; i2c mw 2f 5.1 f; i2c mw 2f 6.1 f; i2c mw 2f 0.1 80`
>
> The story starts with an BOARD1, involves early and late BOARD2, and goes back to
> a BOARD3.
>
> Once upon a time an engineer received a BOARD1 and got some very explicit comments in the cubicle office
> environment for turning it on because of the noise it made. So he came up with a simple cardboard
> shield for the flat front fan to ensure that all the air actually went through the SoC heatsink properly.
> That way, he could disconnect two of the three fans in the back and add a resistor cable to the front fan
> to slow it down. The BOARD1 was ok then.
>
> Time passes and along comes the first BOARD2 which looked like the early BOARD1 inside the box. After
> turning it on for the very first time, it got turned off VERY quickly because it was much worse. The same
> cardboard shield and modification was added. It was bearable then.
> When another engineer visited the office with an unmodified BOARD2 and used it in open space, he got
> nearly threatened with violence.
> Then new BOARD2s with a black airflow shield over the heatsink happened, which was a really great idea.
> The fans used were not, so that one also got modified by replacing the back fans with quiet ones and
> disconnecting the useless front fan completely. Again it was ok then.
>
> Along the way the engineer discovered that a BOM mistake had been made for the BOARD2 that caused I2C
> to be effectively partially non-functional without software patches to the SDK. Two resistors were
> missing. Adding software patches to the SDK for U-Boot and Linux, all I2C magically worked, and, e.g,
> temp sensors could suddenly be used. This was important because some customers wanted to know
> much more about the thermal side of our high end chips and jet engine fans didn't position us well
> against Intel. Also, over 100 of the BOARD2s were to be modified also to be quiet by buying many few
> fans and resistors to address a specific market. The new part number for such systems is XXXX.
> The engineer that started the idea didn't really like the extra effort and cost that someone would have to
> spend to make this happen, so he thought about the topic some more, to see if there was a simpler way
> to make the system quiet.
>
> Along comes a new special customer opportunity asking for a BOARD1 in an application space where you can't
> sell by going there with a noisy box. So a BOARD1 was found to be modified, but the engineer was still thinking
> about inexpensive options to make BOARD2s office use compatible.
> Wasn't there a device in there called W83793G in both the BOARD2 and BOARD1 schematics called "Winbond H/W
> Monitor"? Wasn't that device capable of doing PWM fan control? Wasn't it also capable of measuring
> temp and doing autonomous fan control properly? Couldn't that chip be configured to do the right thing
> about fans and noise?
>
> So he looked at the different boards available to him and found the following situation:
>
> * BOARD1
>     * The W83793G is sufficiently wired up in the MODEL1 to be used for autonomous fan
> control. It controls both fan PWM lines and can measure chip temp if properly
> configured. Default pin config settings are not quite ok, but good enough.
>     * The MODEL1 BOARD2s don't have the PWM fans though. They only have fans with the tacho
> signal, so there is nothing to control
>     * The BOARD1s don't have the black shield that current BOARD2s have, so the back fans
> can't be used to create suction through the main heat sink, eliminating all usefulness of
> fan control. This can be remedied with a simple piece of U-shaped cardboard to fill the
> gap between heat sink and back fans... which permits disconnecting the front fan
> completely.
>     * The old MODEL1 did have the four wire PWM fans, but such an old board can
> only serve as spare parts box to strip.
> * BOARD2
>     * The BOARD2 comes with the back airflow shield that is needed for proper heat sink
> temp control through the back fans. The front fan is totally pointless due to the  black
> airflow shield, but we still connect it and pay for it
>     * The fan PWM lines to the W83793G are wired up, so fan speed can be controlled
>     * The W83793G is accessible with I2C SW patches applied to the SDK, despite not being
> quite accessible as the schematics suggest. But XX schematics can be a bit strange
> anyway at times as it seems …
>     * It is shipped with four wire PWM fans that are not perfectly quiet, but quite bearable
> when speed is reduced
>     * … but the temp diodes are disconnected from the W83793G by choice of BOM, so
> automatic control in HW is impossible. Linux could in theory do software based fan
> control but our SDK doesn't.
>
> So we have BOARD1 which would be perfectly capable of being quiet by doing automatic fan control if it
> had the PWM fans and the black airflow shield … but doesn't. *sigh*
>
> And we have BOARD2s which would be perfectly capable of being quiet by doing automatic fan control if
> they had four resistors in a different place on the PCB … but don't. *sigh*
>
> The moral of the story is: We could have saved money on fans and leave a much better impression at
> customers by doing it right with minimal extra review and changes.
>
> Yes, the W83793G is a pretty obsolete part these days and other pure HW means may be better now,
> but the fact that I found now that we had only 95% of the solution in place leads me to the final
> question.
>
> Couldn't we have thought noise and airflow through before we issue a production manufacturing
> order for such boards? We are actively paying for useless BOM that could have been VERY useful.
>
> Coming back to the start: So what is the U-Boot environment line about? If you take PWM fans and put
> them into a BOARD1, add the U-cardboard shape in the back to be like the BOARD2 black airflow shield,
> disconnect the front fan completely, and then run the line … you end up with a reasonable system.
>
> And now I probably should figure out if there is a reasonable way to do SW based fan control on the BOARD2
> under Linux. Too late for the many BOARD2s to be modified … Oh well more money down the drain …
>
> BR
