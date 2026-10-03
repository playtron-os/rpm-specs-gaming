Name: playtron-app-gameos
Version: 1.3.0.12
Release: 1%{?dist}
Summary: A meta package to install essential packages from GameOS
License: MIT
URL: https://www.playtron.one/

Requires: gamescope-dbus = 1.13.2-1
Requires: gamescope-session = 0.1.0+333-1.fc43
Requires: gamescope-session-playtron = 0.5.0-1.fc43
Requires: grid = 1.36.5-1.fc41
Requires: inputplumber%{?_isa} = 0.76.0-1.fc43
Requires: legendary = 0.20.44-1.playtron
Requires: libpact%{?_isa} = 0.3.0-2
Requires: libplaytron%{?_isa} = 0.4.0-2
Requires: playserve = 1.27.0-1
Requires: playtron-plugin-local = 1.6.1-1
Requires: plugin-egs = 1.3.0-1
Requires: plugin-gog = 1.1.3-1
Requires: powerstation = 0.8.1-1
Requires: reaper = 0.1.0-3.fc43
Requires: SteamBus = 1.27.6-1.fc41
Requires: tzupdate = 3.1.0-1.fc43
Requires: udev-media-automount = 0.1.0+72-1.fc43
Requires: xdg-desktop-portal-openuri = 1.0.1-1.fc43

%description
%{summary}

%files
# This macro is required for the binary RPM to build but can be left empty.

%changelog
* Wed Sep 30 2026 Luke Short <ekultails@gmail.com> 1.3.0.12-1
- Update version

* Fri Mar 27 2026 Luke Short <ekultails@gmail.com> 1.2.2.4-1
- Update version

* Fri Feb 20 2026 Luke Short <ekultails@gmail.com> 1.1.10.0-1
- Initial RPM release
