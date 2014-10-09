%global owner lzap

Name:     systemd-shortcuts
Version:  0.1.0
Release:  2%{?dist}
Summary:  Bash alias with code completion
Group:    System Environment/Base
License:  GPLv2+
URL:      https://github.com/lzap/systemd-shortcuts
Source0:  https://github.com/%{owner}/%{name}/archive/%{version}.tar.gz

Requires: systemd
BuildRequires: asciidoc

%description
Provides bash alias with shell completion and legacy systems support

%prep
%setup -q

%build
make

%install
make install PREFIX=%{buildroot}/usr

%files
%doc README.md
%{_bindir}/sysd
%{_datadir}/bash-completion/sysd
#%{_datadir}/man/man1/%{name}.1.gz

%changelog
* Thu Oct 09 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.0-2
- Added man page

* Thu Oct 09 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.0-1
- Initial release

