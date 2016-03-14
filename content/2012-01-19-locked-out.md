Date: 2012-01-19 23:52
Title: Lockout: no pass, no key
Tags: Linux, d'oh
Category: misc
Slug: locked-out

A foreword
----------

As you may not know, I'm mostly a Microsoft tech junkie venturing into the wonderful world of Linux. I've visited this land from time to time, but never had the time or motivation to try and settle in, but all this is about to change as one of my New Years resolutions was to get my hands dirty in Linux.

Every new beginning is a learning experience, and what better way to learn than from the mistakes made (and the process of trying to fix them)? With this, I bring you my first - and probably not last - embarrassing story.

***

The idea
--------

The goal was noble: *try and make my VPS as secure as possible*. And what better way to achieve this than to disable ssh password authentication, only allowing users to connect with public key authentication?

In the end, it was simple! All I had to do was modify **/etc/ssh/sshd_config** and add

    :::bash
    PasswordAuthentication no

After a restart of the ssh server all was good in the world.

Heck, I was so happy that I managed to get everything running that I even made an excited tweet that would prove to be a bit too prescient for my taste.

<p align="center"><blockquote class="twitter-tweet"><p>Finally managed to get git to behave. I feel so victorious I'd reinstall the server just to do it again. Which reminds me, need backups.</p>&mdash; Serban Constantin (@fuzzmz) <a href="https://twitter.com/fuzzmz/status/159357579846365185" data-datetime="2012-01-17T19:33:00+00:00">January17, 2012</a></blockquote></p>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

***

The catalyst
------------

Every time I logged in, the working directory was **/root** (and yes, I know that I shouldn't use root for my day to day business, but hey, that's why I disabled password authentication) and yet all of my work was done in **/home**. This in turn lead to a very frustrated Fuzz who sought to fix his problem.

I mean, it couldn't be that hard to change the login directory, would it? Heck, Linux even gives you a simple way to do it through

    :::bash
    $ usermod -d newdir loginname

So all I had to do was to run *usermod -d /home root* and I'd be set. Little did I know that:

+  there is an additional parameter, *-m* which moves the contents of the old dir to the new one (\*cough\* \*cough\*);
+  you can't run the command for the user you're currently logged in with.

This meant that I had to search for an alternative: it was changing the directory directly in the **/etc/passwd** file, and so I did.

And things were good!

***

There are no keys to this castle
--------------------------------

A short time passes after changing the passwd file and I decide to do a logout and log back in.

    :::shell
    Permission denied (publickey).

OK, this isn't good, this isn't good at all!

Remember that -m I told you about? Yeah, the one that moves the contents of the old login directory to the new one; well, one of the things it moves is the **.ssh** folder which contains the authorized_keys file.

What's so special about that file? Well, it holds the list of rsa keys which are allowed to access the server. Think of them as the keys that open your house door in the absence of people inside (the password, which I disabled) to open the door for you.

In short:

<p align="center"><blockquote class="twitter-tweet"><p>Just as I got everything running the way I wanted I managed to lock myself out of the server. Fucking piece of shit!</p>&mdash; Serban Constantin (@fuzzmz) <a href="https://twitter.com/fuzzmz/status/159371687379484675" data-datetime="2012-01-17T20:29:00+00:00">January17, 2012</a></blockquote></p>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Fortunately, while bitching on Twitter about the whole situation [Keph](http://twitter.com/Kephu) reminds me that I still have access to the server... somewhat.

***

IRC bouncer to the rescue!
--------------------------

One of the purposes of that VPS is to run [ZNC](http://wiki.znc.in), an IRC bouncer which has some nice capabilities, one of them being a module called *shell* which allow you to type commands into a query as if it were a terminal.

"Yay, I am saved!" thought I, without realizing that I had ZNC run under a non-admin account, exactly because of the shell module. The reasoning is that in case someone hacks my IRC password they won't be able to do any damage as, either by loging in the server directly through ssh or via the shell module.

On the upside, even though I couldn't do much I could at least write an authorized_keys file for that user and get ssh access to the server; this in turn meant that I could back up a portion of my data in case I had to reinstall the server.

***

Admin panel? What admin panel?
------------------------------

Of course, people both in IRC and on Twitter told me to see if I can get access to the server via the admin panel provided by the VPS host. Fortunately for me, they did indeed provide such access via a serial console.

<img style="float:left; padding-right:10px" src="/images/imported-old/magic-button.PNG" />

I had seen this magic button and tried it even before embarking on the amazing IRC-hackathon journey, I, in my eternal wisdom, decided to replace the default username in the dialogue that popped up when I pressed it with root, which in turn led me to the same "Permission denied(publickey)" error message.

This time though, this time it would be different! This time I would leave the default username and gaze upon the wonders of

    :::bash
    root@qwerty:~#

Yes, I was in and victorious!

I quickly created a .ssh/authorized_keys file under my new login directory and started working on my backup strategy.

But about that, in the next blog update.
