title: Making private tests public
date: 2016-03-09
slug: making-private-tests-public
category: misc
tags: git, AccuRev, scm
summary: Say you've been developing a tool for your company or your own use, and want to make the source public. As any good coder, you've also written some tests, but guess what, those tests can't be easily made available.

Say you've been developing a tool for your company or your own use, and want to make the source public. As any good coder, you've also written some tests, but guess what, those tests can't be easily made available.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Or better said, the tests rely on non-free tools and a specific configuration for them to boot.</p>&mdash; Serban Constantin (@fuzzmz) <a href="https://twitter.com/fuzzmz/status/707493366766895105">March 9, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

To give some more context, the tests are specific to a tool I wrote for migrating history from AccuRev to git. The problem here is that AccuRev is a tool which isn't widely available, and to make things even more fun, we're talking about migrating history, so we need to have a known good state in the tests in order to check the migration was done successfully.

Bellow is a simple test which will fail if the user doesn't have AccuRev installed on his machine:

```python
def test_accurev_login_error_handling():
    assert not accurev_login('badtest', 'badtest')
```

That's a simple one, but we can get into even more complicated ones, like comparing the history obtained by the migration script to a known good configuration:

```python
def test_get_history(set_fixture):
    historyfile = set_fixture[2]
    modhist = set_fixture[3]
    acchist = get_history('Test_gitmigrate_testhist')

    with open(acchist, 'r') as fin:
        content = fin.read().splitlines(True)
    with open(modhist, 'w') as fout:
        fout.writelines(content[4:])
    assert filecmp.cmp(modhist, historyfile)
```

The problem here is that even if the developer has AccuRev installed on his system, there's no way for me to provide him with a valid stream history which will allow the tests to pass because, well, it's history, which contains information like the user who commited the code, when it was commited, what the message was and so on.

I'm wondering what's the proper way to make the tests for such a project available.

* Should I make them public and just note that they'll fail?
* Write a guide on how to modify the tests in order for them to work? But then, doesn't this pose the risk of sabotaging your own tests, so that they'll always pass no mater what?
* Simply mark all AccuRev specific tests are failable and tell possible contributors to enable them if they have AccuRev? But then I'll have to be careful during pull requests to not merge any of the changes done to make the tests work for their specific environment.
* Not publish any tests at all? Or just leave in the very generic python ones?

I know that this is mitigated to some level by the fact that if someone is interested in this migration script they're most likely going to have all the software installed, but it's still a bit of a headache. Not to mention not being able to have automated testing via Travis-CI once the code is made public, which means even more fun with running manual tests in case of a pull request.

So, how would you handle this? Hit me up on Twitter (just reply to the tweets embedded above) or leave me your thoughts on the bellow :fa-google-plus: post.

<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
<div class="g-post" data-href="https://plus.google.com/+SerbanConstantin/posts/DMMDpNHAtTx"></div>
