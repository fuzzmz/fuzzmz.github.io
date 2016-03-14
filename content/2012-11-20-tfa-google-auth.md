Date: 2012-11-20
Title: Two-factor auth with Google Authenticator
Tags: Debian, Google, security, TFA, T-FA, 2FA
Category: how-to
Slug: tfa-google-auth

The reason
----------

As you may remember I've went through [a bit of an ordeal](//fuzz.me.uk/locked-out/) trying to secure my server by allowing users to log in only with certificates. This had the advantage of being more secure than a password but, as time went on, the big disadvantage of not being able to log in from PCs which lacked the certs.

Moving forward (and doing a fresh install on the VPS, which I'll address in a future post) I've went back on my decision to only allow certificate based logins. The downside to this change is that I felt the the server was still exposed despite using a strong password.

Fortunately Google offers a nice Authenticator application for smartphones as well as offering a [pluggable authentication module (PAM)](https://code.google.com/p/google-authenticator/) which ties in with the Authenticator app for two-factor authentication on login. This means that besides knowing the username and password someone would need to have a time-based one-time password generated by the app in order to log in to the site.

***

Installing google-authenticator PAM
-----------------------------------

I'm running Debian so this guide applies to Debian and Debian-based distributions.

First of all we're going to need to install the build-essential package which will allow us to actually install the software.

	sudo apt-get install build-essential

After we've got them installed we're going to install some dependencies needed for the PAM module to work (libpam-dev) as well as to retrieve (git) and easily configure the software (libqrencode-dev).

	sudo apt-get install git libpam-dev libqrencode-dev libpam0g-dev

Now let's go ahead and download the code:

	git clone https://code.google.com/p/google-authenticator/

This grabs the files from Google's server and creates a local copy. After that's done navigate to the google-authenticator/libpam directory and run

	sudo make install

Now that we've got everything installed it's time to actually set up the application. This is extremely easy, just run ```google-authenticator``` which will generate a QR code (thanks to the libqrencode-dev package); scan this code in the Google Authenticator mobile app (or enter the information by hand) and head back to your PC to finish setting up the software by answering the questions it asks.

***

Setting up the OS to use Challenge Response Authentication
----------------------------------------------------------

Once the previous step is done we need to let the OS know that is has to use the newly installed PAM module. To do this we need to edit the ```/etc/pam.d/common-auth``` (by running ```sudo vim /etc/pam.d/common-auth``` for example) and adding the following line:

	auth    required                        pam_google_authenticator.so

Next up is the ssh_config file in order to allow SSH to send challenge requests:

	sudo vim /etc/ssh/sshd_config

Find the line containing ```ChallengeResponseAuthentication``` and set it to yes (also uncomment it if it's commented out) so that it looks like:

	ChallengeResponseAuthentication yes

Now all there's left to do is restart the SSH server and to test the change:

	sudo /etc/init.d/ssh restart

The next time you'll log in you should be greeted with a message asking for a verification code after entering the username and password.

	:::bash
	ssh user@host
	Password:
	Verification code:

***

Bonus points
------------

One advantage to this is the fact that even if you log in using a certificate (which bypasses the two-factor authentication) you are still asked for a verification code when trying to elevate to root via sudo for example.