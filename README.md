sysd(8)
=======
:man source:  sysd
:man manual:  systemd\-shortcuts

NAME
----
systemd-shortcuts - shortcuts for systemd with aliases and completion

SYNOPSIS
--------

    sysd
    sysd s
    sysd j
    sysd h
    sysd n
    sysd systemctl
    sysd bootctl
    sysd hostnamectl
    sysd journalctl
    sysd localectl
    sysd loginctl
    sysd machinectl
    sysd timedatectl
    sysd analyze
    sysd ask-password
    sysd cat
    sysd cgls
    sysd cgtop
    sysd coredumpctl
    sysd delta
    sysd detect-virt
    sysd inhibit
    sysd machine-id-setup
    sysd notify
    sysd nspawn
    sysd run
    sysd stdio-bridge
    sysd tmpfiles
    sysd tty-ask-password-agent
    sysd help

INTRODUCTION
------------

Tired of typing

    systemc<TAB>

to do call `systemctl`?

Don't like typing

    systemd-cgl<TAB>

to get list cgroups processes?

You are on the right place.

    yum -y install systemd-shortcuts
    source /usr/share/bash-completion/sysd || echo "Or re-login"

*Warning: This is just a POC and it can be thrown out or completely rewritten.
This is not anything stable or finished. Send your comments (issues), or
better, Pull Requests.*

DESCRIPTION
-----------

This package provides *sysd* wrapper (think an alias) that calls what is
provided as second option. There are several one-letter shortcuts available
(see bellow) and shell completion.

Some commands are equal:

    sysd systemctl = sysd s = sysd
    sysd journalctl = sysd j
    sysd hostnamectl = sysd h
    sysd systemd-nspawn = sysd n
    sysd cgls = sysd lscg
    sysd cgtop = sysd topcg

ONE LETTER SHORTCUTS
--------------------

The key concept of systemd-shortcuts are, you guessed it, one letter shortcuts.
They are carefully selected and they will not change in future. It is obvious
that the one-letter space is small and it should not be blindly polluted.

The following table shows all one letter shortcuts:

| sysd shortcut | systemd binary |
| ------------- | -------------- |
| sysd s        | systemctl      |
| sysd j        | journalctl     |
| sysd h        | hostnamectl    |
| sysd n        | systemd-nspawn |

TYPO SYMLINKS
-------------

The following symlinks are installed in case you miss the space. They work as
expected:

    sysds
    syds

COMPLETE MAPPING
----------------

| sysd command                | systemd binary                 |
| ------------                | --------------                 |
| sysd systemctl              | systemctl                      |
| sysd bootctl                | bootctl                        |
| sysd hostnamectl            | hostnamectl                    |
| sysd journalctl             | journalctl                     |
| sysd localectl              | localectl                      |
| sysd loginctl               | loginctl                       |
| sysd machinectl             | machinectl                     |
| sysd timedatectl            | timedatectl                    |
| sysd analyze                | systemd-analyze                |
| sysd ask-password           | systemd-ask-password           |
| sysd cat                    | systemd-cat                    |
| sysd cgls                   | systemd-cgls                   |
| sysd cgtop                  | systemd-cgtop                  |
| sysd coredumpctl            | systemd-coredumpctl            |
| sysd delta                  | systemd-delta                  |
| sysd detect-virt            | systemd-detect-virt            |
| sysd inhibit                | systemd-inhibit                |
| sysd machine-id-setup       | systemd-machine-id-setup       |
| sysd notify                 | systemd-notify                 |
| sysd nspawn                 | systemd-nspawn                 |
| sysd run                    | systemd-run                    |
| sysd stdio-bridge           | systemd-stdio-bridge           |
| sysd tmpfiles               | systemd-tmpfiles               |
| sysd tty-ask-password-agent | systemd-tty-ask-password-agent |

As you can see the mapping is pretty straightforward, in addition to the
one-to-one mapping the following aliases are available:

| sysd command | systemd binary                |
| ------------ | --------------                |
| sysd         | *the same effect as 'sysd s'* |
| sysd help    | shows manual page             |
| sysd lscg    | systemd-cgls                  |
| sysd topcg   | systemd-cgtop                 |

LEGACY SYSTEMS SUPPORT
----------------------

When you need to switch between systemd-based and legacy (sysv init) systems,
you probably appreciate that systemd-shortcuts works on these two. Some
commands are mapped to their counterparts:

| sysd command   | legacy command |
| ------------   | -------------- |
| sysd systemctl | /sbin/service  |

SHELL COMPLETION
----------------

This command comes with bash completion. There is no zsh completion support yet.

OPTIONS
-------

Please refer to the systemd man pages and documentation to find out more.

MOTIVATION
----------

My motivation to select `sysd` as the preferred default alias was simple. I
wanted something that one can type with only left hand, because most people
are right-handed and some of them use mouse. Second, I wanted a binary/alias
that is not present on Fedora-based and Debian-based systems. Also it should
be as short as possible while clear to understand for those who see this on a
screencast or something. Also people tend to create short aliases like `g`,
`gs` or `gg` and I did not want the alias to collide so the shortest possible
alias was four or three characters.

In addition to the default `sysd`, systemd-shortcuts installs a symlink called
`syd` which is even shorter, but perhaps harder to understand for newcomers or
less appropriate. I think the letter saved is not worth it, but let's see how
people like it.

TODO LIST
---------

    * syd "shorter" shortcut is not yet implemented
    * typo symlinks are not yet done too

SEE ALSO
--------

*systemd-shortcuts(8)*, *sysd*(8), *syd*(8)

*systemctl*(1), *bootctl*(1), *hostnamectl*(1), *journalctl*(1),
*localectl*(1), *loginctl*(1), *machinectl*(1), *timedatectl*(1),
*systemd-analyze*(1), *systemd-ask-password*(1), *systemd-cat*(1),
*systemd-cgls*(1), *systemd-cgtop*(1), *systemd-coredumpctl*(1),
*systemd-delta*(1), *systemd-detect-virt*(1), *systemd-inhibit*(1),
*systemd-machine-id-setup*(1), *systemd-notify*(1), *systemd-nspawn*(1),
*systemd-run*(1), *systemd-stdio-bridge*(1), *systemd-tmpfiles*(1),
*systemd-tty-ask-password-agent*(1), *systemd-cgls*(1), *systemd-cgtop*(1)

AUTHORS
-------

    * Lukas Zapletal <lzap+public@redhat.com>

CONTRIBUTING
------------

https://github.com/lzap/systemd-shortcuts

