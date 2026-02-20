Name: playtron-app-gameos
Version: 1.1.10.0
Release: 1%{?dist}
Summary: A meta package to install essential packages from GameOS
License: MIT
URL: https://www.playtron.one/

Requires: gamescope-dbus >= 1.10.4-1, gamescope-dbus < 1.10.4-2
Requires: gamescope-session >= 0.1.0+319-1, gamescope-session < 0.1.0+319-2
Requires: gamescope-session-playtron >= 0.4.1-1, gamescope-session-playtron < 0.4.1-2
Requires: grid >= 1.24.0-1, grid < 1.24.0-2
Requires: inputplumber >= 0.67.0-0, inputplumber <= 0.67.0-1
Requires: legendary >= 0.20.41-1.playtron, legendary < 0.20.41-2.playtron
Requires: libpact >= 0.3.0-1, libpact < 0.3.0-2
Requires: libplaytron >= 0.4.0-1, libplaytron < 0.4.0-2
Requires: playserve >= 1.15.0-1, playserve < 1.15.0-2
Requires: playtron-plugin-local >= 1.5.0-1, playtron-plugin-local < 1.5.0-2
Requires: powerstation >= 0.7.0-1, powerstation < 0.7.0-2
Requires: reaper >= 0.1.0-2, reaper < 0.1.0-3
Requires: SteamBus >= 1.26.5-1, SteamBus < 1.26.5-2
Requires: tzupdate >= 3.1.0-1, tzupdate < 3.1.0-2
Requires: udev-media-automount >= 0.1.0+72-1, udev-media-automount < 0.1.0+72-2
Requires: xdg-desktop-portal-openuri >= 1.0.1-1, xdg-desktop-portal-openuri < 1.0.1-2

%description
%{summary}

%files
# This macro is required for the binary RPM to build but can be left empty.

%changelog
* Fri Feb 20 2026 Luke Short <ekultails@gmail.com> 1.1.10.0-1
- Initial RPM release
