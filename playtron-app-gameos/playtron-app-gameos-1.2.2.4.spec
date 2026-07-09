Name: playtron-app-gameos
Version: 1.2.2.4
Release: 1%{?dist}
Summary: A meta package to install essential packages from GameOS
License: MIT
URL: https://www.playtron.one/

Requires: gamescope-dbus >= 1.13.1-1, gamescope-dbus < 1.13.1-2
Requires: gamescope-session >= 0.1.0+333-1, gamescope-session < 0.1.0+333-2
Requires: gamescope-session-playtron >= 0.4.1-1, gamescope-session-playtron < 0.4.1-2
Requires: grid >= 1.36.1-1, grid < 1.36.1-2
Requires: inputplumber >= 0.75.2-0, inputplumber <= 0.75.2-1
Requires: legendary >= 0.20.41-1.playtron, legendary < 0.20.41-2.playtron
Requires: libpact >= 0.3.0-1, libpact < 0.3.0-2
Requires: libplaytron >= 0.4.0-1, libplaytron < 0.4.0-2
Requires: playserve >= 1.24.1-1, playserve < 1.24.1-2
Requires: playtron-plugin-local >= 1.5.0-1, playtron-plugin-local < 1.5.0-2
Requires: plugin-egs >= 1.2.4-1, plugin-egs < 1.2.4-2
Requires: plugin-gog >= 1.1.2-1, plugin-gog < 1.1.2-2
Requires: powerstation >= 0.8.1-1, powerstation < 0.8.1-2
Requires: reaper >= 0.1.0-2, reaper < 0.1.0-3
Requires: SteamBus >= 1.27.3-1, SteamBus < 1.27.3-2
Requires: tzupdate >= 3.1.0-1, tzupdate < 3.1.0-2
Requires: udev-media-automount >= 0.1.0+72-1, udev-media-automount < 0.1.0+72-2
Requires: xdg-desktop-portal-openuri >= 1.0.1-1, xdg-desktop-portal-openuri < 1.0.1-2

%description
%{summary}

%files
# This macro is required for the binary RPM to build but can be left empty.

%changelog
* Fri Mar 27 2026 Luke Short <ekultails@gmail.com> 1.2.2.4-1
- Update version

* Fri Feb 20 2026 Luke Short <ekultails@gmail.com> 1.1.10.0-1
- Initial RPM release
