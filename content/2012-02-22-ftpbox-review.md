Date: 2012-02-22
Title: A look at FTPbox
Tags: FTPbox, Dropbox, syncing
Category: misc
Slug: ftpbox-review

<img style="float:left; padding-right:10px" src="/images/imported-old/ftpbox.png" />

[Dropbox](https://www.dropbox.com/) is one of the most well known syncing services, and deservedly so, but one downside is that you have to use their servers for storing data, and with that, the account space limits they have in place. But what if you could use your own server to act as a repository for your synced files?

[FTPbox](http://ftpbox.org/) comes to solve just that problem, or at least tries, by offering a way to synchronize your files to your own host, via FTP. The reason I say tries is that FTPbox is still in beta and has a few problems, some caused by the software itself, others caused by the fact that you're limited by what your hosting provider is offering you (in terms of FTP availability and options).

***

The software
------------

I'd first like to address the problems that are strictly tied to the application. First of all, the version I tested (beta 1.8) wanted to write and read its settings file in the \Program Files\FTPbox directory, which always caused an error and eventually crashed on Windows 7 (and it should act the same on Vista) unless it was being run as administrator, which granted read/write privileges for the Program Files folder. Fortunately, because the application is open-source, I've submitted a patch which fixes this problem by saving the settings file under %AppData%, where it should belong.

You also need to use the same location for the sync folder on all computers; if you don't the application will create multiple folders corresponding to the location of the sync folder on the remote computer (see video for more clear example).

Secondly, it feels sluggish and tends to eat up a lot of resources, which makes me think that the application isn't properly threaded (and the code confirms that to some extent); at first I thought that my .Net Framework 4 install got hosed somehow, but after throwing it in a VM the problem persisted.

Another small inconvenience, at least compared to Dropbox, is the fact that it can only watch a single folder, so all the data you want synced must reside in that folder. Add to that the lack of icon overlays to give you visual feedback on the state of the files and folders (syncing, synced, etc.), no indication of the speed of the synchronization process (or a percentage for the current sync) and no shell integration except the tray icon.

What it does offer though is a web interface to manage your files remotely, which currently consists only of uploading files, deleting them or sharing them with other people. So in short, it's pretty basic at this point in time. I need to stress though that this is still a beta, so a work in progress, and a lot of the things I mentioned above can, and hopefully will get fixed.

***

The Service
-----------

Now, the application is only one part of what FTPbox is trying to be, and that is a a synchronizing service. The main problem is that the most important aspects of the service are dependent on your hosting provider.

The first thing that comes to mind is the available space, which tends not to be that large of a problem, with most hosting services offering hundreds of gigabytes of space. What might become a problem though is the maximum bandwidth allowed: if you're trying to sync really large files on multiple computers you can exhaust your available bandwidth relatively easy, especially if you also want to share those files with other people.

The second thing is upload speed, which can vary greatly depending on how close you are to the server; if large services tend to use multiple servers scattered throughout the world which get you good speeds, you're stuck with what you have. And even if the speed might be great for you, it might be extremely slow for your friend in the US with whom you're sharing your files with.

Another aspect to consider is that other services usually backup their data, which means that if anything goes wrong they still have copies. This isn't that large of an issue though considering that you're syncing the files, so they should exist on at least a computer, which in turn will get synced to the cloud - well, to your server.

But the most important part is security. Despite being advertised as secure, it's up to your hosting provider to offer SFTP access for transfer through SSH, or FTPS for TLS/SSL encryption; in case your hosting provider doesn't offer them it means that your data is sent in the clear and anyone listening it can have access to it. You also need to take into account that the files aren't encrypted on the server, which means that there's the possibility that your server admin can view it.

***

The video
---------

Unfortunately, because the application is currently in beta, there were some problems during the recording of the video. I chose to keep everything as is to show the problems a user might face while using it.

Please remember though that FTPbox is a work in progress and this not represent the final version of the software.

Also, sorry for the lack of the mouse cursor, just now noticed that it's missing.

<iframe width="640" height="360" src="http://www.youtube-nocookie.com/embed/tEzhMorMohU?rel=0" frameborder="0" allowfullscreen></iframe>
