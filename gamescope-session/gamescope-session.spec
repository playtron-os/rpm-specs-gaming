Name: gamescope-session
# GitVersion versioning is to show how many commits have been made to the git repository.
Version: 0.1.0+318
Release: 1%{?dist}
%define ver 57c46d19724ca2766e81cd2f5ee96b3baf3b8ae3
Summary: Common gamescope session files
License: MIT
URL: https://github.com/ChimeraOS/gamescope-session
Source0: https://github.com/ChimeraOS/gamescope-session/archive/%{ver}.zip
Requires: gamescope

# Disable the unused debug package.
%global debug_package %{nil}

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
/usr/share/gamescope/scripts/99-disable-explicit-sync.lua
/usr/share/gamescope-session-plus/device-quirks
/usr/share/gamescope-session-plus/gamescope-session-plus
/usr/share/licenses/gamescope-session-plus/LICENSE

%changelog
* Fri Aug 1 2025 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+318-1
- Update version

* Thu Jul 24 2025 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+317-1
- Update version

* Fri Jan 10 2025 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+306-1
- Update version

* Mon Dec 02 2024 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+301-1
- Update version

* Fri Sep 20 2024 Luke Short <ekultails@gmail.com> 0.1.0+291-2
- Disable debug package to fix builds on Fedora 41

* Thu Aug 22 2024 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+291-1
- Update version

* Fri Aug 9 2024 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+290-1
- Update version

* Thu Aug 1 2024 Alesh Slovak <aleshslovak@gmail.com> 0.1.0+288-1
- Update version

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
