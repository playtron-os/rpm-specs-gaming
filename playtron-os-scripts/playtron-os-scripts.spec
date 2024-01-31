Name: playtron-os-scripts
Version: 0.3.1
Release: 1%{?dist}
Summary: Scripts and services for a gaming OS
License: Apache-2.0
URL: https://github.com/playtron-os/playtron-os-scripts
Source0: https://github.com/playtron-os/playtron-os-scripts/archive/refs/tags/%{version}.tar.gz
BuildArch: noarch
Requires: cloud-utils-growpart fio parted

%description
%{summary}.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/etc/sysctl.d/
cp -Rv playtron-os-scripts-%{version}/etc/sysctl.d/* %{buildroot}/etc/sysctl.d/
mkdir -p %{buildroot}/usr/bin/
cp -Rv playtron-os-scripts-%{version}/bin/* %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp -Rv playtron-os-scripts-%{version}/lib/systemd/system/* %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/share/licenses/playtron-os-scripts/
cp playtron-os-scripts-%{version}/LICENSE %{buildroot}/usr/share/licenses/playtron-os-scripts/LICENSE

%files
/etc/sysctl.d/50-swappiness.conf
/usr/bin/create-swap.sh
/usr/bin/hwctl
/usr/bin/resize-root-file-system.sh
/usr/lib/systemd/system/create-swap.service
/usr/lib/systemd/system/resize-root-file-system.service
/usr/share/licenses/playtron-os-scripts/LICENSE

%post
/usr/bin/systemctl daemon-reload

%postun
/usr/bin/systemctl daemon-reload

%changelog
* Mon Jan 22 2024 Alesh Slovak <aleshslovak@gmail.com> 0.3.1-1
- Update version

* Mon Jan 22 2024 Alesh Slovak <aleshslovak@gmail.com> 0.3.0-1
- Update version

* Wed Oct 18 2023 Luke Short <ekultails@gmail.com> 0.2.1-1
- Update version

* Tue Jun 27 2023 Luke Short <ekultails@gmail.com> 0.2.0-2
- Change git repository URL
- Change RPM name from "gamingos-scripts" to "playtron-os-scripts"

* Thu Jun 01 2023 Luke Short <ekultails@gmail.com> 0.2.0-1
- Add the create swap files
- Change source code version to use a tag instead of a commit hash

* Thu Jun 01 2023 Luke Short <ekultails@gmail.com> 0.1.0-2
- Add cloud-utils-growpart as a required dependency

* Tue May 23 2023 Luke Short <ekultails@gmail.com> 0.1.0-1
- Initial RPM spec created
