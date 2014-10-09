%global owner lzap
%global commit c5a4525bfa3bd9997834d0603c40093e50e3fd19
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     systemd-shortcuts
Version:  0.1.0
Release:  1%{?dist}
Summary:  Bash alias with code completion
Group:    System Environment/Base
License:  GPLv2+
URL:      https://github.com/lzap/systemd-shortcuts
Source0:  https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

Requires: systemd

%description
Provides bash alias with shell completion and legacy systems support

%prep
%setup -q

%build
make

%install
make install PREFIX=%{buildroot}

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/${name}
#%{_datadir}/man/man1/%{name}.1.gz

%changelog
