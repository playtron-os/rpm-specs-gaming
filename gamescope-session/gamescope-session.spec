Name: gamescope-session
# GitVersion versioning is to show how many commits have been made to the git repository.
Version: 0.1.0+288
Release: 1%{?dist}
%define ver f8390d38c1347a3ad60540db95bcca284b0f1982
Summary: Common gamescope session files
License: MIT
URL: https://github.com/ChimeraOS/gamescope-session
Source0: https://github.com/ChimeraOS/gamescope-session/archive/%{ver}.zip
Requires: gamescope

%description
%{summary}.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/usr/share/licenses/gamescope-session-plus
cp -Rv gamescope-session-%{ver}/usr/ %{buildroot}/
rm -f %{buildroot}/usr/README.md
cp gamescope-session-%{ver}/LICENSE %{buildroot}/usr/share/licenses/gamescope-session-plus/LICENSE

%files
/usr/bin/export-gpu
/usr/bin/gamescope-session-plus
/usr/lib/systemd/user/gamescope-session-plus@.service
/usr/libexec/gamescope-sdl-workaround
/usr/share/gamescope-session-plus/device-quirks
/usr/share/gamescope-session-plus/gamescope-session-plus
/usr/share/licenses/gamescope-session-plus/LICENSE

%changelog
* Thu Aug 01 2024 Luke Short <ekultails@gmail.com> 0.1.0+288-1
- Update version
- Add new /usr/libexec/gamescope-sdl-workaround script

* Thu Jun 13 2024 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+247-1
- Update version

* Mon Jan 22 2024 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+224-1
- Update version

* Fri Sep 08 2023 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+206-1
- Update version

* Wed May 03 2023 Luke Short <ekultails@gmail.com> 0.1.0+120-1
- Update version

* Wed Apr 12 2023 Luke Short <ekultails@gmail.com> 0.1.0+119-1
- Initial RPM spec created
