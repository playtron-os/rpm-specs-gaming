Name:           legendary
Version:        0.20.41
Release:        1.playtron
Summary:        Free and open-source replacement for the Epic Games Launcher
BuildArch:      noarch

License:        GPL-3.0-or-later
URL:            https://github.com/playtron-os/legendary
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel >= 3.9
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(requests)

Requires:       python3-requests

Recommends:     wine
Recommends:     wine-dxvk

# Disable the unused debug package.
%global debug_package %{nil}

%description
Legendary is an open-source game launcher that can download and install games
from the Epic Games Store on Linux and Windows. It's name as a tongue-in-cheek
play on tiers of item rarity in many MMORPGs.


%prep
%autosetup -p1

# E: non-executable-script
for lib in %{name}/{*.py,downloader/*.py,lfs/*.py,models/*.py}; do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done


%build
%py3_build


%install
%py3_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}*.egg-info/
%{python3_sitelib}/%{name}/


%changelog
* Tue Sep 9 2025 Alesh Slovak <aleshslovak@gmail.com> 0.20.41-1.playtron
- Update version

* Thu Sep 4 2025 Alesh Slovak <aleshslovak@gmail.com> 0.20.40-1.playtron
- Update version

* Fri Aug 22 2025 Alesh Slovak <aleshslovak@gmail.com> 0.20.39-1.playtron
- Update version

* Wed Aug 13 2025 Alesh Slovak <aleshslovak@gmail.com> 0.20.38-1.playtron
- Update version

* Fri May 23 2025 Alesh Slovak <aleshslovak@gmail.com> 0.20.37-1.playtron
- Switch to Playtron fork

* Mon Mar 24 2025 Luke Short <ekultails@gmail.com> 0.20.36-2
- Add reuse chunks backport
- Add wrapper EXE backport
- Add expose summary backport
- Add repair backport

* Wed Oct 30 2024 Luke Short <ekultails@gmail.com> 0.20.36-1
- Update version
- Add conflict resolution backport

* Fri Sep 20 2024 Luke Short <ekultails@gmail.com> 0.20.35-4
- Disable debug package to fix builds on Fedora 41

* Thu Aug 22 2024 Luke Short <ekultails@gmail.com> 0.20.35-3
- Add support for CYGNI: All Guns Blazing

* Thu Aug 22 2024 Luke Short <ekultails@gmail.com> 0.20.35-2
- Add fix for Black Myth: Wukong

* Mon Jul 22 2024 Alesh Slovak <aleshslovak@gmail.com> 0.20.35-1
- Switch to Heroic Games Launcher fork of legendary

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 08 2023 Packit <hello@packit.dev> - 0.20.34-1
- [packit] 0.20.34 upstream release
- Resolves rhbz#2253644

* Fri Dec 08 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.33-4
- license: Convert to SPDX

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 18 2023 Python Maint <python-maint@redhat.com> - 0.20.33-2
- Rebuilt for Python 3.12

* Sat Jun 17 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.33-1
- chore: Update to 0.20.33

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.20.32-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.32-1
- chore: Update to 0.20.32

* Wed Nov 09 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.31-1
- chore: Update to 0.20.31

* Wed Oct 26 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.30-1
- chore(update): 0.20.30

* Fri Sep 16 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.29-1
- chore(update): 0.20.29

* Thu Sep 01 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.28-1
- chore(update): 0.20.28

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 25 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.27-1
- chore(update): 0.20.27

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.20.26-3
- Rebuilt for Python 3.11

* Thu Jun 02 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.26-1
- chore(update): 0.20.26

* Mon Jan 24 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.25-1
- chore(update): 0.20.25

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.24-1
- chore(update): 0.20.24

* Sun Jan 09 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.23-1
- chore(update): 0.20.23

* Wed Dec 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.22-1
- chore(update): 0.20.22

* Mon Dec 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.21-1
- chore(update): 0.20.21

* Wed Dec 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.20-1
- chore(update): 0.20.20

* Sat Dec 04 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.19-1
- chore(update): 0.20.19

* Fri Oct 29 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.18-1
- chore(update): 0.20.18

* Sat Oct 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.17-1
- chore(update): 0.20.17

* Sun Oct 10 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.16-1
- chore(update): 0.20.16

* Sat Oct 09 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.15-1
- chore(update): 0.20.15

* Fri Oct 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.14-1
- chore(update): 0.20.14

* Tue Oct 05 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.13-1
- chore(update): 0.20.13

* Sun Oct 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.12-1
- build(update): 0.20.12

* Sat Oct 02 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.11-1
- build(update): 0.20.11

* Wed Sep 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.10-1
- build(update): 0.20.10

* Tue Sep 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.9-1
- build(update): 0.20.9

* Thu Sep 02 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.7-1
- build(update): 0.20.7

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.20.6-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.6-1
- build(update): 0.20.6

* Mon Dec 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.5-1
- build(update): 0.20.5

* Wed Dec  9 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.4-1
- build(update): 0.20.4

* Wed Nov 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.3-1
- build(update): 0.20.3

* Thu Nov 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.2-1
- build(update): 0.20.2

* Mon Oct  5 16:51:11 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.1-3
- build(add BR): python3-setuptools | per DL-BL7XMXVEHSDZDMH22YET3I4EK66PK4NI

* Wed Sep  9 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.1-2
- Add weak deps: wine & wine-dxvk

* Wed Sep  9 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.1-1
- Update to 0.20.1

* Tue Sep  8 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.19-1
- Update to 0.0.19

* Tue Jun 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.18-1
- Update to 0.0.18

* Sun May 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.17-1
- Update to 0.0.17

* Sat May 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.16-1
- Update to 0.0.16

* Sat May 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.15-1
- Update to 0.0.15

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.14-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.14-1
- Update to 0.0.14

* Sun May 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.13-1
- Update to 0.0.13

* Fri May 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.11-1
- Update to 0.0.11

* Tue May 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.10-1
- Update to 0.0.10

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.9-1
- Update to 0.0.9

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.8-1
- Update to 0.0.8

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.7-1
- Update to 0.0.7

* Thu Apr 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.6-2
- Initial package

## END: Generated by rpmautospec
