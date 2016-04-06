title: Gerrit out of my review
date: #TODO
slug: gerrit-out-of-my-review
category: ux
tags: code review, git, gerrit, pull requests, github
summary: #TODO

Working as a programmer means that you inadvertently spend time doing code reviews, and if you're not then something isn't quite right in your team/company.

One very popular tool for doing code reviews, at least if you're using git as a source control and versioning system, is [Gerrit][1], initially developed at Google. Despite this, or maybe because of its origins, Gerrit feels to me like the worst possible review system.

My main pet peeve with Gerrit is its granularity: it is at its heart a single patch review system, as opposed to the review a collection of patches (Pull Requests) flows proposed by [GitHub][2] and others; this means that it's extremely hard to see the big picture of a proposed changeset using Gerrit - work on a branch for one week doing 100 commits and you have 100 reviews on your hand, without any way to see a unified diff between your branch as a whole and master.

[1]: https://code.google.com/p/gerrit/ "gerrit - Gerrit Code Review - Google Project Hosting"
[2]: https://help.github.com/articles/using-pull-requests/ "Using pull requests - User Documentation"
