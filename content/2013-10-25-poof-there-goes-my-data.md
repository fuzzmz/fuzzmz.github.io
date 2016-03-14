title: *poof* there goes my data
date: 2013-10-25
slug: poof-there-goes-my-data
category: debug
tags: linux, strace, debug

I was recently playing around with some Linux VMs for work and from time to time I'd end up with the VM restarting.

This in itself was annyoing, but the thing that was really interesting was that some text files weren't modified despite closing the editor some time before the restarts happened.

With this in mind (and blaming myself for being too lazy to install vim and instead used nano) I went ahead and did an strace. What did I find? Saving a file and exiting nano entirely doesn't normally imply an fsync. This means that the file isn't instantly written to disk, but instead it's deferred until the OS does it's clock fsync, which just happens was around the same length of time between me saving the file and the guest OS restarting.

This startx after ^x to exit for a new file named "test" that contains the text "hello\n".

Preparing to save


<!-- language: bash -->
    write(1, "\r\33(B\33[0;7mFile Name to Write: te"..., 313) = 313
    rt_sigaction(SIGTSTP, {SIG_IGN, [], SA_RESTORER, 0x397b635a90}, NULL, 8) = 0
    read(0, "\r", 1)                        = 1
    rt_sigprocmask(SIG_BLOCK, [WINCH], NULL, 8) = 0
    rt_sigprocmask(SIG_UNBLOCK, [WINCH], NULL, 8) = 0
    select(1, [0], NULL, NULL, {0, 0})      = 0 (Timeout)
    getcwd("/home/fuzzmz", 4097)            = 13
    stat("test", 0x7fffabd65d00)            = -1 ENOENT (No such file or directory)
    getcwd("/home/fuzzmz", 4097)            = 13
    stat("test", 0x7fffabd65d00)            = -1 ENOENT (No such file or directory)
    stat("/home/fuzzmz/test", 0x7fffabd65e10) = -1 ENOENT (No such file or directory)
    lstat("test", 0x7fffabd65ce0)           = -1 ENOENT (No such file or directory)
    stat("test", 0x7fffabd65c50)            = -1 ENOENT (No such file or directory)
    umask(0)                                = 02
    umask(02)                               = 0


The important part:


<!-- language: bash -->
    open("test", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 3
    umask(02)                               = 02
    fcntl(3, F_GETFL)                       = 0x8001 (flags O_WRONLY|O_LARGEFILE)
    fstat(3, {st_mode=S_IFREG|0664, st_size=0, ...}) = 0
    mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fb3975af000
    lseek(3, 0, SEEK_CUR)                   = 0
    write(3, "hello\n", 6)                  = 6
    close(3)                                = 0
    munmap(0x7fb3975af000, 4096)            = 0
    stat("test", {st_mode=S_IFREG|0664, st_size=6, ...}) = 0

Process exit and terminal clean up:


<!-- language: bash -->
    rt_sigaction(SIGTSTP, {SIG_IGN, [], SA_RESTORER|SA_RESTART, 0x397b635a90}, {SIG_IGN, [], SA_RESTORER, 0x397b635a90}, 8) = 0
    select(1, [0], NULL, NULL, {0, 0})      = 0 (Timeout)
    select(1, [0], NULL, NULL, {0, 0})      = 0 (Timeout)
    write(1, "\r\33[58d\33[39;49m\33(B\33[m\33[J\33[1;95H\33("..., 109) = 109
    rt_sigaction(SIGTSTP, {SIG_IGN, [], SA_RESTORER, 0x397b635a90}, NULL, 8) = 0
    write(1, "\33[59;1H\33[?1049l\r\33[?1l\33>", 23) = 23
    ioctl(1, SNDCTL_TMR_STOP or SNDRV_TIMER_IOCTL_GINFO or TCSETSW, {B38400 opost isig icanon echo ...}) = 0
    ioctl(0, SNDCTL_TMR_START or SNDRV_TIMER_IOCTL_TREAD or TCSETS, {B38400 opost isig icanon echo ...}) = 0
    ioctl(0, SNDCTL_TMR_TIMEBASE or SNDRV_TIMER_IOCTL_NEXT_DEVICE or TCGETS, {B38400 opost isig icanon echo ...}) = 0
    exit_group(0)                           = ?
    +++ exited with 0 +++


Emacs does not fsync() either. However, vi does fysync().

I seriously thought ANY application that opened a file for write would end up doing an fsync when it closed normally. Like, without even trying specifically in the code to do so - I thought just closing the filehandle would do it.

I guess part of the problem was that historically file systems didn't handle fsync well. A fsync to any file caused the entire file system to sync, making the call extremely expensive.

One thing to remember though is that over NFS a close() implies an implicit fsync(), due to the way the NFS consistency model works, but not on a local fs.
