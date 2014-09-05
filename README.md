Shell shortcuts for systemd with aliases
========================================

*Warning: This is just on a paper at the moment*

Tired of typing

    systemc<TAB>

to do call `systemctl`?

Don't like typing

    systemd-cgl<TAB>

to get list cgroups processes?

You are on the right place.

Why sysd
--------

My motivation to select `sysd` as the preferred default alias was simple. I
wanted something that one can type with only left hand, because most people are
right-handed and use mouse. Second, I wanted a name that is not present on
Fedora-based and Debian-based systems. Also it should be as short as possible
while clear to understand for those who see this on a screencast or something.
Also people tend to create short aliases like `g`, `gs` or `gg` and I did not
want the alias to collide.

In addition to the default `sysd`, systemd-shortcuts installs a symlink called
`syd` which is even shorter, but perhaps harder to understand for newcomers or
less appropriate. I think the letter saved is not worth it, but let's see how
people like it. I can always remove the symlink in the next major release.

For now, the following two commands are equivalent:

    sysd help
    syd help

One letter shortcuts
--------------------

The key concept of systemd-shortcuts are, you guessed it, one letter shortcuts.
They are carefully selected and they will not change in future. It is obvious
that the one-letter space is small and it should not be blindly polluted.

The following table shows all one letter shortcuts:

| sysd shortcut | systemd binary |
| ------------- | -------------- |
| sysd s | systemctl |
| sysd j | journalctl |
| sysd h | hostnamectl |
| sysd n | systemd-nspawn |

The following symlinks are installed in case you miss the space. They work as expected:

    sysds
    syds

Complete mapping
----------------

| sysd command | systemd binary |
| ------------ | -------------- |
| sysd bootctl | bootctl |
| sysd hostnamectl | hostnamectl |
| sysd journalctl | journalctl |
| sysd localectl | localectl |
| sysd loginctl | loginctl |
| sysd machinectl | machinectl |
| sysd timedatectl | timedatectl |
| sysd analyze | systemd-analyze |
| sysd ask-password | systemd-ask-password |
| sysd cat | systemd-cat |
| sysd cgls | systemd-cgls |
| sysd cgtop | systemd-cgtop |
| sysd coredumpctl | systemd-coredumpctl |
| sysd delta | systemd-delta |
| sysd detect-virt | systemd-detect-virt |
| sysd inhibit | systemd-inhibit |
| sysd machine-id-setup | systemd-machine-id-setup |
| sysd notify | systemd-notify |
| sysd nspawn | systemd-nspawn |
| sysd run | systemd-run |
| sysd stdio-bridge | systemd-stdio-bridge |
| sysd tmpfiles | systemd-tmpfiles |
| sysd tty-ask-password-agent | systemd-tty-ask-password-agent |

As you can see the mapping is pretty straightforward, in addition to the
one-to-one mapping the following aliases are available:

| sysd command | systemd binary |
| ------------ | -------------- |
| sysd | *expands to the last command* |
| sysd help | shows manual page |
| sysd lscg | systemd-cgls |
| sysd topcg | systemd-cgtop |

Wait, a shell wrapper
---------------------

Around *systemd*? Craziness!

Nope, this is just proof-of-concept. If it is successful enough, I'll write some C-code. I know, every tick counts.

