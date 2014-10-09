%global owner lzap

Name:     systemd-shortcuts
Version:  0.1.3
Release:  1%{?dist}
Summary:  Bash alias with code completion
Group:    System Environment/Base
License:  GPLv2+
URL:      https://github.com/lzap/systemd-shortcuts
Source0:  https://github.com/%{owner}/%{name}/archive/%{version}.tar.gz

BuildArch: noarch

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
%{_datadir}/man/man8/%{name}.8.gz
%{_datadir}/man/man8/sysd.8.gz
%{_datadir}/man/man8/syd.8.gz

%changelog
* Thu Oct 09 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.3-1
- Removed systemd requirement

* Thu Oct 09 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.2-1
- Fixed architecture (noarch)

* Thu Oct 09 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.1-1
- Improved makefile and man pages

* Thu Oct 09 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.0-2
- Added man page

* Thu Oct 09 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.0-1
- Initial release

