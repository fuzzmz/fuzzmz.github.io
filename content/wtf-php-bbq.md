title: WTF PHP BBQ
date: 2014-11-10
slug: wtf-php-bbq
category: debug
tags: security, coding, php

Despite me trying to keep an open mind about all programming languages, I just can't stand PHP with its broken defaults and weird-ass quirks. As usual, I'll link to [PHP: a fractal of bad design](http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/) for an all-encompassing article on why PHP sucks, but let me just tell you one of my recent fun times with PHP.

Say you have an encrypted link to a SOAP service provided by a 3<sup>rd</sup> party and you want to connect to it. It's as simple as setting up a SoapClient object to connect using https, right?

```lang-php
$soap = new SoapClient('https://soap.example.com/service.wsdl');
```

That snippet of code is perfectly functional, except that it fails to do one important thing, and that is to provide some semblance of security. You see, by default PHP performs **absolutely no default validation** of any kind. It'll accept self-signed certificates, certificates for the wrong server, etc. Basically, default is completely insecure.

Now, the way to do it is to override the stream it uses (and how many people know about that?), until you stumble through and configure a particular stream type and mistype a parameter (which is a string, not a function/method call, and therefore not actually validated against anything) and then test it you find out it's still broken...

Having to do unexpected work to get a secure connection working properly means the average code on the internet does it wrong and assumes, wrongly, the first piece of code would be secure. It isn't.

The actual solution, and not the 1 liner available above, would be something like:

```lang-php
$stream = stream_context_create(
  array('ssl'=>array(
    'verify_peer' => TRUE,
    'allow_self_signed' => FALSE,
    'capath' => '/etc/ssl/certs',   // Valid in Ubuntu at least
    'verify_depth' => 5,
    'CN_match' => 'soap.example.com'
  )));
$soap = new SoapClient("https://soap.example.com/service.wsdl',array('stream_context'=>$stream));
// Assuming everything above is done correctly this should be secure
// You absolutely -must- validate there are no errors in the above.
```

But hey, at least `"verify_peer" => TRUE` is now the default. It is the default if you have a recent version, which, unless you control the whole stack you will be stuck on a server that defaults to `FALSE` so if there is any chance that code you've written will be run on an unknown version you still have to code it specifically the way you need it configured.

Yay PHP! :puke:
