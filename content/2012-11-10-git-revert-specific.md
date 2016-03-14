Date: 2012-11-19
Title: Git revert to commit
Tags: git, revert, undo
Category: debug
Slug: git-revert-specific

Have you ever made a git commit only to figure out that it wasn't such a good idea? How about wanting to go back in your history and reverting to a specific commit? It's actually simple once you know how to do it:

	:::git
	git reset 56e05fced
	git reset --soft HEAD@{1}
	git commit -m "Revert to 56e05fced"
	git reset --hard

Just replace 56e05fced with the commit code you want to revert to.

1.  The first line resets the index to a former commit (56e05fced in this case).
2.  The second line moves the pointer back to the previous head.
3.  Third line is self explanatory (commits the changes with a message).
4.  Last tine updates the working copy to reflect the new commit

Then all you have to do is push the changes with a ```git push origin master``` or whatever your branch may be.
