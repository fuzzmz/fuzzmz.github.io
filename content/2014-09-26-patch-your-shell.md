title: Patch your shell
date: 2014-09-26
slug: patch-your-shell
category: debug
tags: security, bash, shellshock

If you've kept an ear to the Internet for the past two days or so you've most likely heard about the latest exploit running wild, Shellshock, it basically is remote code execution via Bash. You can find more information about the exploit [here](http://www.troyhunt.com/2014/09/everything-you-need-to-know-about.html).

Now, most distros will issue patches to fix this, but if you don't want to wait for those, or if you're running a distro that's no longer supported you can patch Bash yourself.

For those running a Debian based distro (though this should work across the board) you can check if you're vulnerable using:

```lang-bash
$ env var='() { ignore this;}; echo uhoh' bash -c /bin/true
```

If you get a response of `uhoh` you're vulnerable.

---
The fix

We're going to download the latest Bash source, apply the available patches and then compile everything.

Just write the code bellow in an update_bash.sh file and run it as root

```lang-bash
#!/usr/bin/env bash
mkdir bash_source
cd bash_source
wget http://ftp.gnu.org/gnu/bash/bash-4.3.tar.gz
#download all patches
for i in $(seq -f "%03g" 0 29); do wget http://ftp.gnu.org/gnu/bash/bash-4.3-patches/bash43-$i; done
tar zxvf bash-4.3.tar.gz
cd bash-4.3
#apply all patches
for i in $(seq -f "%03g" 0 29);do patch -p0 < ../bash43-$i; done
#build and install
./configure
make
make install
cd ..
cd ..
rm -r bash_source
```

You can now retest to see if you're vulnerable:

```lang-bash
$ env var='() { ignore this;}; echo uhoh' bash -c /bin/true
```

If you get the following response then you're safe.

```lang-bash
bash: warning: var: ignoring function definition attempt
bash: error importing function definition for 'var'
```

Please note though that the patches issued so far don't completely fix the exploit, but make it harder for your system to be compromised.
