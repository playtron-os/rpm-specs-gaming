Name: gamescope-session
# GitVersion versioning is to show how many commits have been made to the git repository.
Version: 0.1.0+119
Release: 1%{?dist}
%define ver a82c74982d52264056b4f1cc372478a604a3526f
Summary: Steam Big Picture Mode session based on gamescope for ChimeraOS
License: MIT
URL: https://github.com/ChimeraOS/gamescope-session
Source0: https://github.com/ChimeraOS/gamescope-session/archive/%{ver}.zip

%description
%{summary}.

%prep
%setup -q -c
# RPM builds will fail with an error if the shebang of a Python program does not explicility say
# "python2" or "python3" ("python" is not allowed).
sed -i s'/env\ python/env\ python3/'g gamescope-session-%{ver}/usr/share/gamescope-session/gamescope-session-script
sed -i s'/env\ python/env\ python3/'g gamescope-session-%{ver}/usr/bin/steam-http-loader

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
/usr/bin/steamos-polkit-helpers/steamos-update
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
* Wed Apr 12 2023 Luke Short <ekultails@gmail.com> 0.1.0+119-1
- Initial RPM spec created
