Name: gamescope-session
# GitVersion versioning is to show how many commits have been made to the git repository.
Version: 0.1.0+190
Release: 1%{?dist}
%define ver 42751dd77d6ae17163e20983b227d3a05a4217a0
Summary: Steam Big Picture Mode session based on gamescope for ChimeraOS
License: MIT
URL: https://github.com/ChimeraOS/gamescope-session
Source0: https://github.com/ChimeraOS/gamescope-session/archive/%{ver}.zip
Requires: gamescope

%description
%{summary}.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/usr/share/licenses/gamescope-session
cp -Rv gamescope-session-%{ver}/usr/ %{buildroot}/
rm -f %{buildroot}/usr/README.md
cp gamescope-session-%{ver}/LICENSE %{buildroot}/usr/share/licenses/gamescope-session/LICENSE

%files
/usr/bin/export-gpu
/usr/bin/gamescope-session
/usr/bin/jupiter-biosupdate
/usr/bin/steam-http-loader
/usr/bin/steamos-polkit-helpers/jupiter-biosupdate
/usr/bin/steamos-polkit-helpers/steamos-select-branch
/usr/bin/steamos-polkit-helpers/steamos-update
/usr/bin/steamos-select-branch
/usr/bin/steamos-session-select
/usr/bin/steamos-update
/usr/lib/systemd/user/gamescope-session.service
/usr/share/applications/gamescope-mimeapps.list
/usr/share/applications/steam_http_loader.desktop
/usr/share/gamescope-session/device-quirks
/usr/share/gamescope-session/gamescope-session-script
/usr/share/licenses/gamescope-session/LICENSE
/usr/share/polkit-1/actions/org.chimeraos.update.policy
/usr/share/wayland-sessions/gamescope-session.desktop

%changelog
* Fri Sep 08 2023 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+190-1
- Update version

* Wed May 03 2023 Luke Short <ekultails@gmail.com> 0.1.0+120-1
- Update version

* Wed Apr 12 2023 Luke Short <ekultails@gmail.com> 0.1.0+119-1
- Initial RPM spec created
