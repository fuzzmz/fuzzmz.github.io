title: Google+ comment numbers in Ghost
date: 2013-11-11
slug: gplus-comment-number-ghost
category: how-to
tags: google, ghost, social

As you might now, this site is running on the [Ghost](https://ghost.org/) blogging platform. One of the "disadvantages" of using Ghost is that it doesn't include a native commenting system.

Now, the reason why I used quote marks when saying disadvantage is because this forces you to make your own mind about what tool you want to use to power your comments instead of relying on what the platform provides.

Me, being the Google fanboy that I am decided to go with using Google+ for the commenting system, thanks to the great guide provided by [Bios Elemental](http://bioselemental.com/ghost-adding-google-comments/) and tweaks by [SEO Michael](http://seo-michael.co.uk/add-google-plus-comments-to-ghost/). One thing was missing though, and that thing was a way to display the number of comments a post has.

This turns out to be not such a hard thing to implement, though it requires some more steps than just modifying the theme template.


1. Linking your Google+ profile to the content

The first step we need to take is to link our Google+ profile to the website we blog on.

To do this we first need to modify our theme so that Google knows that we're the authors.

To do this we need to add `<a href="[profile_url]?rel=author">Google</a>` somewhere in our theme, replacing `[profile_url]` with our Google+ profile ID.

I chose to make this change in the footer of the website which is found in the `default.hbs` file.

For example, this is how my footer section looks like, with the linking code in the copyright section:

<script src="https://gist.github.com/fuzzmz/7420741.js"></script>

After making this change you need to:

* [Sign in to your Google+ profile](http://profiles.google.com/me/about)
* Edit the links section (just click edit on any category and go to the links tab)
* Under *Contributor to* click on *Add custom link* add the link to your blog and save the changes

![Google+ contributor link](/images/gplus-comment-number-ghost/gcontrib.png)

To check that your content is now linked to Google+ you can go to the [structured data testing tool](http://www.google.com/webmasters/tools/richsnippets) and check your URL; if everything is working correctly you should have a message informing you that *Authorship is working for this webpage.*

![Authorship is working](/images/gplus-comment-number-ghost/autorship.png)


2. Insert the comments counter

Now that we have our blog and Google+ account linked up, it's time to actually display the number of comments for each article.

To do this we need to edit the `index.hbs` file which is responsible with displaying our, well, index :)

I think that the best location to display the number a comments an article has is right next to the article title, so we'll modify the `post-title` class to include our counter by adding the following code (this can be used wherever you want the counter to appear):

`<div class="g-commentcount" data-href="{{@blog.url}}{{url}}"></div>`

For example, my article class now looks like this (note the counter code added to the post-title class):

<script src="https://gist.github.com/fuzzmz/7421039.js"></script>

And that's it, restart Ghost and you're good to go!
