title: Charge me, baby!
date: 2014-03-08
slug: charge-me-baby
category: misc
tags: batteries, charging

You know, with the number of smartphones increasing in the market I see more and more people spewing bullshit about batteries and how you should charge them.

![featureimage](/images/charge-me-baby/batteries.jpg)

---

###Batteries in an ideal world

When talking about batteries most of the confusion here comes from how differently battery packs are treated to single batteries. What you need to remember is that phones use single batteries.

In an ideal world, if you wanted your battery to last as long as possible you would:

1. Never drain below 60%. CC charging wears the battery more than CV does, CC is used from 0 to 60.
2. Turn the phone off for at least 30 minutes before charging to allow temperature to reach ambient and to avoid charge rate fluctuation.
3. Keep it on external power whenever possible to avoid unnecessary [dis]charging, which is of course unavoidable wear.

However, the difference between CC and CV is only really evident after some years of use, so it's quite safe to just charge it whenever you can, with the provision that if it hits very low levels, charge it sooner rather than later.

---

###Let's talk about myths

The truth is that it doesn't matter if the phone is reading 0, 20, 40 or 50% when you charge it. You're in the CC charge domain regardless. 0% on an Android is usually about 3.0V. This is purely arbitrary and chosen as a balance between battery longevity and battery capacity: It's configurable in the power management IC (set at factory, not aware of any devices which allow it to be changed in the field). Lithium polymer/ion cells are very unhappy below about 2.8V, they go that low and they will suffer greatly.

Let's get geeky!

![voltage_curve](/images/charge-me-baby/voltage_curve.png)
<strong>Voltage curve for a typical smartphone</strong>


See that elbow at 10%? That's the very beginnings of the high damage domain. It doesn't really start until lower than 0% (i.e. fully discharge, then leave for a month so self-discharge does the rest).

So we have three different statuses for the battery to be in. It's either in the low damage domain at 60+%, a charge here will cause very little capacity reduction. There's the medium damage domain between 0% and 60%, try to avoid this if possible, finally the high damage domain overlaps the medium, from 10% down to 2.8V, below 0%: Avoid this one at all costs.

There is one final domain, at about 2.2V, where the cell starts venting hydrogen or swelling if it can't. It might even burst. Once at this point, you might as well get a new battery, because the next charge will find that - permanently - around a quarter of the cell's original capacity is gone. Left for a year or so to discharge and vent, you could well be looking at a majority of the capacity never coming back.

So basically just use your phone and don't let it get too low, but other than that, charge it whenever it's convenient.
