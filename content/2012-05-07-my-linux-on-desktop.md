Date: 2012-05-07
Title: My Linux on the Desktop
Tags: linux, PC, desktop, virtualization
Category: misc
Slug: my-linux-on-desktop

As some of you know I'm a big Microsoft fanboy as 90% of what I do is based around MS tech (be it C#, .NET, SQL Server and so on); with this in mind I always find myself amused by the eternal "next year will be the year of Linux on PC", which is now accentuated by the lukewarm feelings parts of the internet has over Windows 8.

The problem with Linux on the Desktop is that it doesn't bring anything to the table that can't be achieved in an easier/cleaner fashion using another OS, be it Windows or Mac OS X if you're a Unix fan.

***

Now imagine the following Linux install:

* Xen Hypervisor (GPL2)
* Mint as the main OS
* Point updates are downloaded without interruption of the "default" main OS; when the user clicks on "Upgrade now" the boot process just points to a different image on the disk. If something doesn't work, the user can just use a previous version that did work.
* A new package manager
* The user directory is "protected" by Next3 (or Next4), so that if the "Upgrade now" process creates an incompatible data set, the "Rollback" feature can automatically move back to the correct version of the data.
* All of the above happens without any user visibility other than "Upgrade" and "Rollback"; if architected properly the Rollback can be on a per app basis such that different versions of the OS are loaded simultaneously!

Of course this feature isn't going to be consumer desired, but it does fix a problem consumers have; systems getting out of date and compatibility when systems do get updated. When coupled with Next3 you can also implement a safety net for data backup, for example, that file versioning can be used to implement a "backup vault" to protect the user from accidental deletes and changes.

Even better if you've already got the setup for Xen+Multiple OSes, you can bake in "read only" features to improve the security of the system. If something appears to "compromise" one of the guest OSes, it can be re-initialized and the user warned of which site/activity/program caused the problem.

So that immediately gives Linux the possibility of an OS advantage if an OEM were to take advantage of these features. Continuous update, continuous compatibility, and continuous backup/restore are all features currently lacking from "mainstream" Linux today that are actually rather valuable. It's also worth noting that OS X and Windows already offer something like "Continuous update", but don't truly promise "continuous compatibility".

The sandboxing is also a good feature even if it isn't in of itself a strong selling point.

To further mix it up the App Store model can be implemented ala the stable/unstable channel, adding another dimension of trusted/untrusted, where untrusted code/apps are "uncurated" and trusted code is "curated". Users can have the advantages of iOS as well as the flexibility of OSS and "open" app stores. With the sandbox and hypervisor the threat of untrusted code is also diminished if untrusted apps are launched into special guest OSes.
