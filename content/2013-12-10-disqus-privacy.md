title: Disqus and privacy
date: 2013-12-10
slug: disqus-privacy
category: debug
tags: privacy, hacking, social

Remember when I said that I prefer Google+ commenting to other systems because it tries to enforce real names, and thus less trolling and better thought of posts, than other platforms?

Well, it looks like Disqus, which is used by around 50 million users world wide and 750 000 media sites and blogs, and which allows users to use whatever nickname they want, has been hacked - though I guess hack is not exactly the proper term to use.

The Swedish company Resarchgruppen has cracked the Disqus commenting system, enabling them to identify Disqus users by their e-mail addresses. The problem is that this hack relies on the public API to extract MD5 hashes of user e-mail addresses.

For example, registering to use the API and then replacing the api_secret with a valid one, then running the following command would give you the MD5 hash of my Disqus associated email address.

<!-- language: bash -->
    curl 'https://disqus.com/api/3.0/users/details.json?user=username:fuzzmz&api_secret=REPLACE_ME'

An attacker can then match those hashes to email databases, like those from the recent Adobe hack (over 150 million email addresses) thus revealing the true identity of the user.

Now, true, this is against the Disqus TOS for the API, specifically the parts regarding *collecting or harvesting any personally identifiable information*, but let's be honest here, which hacker would really care about that?
