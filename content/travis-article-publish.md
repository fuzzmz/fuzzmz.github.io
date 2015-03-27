title: Travis-CI article publishing
date: 2015-03-25
slug: travis-article-publish
category: how-to
tags: git, Travis-CI, GitHub
summary: Geeking out after switching back the blog to [Pelican][1] and hosting it on [GitHub Pages][2], I decided to set up automated publishing of the HTML content from the markdown articles without manually running Pelican on my own PC. So what better way to do this than plug everything into [Travis CI][3], because continuous integration doesn't automatically imply code.
    [1]: https://github.com/getpelican/pelican "Static site generator that supports Markdown and reST syntax. Powered by Python."
    [2]: https://pages.github.com/ "GitHub Pages"
    [3]: https://travis-ci.org/ "Travis CI - Free Hosted Continuous Integration Platform for the Open Source Community"

#Configuring the job

I'm not going to go through the whole set-up of having Pelican up and running, nor about how to configure GitHub pages in order to publish your blog, though those are some nice ideas for future articles :fa-lightbulb-o:.

The publishing flow would be as follows:

1. Create a separate `article/article-name` branch on which to work on the article
2. Submit a pull request to the `source` branch once the article is finished
3. On pull request merge run a Travis CI job to get the latest changes, publish using Pelican and push the output back to the `master` branch in order to make the changes public.

I am fully aware that this sounds so much more complicated compared to publishing an article using :fa-wordpress: [Wordpress][4] for example, but it fits well into my mostly command line world, :fa-git: and :fa-github: love and general geekiness.

The actual implementation can be split in two:

1. Getting Travis CI to notice that a merge was made
2. Telling Travis CI what to do once `1` happens

---

##1. Travis integration

Actually setting up Travis CI is pretty easy and [their docs][5] are amazing, so in short you flip a setting in your GitHub repository options and add a `.travis.yml` file which basically configures how a Travis CI job works.

My [`.travis.yml`][6] file is as follows:

```lang-yaml
language: python
python:
  - '2.7'
branches:
  only:
  - source
before_install:
  - "export TRAVIS_COMMIT_MSG=\"$(git log --format=%B -n 1 | head -c23)\""
install:
  - pip install -r requirements.txt
  - pip install git+https://github.com/fuzzmz/pelicanfly@font-awesome-4.3.0
script:
  - git config --global user.name "Serban Constantin"
  - git config --global user.email serban.constantin@gmail.com
  - make publish
  - make github
env:
  global:
  - secure: M88dgw5e8vf2W9wXgTJCxPsFfQSjkXeHrPfiyllyd7ypPY0AynIbsLGlvS0d6ZKPlXgHNaVQqRcvGSvobLb5FuADyamvPKNLf+LmUOuRh0aiK91s+kVo9+qobl9a4kgY2n5flbZpWAyOYDlMdwZHl9B9uBK1i5KtZMT1j+FKAEk=
```

This file tells us that the scripts will run on Python 2.7, and to only run when changes happen to the `source` branch.

The next step is to tell Travis that before installing our required packages he should export the git commit message which prompted the build to the `TRAVIS_COMMIT_MSG` variable, which will then be used when pushing the HTML files to the `master` branch (see :fa-code-fork: [Fix missing author and commit message][7]).

After that we go ahead and install all the packages required to publish the blog (Pelican, Markdown, etc), as well as a custom fork of one of the packages and configure git so that the correct author is displayed in the repository `master` branch after pushing the published content to it.

We then go ahead and actually publish the content via `make publish` and push it to GitHub using `make github`, functions which will get explained a bit further down.

One more thing that needs done is to have a way to let Travis push the changes back to the repo. This is done by [generating a token][8] on GitHub and encoding it using the [travis ruby application][9] so that others can't use said token to push to my repository.

The last thing that needs to be done is to disable pull request builds in Travis CI to prevent the blog being updated by a pull request.

![disable pull request](/images/travis-article-publish/travis-pull-request.png)

---

##2. Travis commands

The actual steps to publish the blog and push it back to GitHub are detailed in the `Makefile` and called via `make publish` and `make github`.

```lang-makefile
PELICAN=pelican

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py

clean:
    [ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

publish:
    $(PELICAN) $(INPUTDIR) --debug --output $(OUTPUTDIR) --settings $(CONFFILE)

github:
    ghp-import -n -b master -m "${TRAVIS_COMMIT_MSG}" $(OUTPUTDIR)
    @git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git master
```

In the `Makefile` we define the current directory, the directory which holds the articles in markdown, the output directory which will store the generated HTML files as well as the path to the Pelican configuration file.

To publish the blog we simply run Pelican.

To push the changes to the repo so they become live we use `ghp-import` to simplify the process of committing the files and setting the correct branch (`master` in this case) and commit message, and then do a `git push`.

And that's it, now you just have to wait for the Travis CI build to take place, after which your content will be automatically made available.

Oh, and there's also an associated pull request for this article, :fa-code-fork: [add Travis-CI publishing article][10].

[4]: https://en.wordpress.com/ "WordPress.com: Create a free website or blog"
[5]: http://docs.travis-ci.com/user/getting-started/ "Travis CI: Getting started"
[6]: http://goo.gl/KJj2jU
[7]: https://github.com/fuzzmz/fuzzmz.github.io/pull/12 "Fix missing author and commit message #12"
[8]: https://github.com/settings/applications
[9]: https://github.com/travis-ci/travis.rb#installation
[10]: https://github.com/fuzzmz/fuzzmz.github.io/pull/13 "add Travis-CI publishing article"