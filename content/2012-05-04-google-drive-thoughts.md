Date: 2012-05-04
Title: Google Drive - Not Ready for Primetime
Tags: Google, Google Drive, sync
Category: misc
Slug: google-drive-thoughts

<img style="float:left; padding-right:10px" src="/images/import-old/google-drive.PNG" />

[Google Drive](https://drive.google.com) has been available for some time now and I've been playing with it for a bit. I just want to mention right now that I'm a big Dropbox fan and also a user of Microsoft's SkyDrive.

Going back to Google Drive, there's no burying the lead, it sucks. I've been testing the desktop app for automatically syncing files and there are some fatal flaws that makes it unreliable and unusable.

***

First, it doesn't work. I was able to get the program to error out, just like [seemingly everyone else](http://productforums.google.com/forum/#!topic/drive/8DNEH3U6vbE). Since the error can occur during the initializing phase of the program as well as afterwards, it stops functioning and sometimes cannot be started again without always erroring out. The only fix is to 'disconnect' the drive which is one of the biggest mistakes of all.

Why is that the biggest mistake of all? Because you can only 'reconnect' the drive to an empty folder. If the program gets in an infinite error loop, the only fix is to 'disconnect' the GDrive. When doing so, you are presented with an ominous message that seems like it will delete everything in the GDrive folder, and this isn't too far from the truth. You cannot re-enable the program without pointing it to an empty folder. If you think you're clever, you'd just try to sneak the files back into the folder to work around this strange requirement. This is what I tried and it failed miserably. The program would silently download the files anyway and save one version with a number in the filename.

Now, since the program errors out and requires a re-download of everything, I have to download 90,000 files again. I gave up on this process after 3 days, because I just knew it was going to finish and then decided to error out again.

***

Second, it's slow. No, I'm not talking about upload bandwidth and a currently overloaded service. I mean the method it uses to scan the files and sync them to the cloud version is clumsily done. The overhead for this process is insanely high: there is no way to check for blocks of files, so it must check each file individually. I had only 3 megs worth of files and 2000 updates took a very, very long time. I included some more folders that used many small files (around 90,000 files) and it took days to synchronize.

Also, while copying the files to the folder, the file copy process slowed to a crawl -- a 1 minute process was going to take an hour to finish. I was able to close the program to complete the copy in a normal amount of time. So, file operations are much, much slower when working in this folder and this ties into the third issue below.

***

Third, it only supports a single folder location. This means you'd have to use a link (junction/hardlink,symlink) to other folders outside the 'drive' folder. Because the program only monitors the single folder, any changes to the linked folders will not register and may only be seen and updated during the initial scan at startup. To counter this, folders must be moved to this location and then links placed in the original position. It's just as easy to do as otherwise, but it's extremely counter intuitive and takes a while to figure out through trial and error.

Now, you may say that Dropbox and SkyDrive also support only a single folder location, but at least they know how to parse and use links so that if something in a linked folder changes it gets uploaded then instead of at startup.

***

To sum it up: It's broken, slow enough to make it impractical, 'works' only on a single folder, and the files on your computer are a treated as a 'second class citizen'.
