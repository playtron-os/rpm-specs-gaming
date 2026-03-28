Name: playtron-app-gameos
Version: 1.2.2.4
Release: 1%{?dist}
Summary: A meta package to install essential packages from GameOS
License: MIT
URL: https://www.playtron.one/

Requires: gamescope-dbus = 1.13.1-1
Requires: gamescope-session = 0.1.0+333-1.fc42
Requires: gamescope-session-playtron = 0.4.1-1.fc42
Requires: grid = 1.36.1-1.fc41
Requires: inputplumber(x86_64) = 0.75.2
Requires: legendary = 0.20.41-1.playtron
Requires: libpact%{?_isa} = 0.3.0-1
Requires: libplaytron%{?_isa} = 0.4.0-1
Requires: playserve = 1.24.1-1
Requires: playtron-plugin-local = 1.5.0-1
Requires: plugin-egs = 1.2.4-1
Requires: plugin-gog = 1.1.2-1
Requires: powerstation = 0.8.1-1
Requires: reaper = 0.1.0-2.fc42
Requires: SteamBus = 1.27.3-1.fc41
Requires: tzupdate = 3.1.0-1.fc42
Requires: udev-media-automount = 0.1.0+72-1.fc42
Requires: xdg-desktop-portal-openuri = 1.0.1-1.fc42

%description
%{summary}

%files
# This macro is required for the binary RPM to build but can be left empty.

%changelog
* Fri Mar 27 2026 Luke Short <ekultails@gmail.com> 1.2.2.4-1
- Update version

* Fri Feb 20 2026 Luke Short <ekultails@gmail.com> 1.1.10.0-1
- Initial RPM release
