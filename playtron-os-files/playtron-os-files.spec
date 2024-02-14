Name: playtron-os-files
Version: 0.6.0
Release: 1%{?dist}
Summary: Scripts and services for a gaming OS
License: Apache-2.0
URL: https://github.com/playtron-os/playtron-os-files
Source0: https://github.com/playtron-os/playtron-os-files/archive/refs/tags/%{version}.tar.gz
BuildArch: noarch
Requires: clatd cloud-utils-growpart fio parted
BuildRequires: systemd-rpm-macros
Obsoletes: playtron-os-scripts
Conflicts: playtron-os-scripts

%description
%{summary}.

%prep
%setup -q -c

%install
cp -Rv playtron-os-files-%{version}/etc/ %{buildroot}/
cp -Rv playtron-os-files-%{version}/usr/ %{buildroot}/

mkdir -p %{buildroot}/usr/share/licenses/playtron-os-files/
cp playtron-os-files-%{version}/LICENSE %{buildroot}/usr/share/licenses/playtron-os-files/

%files
/etc/gai.conf
/etc/xdg/weston/weston.ini
/usr/bin/clatd-ipv6-check
/usr/bin/create-swap.sh
/usr/bin/hwctl
/usr/bin/playtron-factory-reset
/usr/bin/resize-root-file-system.sh
/usr/lib/sysctl.d/50-swappiness.conf
/usr/lib/systemd/logind.conf.d/00-playtron-power.conf
/usr/lib/systemd/system/clatd-ipv6-check.service
/usr/lib/systemd/system/create-swap.service
/usr/lib/systemd/system/resize-root-file-system.service
/usr/lib/systemd/system-preset/50-playtron.preset
/usr/lib/systemd/user-preset/50-playtron.preset
/usr/lib/udev/rules.d/50-lenovo-legion-controller.rules
/usr/share/licenses/playtron-os-files/LICENSE
/usr/share/lightdm/lightdm.conf.d/55-playtron.conf
/usr/share/polkit-1/rules.d/50-one.playtron.factory-reset.rules
/usr/share/polkit-1/rules.d/50-one.playtron.rpmostree1.rules

%post
%systemd_post create-swap.service resize-root-file-system.service

%preun
%systemd_preun create-swap.service resize-root-file-system.service

%postun
%systemd_postun create-swap.service resize-root-file-system.service

%changelog
* Wed Feb 14 2024 Luke Short <ekultails@gmail.com> 0.6.0-1
- Update version

* Wed Feb 14 2024 Alesh Slovak <aleshslovak@gmail.com> 0.5.2-1
- Update version
- Change git repository URL
- Change RPM name from "playtron-os-scripts" to "playtron-os-files"

* Tue Feb 13 2024 Alesh Slovak <aleshslovak@gmail.com> 0.5.1-1
- Update version

* Wed Feb 7 2024 Alesh Slovak <aleshslovak@gmail.com> 0.5.0-1
- Update version

* Thu Jan 25 2024 Alesh Slovak <aleshslovak@gmail.com> 0.4.0-1
- Update version

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
