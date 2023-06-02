Name: gamingos-scripts
Version: 0.2.0
Release: 1%{?dist}
%define ver 0.2.0
Summary: Scripts and services for a gaming OS
License: Apache-2.0
URL: https://github.com/LukeShortCloud/gamingos-scripts
Source0: https://github.com/LukeShortCloud/gamingos-scripts/archive/refs/tags/%{ver}.tar.gz
BuildArch: noarch
Requires: cloud-utils-growpart

%description
%{summary}.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/etc/sysctl.d/
cp -Rv gamingos-scripts-%{ver}/etc/sysctl.d/* %{buildroot}/etc/sysctl.d/
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp -Rv gamingos-scripts-%{ver}/lib/systemd/system/* %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/sbin/
cp -Rv gamingos-scripts-%{ver}/sbin/* %{buildroot}/usr/sbin/
mkdir -p %{buildroot}/usr/share/licenses/gamingos-scripts/
cp gamingos-scripts-%{ver}/LICENSE %{buildroot}/usr/share/licenses/gamingos-scripts/LICENSE

%files
/etc/sysctl.d/50-swappiness.conf
/usr/lib/systemd/system/create-swap.service
/usr/lib/systemd/system/resize-root-file-system.service
/usr/sbin/create-swap.sh
/usr/sbin/resize-root-file-system.sh
/usr/share/licenses/gamingos-scripts/LICENSE

%post
/usr/bin/systemctl daemon-reload

%postun
/usr/bin/systemctl daemon-reload

%changelog
* Thu Jun 01 2023 Luke Short <ekultails@gmail.com> 0.2.0-1
- Add the create swap files
- Change source code version to use a tag instead of a commit hash

* Thu Jun 01 2023 Luke Short <ekultails@gmail.com> 0.1.0-2
- Add cloud-utils-growpart as a required dependency

* Tue May 23 2023 Luke Short <ekultails@gmail.com> 0.1.0-1
- Initial RPM spec created
