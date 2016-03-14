title: Prettify your git log graphs
date: 2013-10-03
slug: git-graph-pretty
category: how-to
tags: git, scm

If you're using git as a version control system you must know of the awesomeness that is `git log --graph`; this displays your commits in a nice tree form.

The downside to this is that it can be loooong and hard to parse, so let's prettify it!

By making the following alias you get:

* colors
* graph of commits
* one commit per line
* abbreviated commit IDs
* dates relative to now
* commit references
* author of the commit

And the alias is:

```git
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"
```

What you'll see will be similar to:

![git pretty graph log](/images/git-graph-pretty/git_lg.png)
