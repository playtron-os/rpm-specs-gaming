Name: reaper
Version: 0.1.0
Release: 2%{?dist}
Summary: A command to monitor and annotate a process tree
License: MIT
URL: https://github.com/playtron-os/reaper
Source0: https://github.com/playtron-os/reaper/archive/refs/tags/%{version}.tar.gz
BuildRequires: systemd-rpm-macros meson make gcc-c++

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
cp reaper-%{version}/build/reaper %{buildroot}/usr/bin/

mkdir -p %{buildroot}/usr/share/licenses/reaper/
cp reaper-%{version}/LICENSE %{buildroot}/usr/share/licenses/reaper/

%files
/usr/bin/reaper
/usr/share/licenses/reaper/LICENSE

%changelog
* Fri Sep 20 2024 Luke Short <ekultails@gmail.com> 0.1.0-2
- Disable debug package to fix builds on Fedora 41

* Mon Apr 29 2024 Alesh Slovak <aleshslovak@gmail.com> 0.1.0-1
- Initial RPM spec created
