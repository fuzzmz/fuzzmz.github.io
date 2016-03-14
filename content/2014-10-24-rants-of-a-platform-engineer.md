title: Rants of a platform engineer
date: 2014-10-24
slug: rants-of-a-platform-engineer
category: misc
tags: devops, rants

Hi, I'm Fuzzmz and I part of my job description is software build and release engineer. If you've recently played with [CodeWarrior Development Studio for QorIQ LS series for ARM v7 ISA](http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=CW-LS-ARM7) or for Power Architecture you should know that the final product builds were done by me.

This means that what I and the rest of my team does is handle the build process, where all components get integrated to form the final product, as well as handling the build and integration system. What follows are a few thoughts based on my experiences and struggles faced so far during my job.

---

I guess a nicer way to name my job would be *platform engineering*, as we are tasked with taking care of a part of the systems which power scalability, fault tolerance, and developer productivity.

Please note though that the following bullet points aren't meant to apply to everyone, nor are all of them in use at my job, though we strive to make things as smooth as possible.

So, without further ado, here are the guidelines we try to adhere to:

1. Systems are provisioned via code
2. Engineers with production responsibilities are embedded with feature teams
3. Monitoring and alert configuration is centralized and easily accessible to the people who need them
4. Systems are self-healing without human involvement
5. Everyday administration tasks are handled through automated systems
6. Configuration data is stored in an auditable central repository
7. Applications are presented with a fresh, consistent runtime regardless of deployment environment
8. Any system that must be deployed more often than monthly does so faster than you can get a cup of coffee

---

###1. Systems are provisioned via code

This is the foundation of everything. Whether it's Chef or Puppet, bash scripts or even VM snapshots, every developer's time and skills should be more valuable than just manually provisioning stuff. Couple that with the inherent systems documentation that you get from reading Chef cookbooks for example and you've got the foundational building block for everything else you do. You just shouldn't *have* time to do otherwise.

---

###2. Engineers with production responsibilities are embedded with feature teams

Despite having a team dedicated to shipping the final product (hi to all of the release engineering guys out there), they don't have time to ship everybody else's stuff, too.

You hire smart people everywhere so who better to know the requirements, pitfalls and shortcuts in building their specific pieces of code? Give them ownership of their own deliverables and rely on the platform team to enable them with tooling and, if needed, assistance in making their deployments possible. This will ensure that they are always in the loop when it comes to the outcome of their builds and deliverable sanity.

---

###3. Monitoring and alert configuration is centralized and easily accessible to the people who need them

Centralized logging and monitoring of system statistics has two major pluses: developer velocity and system self-documentation. SSH may be necessary in the odd edge case, but if somebody has to log into a machine just to read their logs, they're going to be slower when they do it or not do it at all. Make sure that your devs can readily know when something's wrong, or when a fault somewhere else in the .org might affect them.

Also, every data point counts when it comes to logging, so having the record of Things That Have Needed Monitoring can help inform future decisions.

---

###4. Systems are self-healing without human involvement

Do you enjoy waking up to a log full of errors? Or emails from colleagues bitching that something isn't quite working?

In a sane environment, the steps to recover from failure should be well-documented and extremely digital — you should be able to document them as a bunch of if-thens.

Now, I'm pretty sure a healthy environment already has lots of if-then processors lying around. They're called computers. You can rent one that can complete all the if-thens that most failures could ever need for two cents an hour in AWS. It's cheaper than having a meat processor doing the moral equivalent (and then calling you when he or she gets off-book) and more reliable.

An issue that needs to be escalated out-of-hours to a developer should require a postmortem. Turn the results into Python and have it send you an email telling you what it **did**, not what you *need to do*. Then save the shouting, screaming and flailing around for when something is really wrong.

---

###5. Everyday administration tasks are handled through automated systems

I've heard this item expressed in an even more aggressive manner: *no developer should need SSH access to a production system*. I think that's overkill. No matter how much monitoring you stack up, there are some issues that require getting in there and perturbing electrons directly.

But everyday tasks? See point 4. You've got if-then machines all over the place. Use them.

---

###6. Configuration data is stored in an auditable central repository

This should be pretty explicit. Your Chef or Puppet configs? Store them in git, or whatever else DCVS you want. Your build scripts? Git. Your per-app configs? Git. And so on and so forth.

---

###7. Applications are presented with a fresh, consistent runtime regardless of deployment environment

Now, I also handle the installers for the products I cover. And let me tell you, installing on Linux is a bitch, especially when you can't use native packages and have lots and lots of dependencies.

Granted, I'd love nothing more than just offering a pre-configured [Docker](https://www.docker.com/) container with all of our files and binaries in it, but we're still far away from that (the disadvantages of having an IDE which requires a GUI as opposed to a command line suite).

There's nothing worse than plopped down on a machine that's been running for a year-plus, with who-knows-how-many missing patches that dev and test have. This is silly. Give every application a new sandbox and shed no tears when it gets blown away. And if a sandbox is not possible, then make sure that the environment is as close to your tested *standard* as possible.

---

###8. Any system that must be deployed more often than monthly does so faster than you can get a cup of coffee

Please note: this isn't an excuse for really slow coffee machines.

Fast deploys are critical both for developer productivity and for production safety. Everybody knows that distractions cause many developers to lose their flow. Script everything, and test from time to time.

---

OK, rant over. Not sure how to end this, so I'll just point you to the comments form bellow.
