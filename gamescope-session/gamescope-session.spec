Name: gamescope-session
# GitVersion versioning is to show how many commits have been made to the git repository.
Version: 0.1.0+247
Release: 1%{?dist}
%define ver c0da7d8a82ec7adf5737b899ea239c137707f60f
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
/usr/share/gamescope-session-plus/device-quirks
/usr/share/gamescope-session-plus/gamescope-session-plus
/usr/share/licenses/gamescope-session-plus/LICENSE

%changelog
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
