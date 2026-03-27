Name: reaper-playtron
Version: 0.2.0
Release: 1%{?dist}
Summary: A command to monitor and annotate a process tree
License: MIT
URL: https://github.com/playtron-os/reaper
Source0: https://github.com/playtron-os/reaper/archive/refs/tags/%{version}.tar.gz
BuildRequires: systemd-rpm-macros meson make gcc-c++
Provides: reaper = %{version}
Obsoletes: reaper < %{version}

# Disable the unused debug package.
%global debug_package %{nil}

%description
%{summary}.

%prep
%setup -q -c

%build
cd reaper-%{version}
make

%install
mkdir -p %{buildroot}/usr/bin
cp reaper-%{version}/build/reaper-playtron %{buildroot}/usr/bin/

mkdir -p %{buildroot}/usr/share/licenses/reaper-playtron/
cp reaper-%{version}/LICENSE %{buildroot}/usr/share/licenses/reaper-playtron/

%files
/usr/bin/reaper-playtron
/usr/share/licenses/reaper-playtron/LICENSE

%changelog
* Fri Mar 27 2026 Luke Short <ekultails@gmail.com> 0.2.0-1
- Use new reaper-playtron project name

* Fri Sep 20 2024 Luke Short <ekultails@gmail.com> 0.1.0-2
- Disable debug package to fix builds on Fedora 41

* Mon Apr 29 2024 Alesh Slovak <aleshslovak@gmail.com> 0.1.0-1
- Initial RPM spec created
