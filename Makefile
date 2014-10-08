PREFIX = $(DESTDIR)/usr/local
BINDIR = $(PREFIX)/bin
DATADIR = $(PREFIX)/share
 
all: sysd
 
sysd:
	bash -n sysd

install: all
	install -D sysd $(BINDIR)/sysd
	install -Dm644 sysd-completion-bash $(DATADIR)/bash-completion/sysd
 
clean:
	#-rm -f man
 
distclean: clean
 
.PHONY : all sysd install clean distclean
