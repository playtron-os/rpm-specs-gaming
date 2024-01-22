Name: gamescope-session-playtron
# GitVersion versioning is to show how many commits have been made to the git repository.
Version: 0.1.0+10
Release: 1%{?dist}
%define ver de109ba0b8db
Summary: Playtron Session for PlaytronOS
License: TBD
URL: https://bitbucket.org/playtron-one/gamescope-session-playtron
Source0: https://bitbucket.org/playtron-one/%{name}/get/%{ver}.tar.gz#/playtron-one-%{name}-%{ver}.tar.gz
Requires: gamescope
Requires: gamescope-session
Requires: playtron-app
Requires: brightnessctl

%description
%{summary}.

%prep
%setup -q -c

%install
cp -Rv playtron-one-%{name}-%{ver}/usr/ %{buildroot}/

%files
/usr/share/gamescope-session-plus/sessions.d/playtron
/usr/share/wayland-sessions/gamescope-session-playtron.desktop
/usr/bin/hwctl
/usr/bin/jupiter-dock-updater
/usr/bin/jupiter-biosupdate
/usr/bin/steamos-update
/usr/bin/playtronos-session-select

%changelog
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
