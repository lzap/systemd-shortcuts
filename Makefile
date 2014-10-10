PREFIX = $(DESTDIR)/usr/local
BINDIR = $(PREFIX)/bin
DATADIR = $(PREFIX)/share
 
all: sysd systemd-shortcuts.8.gz sysd.8.gz syd.8.gz

systemd-shortcuts.8.asciidoc:
	cat systemd-shortcuts.asciidoc.in > $@
	sed -n '/NAME/,$$p' README.md >> $@

systemd-shortcuts.8.gz: systemd-shortcuts.8.asciidoc
	a2x --verbose -d manpage -f manpage $<
	gzip -9 systemd-shortcuts.8

sysd.8.gz:
	ln -sf systemd-shortcuts.8.gz sysd.8.gz
 
syd.8.gz:
	ln -sf systemd-shortcuts.8.gz syd.8.gz
 
sysd:
	bash -n sysd

install: all
	install -D sysd $(BINDIR)/sysd
	install -Dm644 sysd-completion-bash $(DATADIR)/bash-completion/sysd
	install -Dm644 systemd-shortcuts.8.gz $(DATADIR)/man/man8/systemd-shortcuts.8.gz
	install -Dm644 sysd.8.gz $(DATADIR)/man/man8/sysd.8.gz
	install -Dm644 syd.8.gz $(DATADIR)/man/man8/syd.8.gz
 
clean:
	-rm -f *.8 *.8.gz *.asciidoc
 
distclean: clean
 
.PHONY : all sysd install clean distclean
