Name: gamescope-session-playtron
Version: 0.4.0
Release: 1%{?dist}
Summary: Playtron Session for PlaytronOS
License: MIT
URL: https://github.com/playtron-os/gamescope-session-playtron
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Requires: gamescope
Requires: gamescope-session
Requires: grid
Requires: brightnessctl

# Disable the unused debug package.
%global debug_package %{nil}

%description
%{summary}.

%prep
%setup -q -c

%install
cp -Rv %{name}-%{version}/usr/ %{buildroot}/

%files
/usr/share/gamescope-session-plus/sessions.d/playtron
/usr/share/wayland-sessions/gamescope-session-playtron.desktop
/usr/bin/jupiter-dock-updater
/usr/bin/jupiter-biosupdate
/usr/bin/steamos-update

%changelog
* Mon Aug 04 2025 Alesh Slovak <aleshslovak@gmail.com> 0.4.0-1
- Update version

* Tue Apr 01 2025 Alesh Slovak <aleshslovak@gmail.com> 0.3.3-1
- Update version

* Fri Mar 21 2025 Alesh Slovak <aleshslovak@gmail.com> 0.3.2-1
- Update version

* Fri Mar 07 2025 Alesh Slovak <aleshslovak@gmail.com> 0.3.1-1
- Update version

* Mon Dec 02 2024 Alesh Slovak <aleshslovak@gmail.com> 0.3.0-1
- Update version

* Mon Nov 18 2024 Alesh Slovak <aleshslovak@gmail.com> 0.2.5-1
- Update version

* Fri Nov 01 2024 Luke Short <ekultails@gmail.com> 0.2.4-1
- Update version

* Fri Oct 11 2024 Alesh Slovak <aleshslovak@gmail.com> 0.2.3-1
- Update version

* Fri Sep 20 2024 Luke Short <ekultails@gmail.com> 0.2.2-2
- Disable debug package to fix builds on Fedora 41

* Fri Aug 9 2024 Alesh Slovak <aleshslovak@gmail.com> 0.2.2-1
- Update version

* Tue Feb 13 2024 Alesh Slovak <aleshslovak@gmail.com> 0.2.1-1
- Update version, update dependency name

* Mon Jan 22 2024 Alesh Slovak <aleshslovak@gmail.com> 0.2.0
- Update to use GitHub repo

* Wed Dec 13 2023 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+10
- Update version

* Tue Nov 21 2023 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+9
- Update version

* Fri Nov 10 2023 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+6
- Update version

* Wed Nov 8 2023 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+5
- Update version

* Mon Oct 16 2023 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+4
- Update version

* Mon Oct 2 2023 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+3
- Initial RPM spec created
