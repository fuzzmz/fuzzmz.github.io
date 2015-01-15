title: Presence indicators
date: 2013-09-26
slug: presence-indicators
category: UX
tags: google, hangouts, IM, chat

<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>

> /> is there anybody out there?

No, really. With the advent of mobile devices we are more connected than ever to all of our friends, acquaintances or random people who happen to have our IM handles. So in this always-connected world do presence indicators have a place of their own?

---

Available/Busy/Away


In the olden days, when geeks were tied to their computers, IM programs came with this wonderful concept of presence indicators such as *available*, *busy* or *away*.

They were meant let the other people around know if you were or not paying attention to the IM application, or, in the case of the most useful status of all **offline / invisible**, make them leave you alone all-together.

But as time passed and people got more and more used to IMing the relevance of the presence indicator diminished; it didn't matter if you were available or busy because 99% of the time you'd end up with a `hey, got a minute?` on your screen. Not even the mighty *invisible* managed to keep them away as services evolved to store offline messages until you'd get back online.

Social anxiety


And because just having people ignore your presence indicator wasn't enough, some insidious developers decided that it would be a good idea to take things a step further and tell you if the other person closed the conversation window.

No, really, just hover or tap on the image above to see what I'm talking about.

<script type="text/javascript">function onHover1()
{
    $("#menuImg1").attr('src', '/images/presence-indicators/im_off_blur.png');
}

function offHover1()
{
    $("#menuImg1").attr('src', '/images/presence-indicators/im_on_blur.png');
}</script>

<p><img id="menuImg1" src="/images/presence-indicators/im_on_blur.png" alt="IM window open indicator" onmouseover="onHover1();" onmouseout="offHover1();" /></p>


This leads to awkward situations when you don't close the window immediately after a heated discussion of fear that the other guy thinking that you're being passive aggressive.

It also makes people assume that just because that indicator is shown (which, unless you're actually offline, is always displayed) you've read the message and are starting a lengthy response to his 3 word query, in turn leading to presence indicators being even more worthless.

Always-connected


But here we are now, with mobile phones and data plans in our pockets, a complete disregard for presence indicators and always-on IM clients.

What's the role of the presence indicator now? I think it's time to move away from the concept of *instant messaging* towards simply *messaging* - the idea being, online state doesn't matter, you just send your message anytime and the person reads and responds to it when they're able.

Google tried to do this with the Hangouts app but the backlash was so huge that in the most recent version they reinstated (though in a somewhat half-assed fashion) presence indicators.

<script type="text/javascript">function onHover2()
{
    $("#menuImg2").attr('src', '/images/presence-indicators/hangouts_new.png');
}

function offHover2()
{
    $("#menuImg2").attr('src', '/images/presence-indicators/hangouts_old-1.png');
}</script>

<p><img id="menuImg2" src="/images/presence-indicators/hangouts_old-1.png" alt="Old Hangouts layout" onmouseover="onHover2();" onmouseout="offHover2();" /></p>


But what's curious is that even the darlings of the IM world, Apple's iMessage and WhatsApp seem to have forgone presence indicators.

"But WhatsApp still has them!" you might say. To this I can only reply with:

![WhatsApp contact list](/images/presence-indicators/whatsapp.png)

The future of presence


Presence needs to change. it needs to be less about idle, away, etc. and more about where it learns how to notify you.

If you never answer when writing an email or using an IDE (or whatever work-related tool) it learns to wait or set up more passive notifications; then when you move over to a game, it pops up about X messages to answer. Or if you only answer certain people during certain hours, to tell you about those and not other people.

We've been having lots and lots of data about our usage, now all that's left is applying some intelligence to that data.

And here's a small poll for those so inclined.

<div class="g-post" data-href="https://plus.google.com/109419825267811970601/posts/TXTrELakTfs"></div>

And as usual, I look forward to your comments down below.
