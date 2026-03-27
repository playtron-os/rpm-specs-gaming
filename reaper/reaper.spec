Name: reaper
Version: 0.1.0
Release: 3%{?dist}
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
mkdir -p %{buildroot}/usr/libexec/playtron
cp reaper-%{version}/build/reaper %{buildroot}/usr/libexec/playtron/

mkdir -p %{buildroot}/usr/share/licenses/reaper/
cp reaper-%{version}/LICENSE %{buildroot}/usr/share/licenses/reaper/

%files
/usr/libexec/playtron/reaper
/usr/share/licenses/reaper/LICENSE

%changelog
* Fri Mar 27 2026 Alesh Slovak <aleshslovak@gmail.com> 0.1.0-3
- Relocate reaper binary to avoid conflict and adhere to standards

* Fri Sep 20 2024 Luke Short <ekultails@gmail.com> 0.1.0-2
- Disable debug package to fix builds on Fedora 41

* Mon Apr 29 2024 Alesh Slovak <aleshslovak@gmail.com> 0.1.0-1
- Initial RPM spec created
