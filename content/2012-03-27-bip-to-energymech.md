Date: 2012-03-27
Title: Bip to Energymech IRC log converter
Tags: irc, python, bip, energymech, log, log converter
Category: debug
Slug: bip-to-energymech

The great thing about knowing how to code is being able to build things that help you out.

I've recently had to convert some IRC logs from the [Bip](http://bip.milkypond.org/) format to the Energymech format used by [ZNC](http://wiki.znc.in/) in order to be able to then generate some statistics from them using [pisg](http://pisg.sourceforge.net/).

My first approach was to hack together some macros and just plow through the logs (fortunately there weren't that many), but this had several downsides:

1. by using macros I had to take out certain data which could be used to generate statistics
2. it's a manual job and doesn't scale well time-wise, despite being able to automate it to some extent
3. can't be easily shared with others

After finishing parsing the logs I decided that it's best to make a learning experience out of it and code a Python script that goes through all the logs and generates the correct output; I knew it wasn't a difficult task (heck, I've thrown it together in around 3 hours of coding and debugging overall) so all I had to do was get cracking.

The largest issue I had with it was regarding the way Python handles regex substitution.

<blockquote class="twitter-tweet tw-align-center"><p>Whoever makes me understand why this Python regex substitution doesn't work gets a cookie and my eternal gratitude. <a href="http://t.co/fj8Nn6i4" title="http://bit.ly/GP8lM3">bit.ly/GP8lM3</a></p>&mdash; Serban Constantin (@fuzzmz) <a href="https://twitter.com/fuzzmz/status/184431795746516992" data-datetime="2012-03-27T00:09:01+00:00">March 27, 2012</a></blockquote>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Thanks to the great wonder that is the Internet I could get an answer to my question in a couple of hours and continue on my marry way.

<blockquote class="twitter-tweet tw-align-center"><p>D'oh, strings in Python are immutable so my re.sub doesn't modify the string in place which means I need to, you know, save the result!</p>&mdash; Serban Constantin (@fuzzmz) <a href="https://twitter.com/fuzzmz/status/184479937229627392" data-datetime="2012-03-27T03:20:19+00:00">March 27, 2012</a></blockquote>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Another nice tip I got was to pre-compile the regex before going through the loop which speeds up things considerably when dealing with lots of text. It was as simple as a:

    :::python
    import re

    talk_mask    = re.compile('\!.*?\:')
    connect_mask = re.compile('\!.*?\has')
    quit_info    = re.compile('\quit.*?\]')
    find_nick    = re.compile('\<* .*?\!')
    time_mask    = re.compile('([0-1]\d|2[0-3]):([0-5]\d):([0-5]\d)')

***

[Download](https://github.com/fuzzmz/bip-to-energymech)
-------------------------------------------------------

I've of course made the code public. It can be found and downloaded from [GitHub](https://github.com/fuzzmz/bip-to-energymech) which is also the place to report bugs or make suggestions.
