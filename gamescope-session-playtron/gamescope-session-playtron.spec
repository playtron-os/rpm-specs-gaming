Name: gamescope-session-playtron
Version: 0.2.1
Release: 1%{?dist}
Summary: Playtron Session for PlaytronOS
License: MIT
URL: https://github.com/playtron-os/gamescope-session-playtron
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Requires: gamescope
Requires: gamescope-session
Requires: grid
Requires: brightnessctl

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
/usr/bin/playtronos-session-select

%changelog
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
