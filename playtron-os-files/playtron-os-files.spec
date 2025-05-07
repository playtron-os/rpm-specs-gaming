Name: playtron-os-files
Version: 0.22.3
Release: 2%{?dist}
Summary: Scripts and services for a gaming OS
License: GPL-3.0-only
URL: https://github.com/playtron-os/playtron-os-files
Source0: https://github.com/playtron-os/playtron-os-files/archive/refs/tags/%{version}.tar.gz
BuildArch: noarch
Requires: clatd cloud-utils-growpart fio fio-engine-libaio ladspa-noise-suppression-for-voice parted python3-pygame python3-dbus python3-gobject foot google-noto-sans-mono-cjk-vf-fonts rsync stress-ng vkmark alsa-utils /usr/bin/ffmpeg powerstation upower zram-generator
BuildRequires: systemd-rpm-macros
Obsoletes: playtron-os-scripts <= 0.5.1-1
Conflicts: playtron-os-scripts zram-generator-defaults

# Disable the unused debug package.
%global debug_package %{nil}

%description
%{summary}.

%prep
%setup -q -c

%install
cp -Rv playtron-os-files-%{version}/etc/ %{buildroot}/
cp -Rv playtron-os-files-%{version}/usr/ %{buildroot}/

mkdir -p %{buildroot}/usr/share/licenses/playtron-os-files/
cp playtron-os-files-%{version}/LICENSE %{buildroot}/usr/share/licenses/playtron-os-files/

%files
/etc/gai.conf
/etc/security/limits.d/50-playtron.conf
/etc/xdg/weston/weston.ini
/etc/xdg/weston/weston-rotated.ini
/usr/bin/clatd-ipv6-check
/usr/bin/hwctl
/usr/bin/playtron-factory-reset
/usr/bin/playtronos-session-select
/usr/bin/playtronos-update
/usr/bin/playtron-weston
/usr/bin/resize-root-file-system.sh
/usr/lib/modprobe.d/50-playtron.conf
/usr/lib/modules-load.d/controllers.conf
/usr/lib/NetworkManager/conf.d/50-playtron.conf
/usr/lib/sddm/sddm.conf.d/55-playtron.conf
/usr/lib/sysctl.d/50-playtron.conf
/usr/lib/systemd/logind.conf.d/00-playtron-power.conf
/usr/lib/systemd/system/clatd-ipv6-check.service
/usr/lib/systemd/system/resize-root-file-system.service
/usr/lib/systemd/system-preset/50-playtron.preset
/usr/lib/systemd/user-preset/50-playtron.preset
/usr/lib/systemd/user/pipewire-rnnoise-switch.service
/usr/lib/systemd/zram-generator.conf
/usr/lib/udev/hwdb.d/59-msi.hwdb
/usr/lib/udev/hwdb.d/59-sui.hwdb
/usr/lib/udev/rules.d/50-ayaneo2s.rules
/usr/lib/udev/rules.d/50-block-scheduler.rules
/usr/lib/udev/rules.d/50-suiplay0x1.rules
/usr/libexec/playtron/dev-session-trigger
/usr/libexec/playtron/hardware-test-tool
/usr/libexec/playtron/stress-test-cpu+ram
/usr/libexec/playtron/stress-test-disk
/usr/libexec/playtron/stress-test-gpu
/usr/libexec/playtron/stress-test-speaker
/usr/share/inputplumber/capability_maps/playtron_ayaneo_type7.yaml
/usr/share/inputplumber/devices/24-playtron-ayaneo_2s_v2.yaml
/usr/share/inputplumber/devices/24-playtron-suiplay0x1_v2.yaml
/usr/share/inputplumber/devices/25-playtron-ayaneo_2.yaml
/usr/share/inputplumber/devices/25-playtron-ayaneo_2s.yaml
/usr/share/inputplumber/devices/25-playtron-legion_go.yaml
/usr/share/inputplumber/devices/25-playtron-msi_claw7_a2vm.yaml
/usr/share/inputplumber/devices/25-playtron-msi_claw8_a2vm.yaml
/usr/share/inputplumber/devices/25-playtron-msi_claw_a1m.yaml
/usr/share/inputplumber/devices/25-playtron-rog_ally.yaml
/usr/share/inputplumber/devices/25-playtron-rog_ally_x.yaml
/usr/share/inputplumber/devices/25-playtron-steam_deck.yaml
/usr/share/inputplumber/devices/25-playtron-suiplay0x1.yaml
/usr/share/licenses/playtron-os-files/LICENSE
/usr/share/pipewire/pipewire.conf.d/pipewire-rnnoise.conf
/usr/share/playtron/test_audio.mp3
/usr/share/playtron/test_video.webm
/usr/share/polkit-1/rules.d/50-one.playtron.factory-reset.rules
/usr/share/polkit-1/rules.d/50-one.playtron.hwctl.rules
/usr/share/polkit-1/rules.d/50-one.playtron.playtronos-session-select.rules
/usr/share/polkit-1/rules.d/50-one.playtron.playtronos-update.rules
/usr/share/polkit-1/rules.d/50-one.playtron.rpmostree1.rules
/usr/share/wayland-sessions/playtron-weston.desktop

%post
%systemd_post clatd-ipv6-check.service sddm.service NetworkManager-wait-online.service resize-root-file-system.service inputplumber.service firewalld.service systemd-zram-setup@zram0.service
%systemd_user_post pipewire-rnnoise-switch.service playserve.service gamescope-dbus.service
systemd-hwdb update

%preun
%systemd_preun clatd-ipv6-check.service sddm.service NetworkManager-wait-online.service resize-root-file-system.service inputplumber.service firewalld.service systemd-zram-setup@zram0.service
%systemd_user_preun pipewire-rnnoise-switch.service playserve.service gamescope-dbus.service

%postun
%systemd_postun clatd-ipv6-check.service sddm.service NetworkManager-wait-online.service resize-root-file-system.service inputplumber.service firewalld.service systemd-zram-setup@zram0.service
%systemd_user_postun pipewire-rnnoise-switch.service playserve.service gamescope-dbus.service

%changelog
* Wed May 07 2025 Alesh Slovak <aleshslovak@gmail.com> 0.22.3-2
- Add missing dependency for the dev-session-trigger script

* Tue May 06 2025 Luke Short <ekultails@gmail.com> 0.22.3-1
- Update version

* Wed Apr 30 2025 Alesh Slovak <aleshslovak@gmail.com> 0.22.2-1
- Update version

* Tue Apr 29 2025 Alesh Slovak <aleshslovak@gmail.com> 0.22.1-1
- Update version

* Thu Apr 17 2025 Luke Short <ekultails@gmail.com> 0.22.0-2
- Add 'rsync' dependency for the factory reset script

* Wed Apr 09 2025 Luke Short <ekultails@gmail.com> 0.22.0-1
- Update version
- Add MSI Claw A2VM controller configurations

* Tue Apr 08 2025 Alesh Slovak <aleshslovak@gmail.com> 0.21.3-1
- Update version
- Add `python3-dbus` dependency for `hardware-test-tool`

* Fri Apr 04 2025 Alesh Slovak <aleshslovak@gmail.com> 0.21.2-1
- Update version

* Tue Apr 01 2025 Luke Short <ekultails@gmail.com> 0.21.1-1
- Update version
- Add microphone noise reduction configuration

* Mon Mar 24 2025 Luke Short <ekultails@gmail.com> 0.20.0-1
- Update version
- Add zram configuration

* Fri Mar 21 2025 Alesh Slovak <aleshslovak@gmail.com> 0.19.4-1
- Update version

* Fri Mar 21 2025 Luke Short <ekultails@gmail.com> 0.19.3-2
- Fix FFmpeg dependency to be more generic

* Fri Mar 21 2025 Alesh Slovak <aleshslovak@gmail.com> 0.19.3-1
- Update version

* Fri Mar 14 2025 Alesh Slovak <aleshslovak@gmail.com> 0.19.2-1
- Update version

* Fri Mar 07 2025 Alesh Slovak <aleshslovak@gmail.com> 0.19.1-1
- Update version

* Tue Feb 11 2025 Alesh Slovak <aleshslovak@gmail.com> 0.18.4-1
- Update version

* Fri Feb 07 2025 Alesh Slovak <aleshslovak@gmail.com> 0.18.3-1
- Update version

* Thu Dec 19 2024 Alesh Slovak <aleshslovak@gmail.com> 0.18.2-1
- Update version

* Mon Dec 16 2024 Alesh Slovak <aleshslovak@gmail.com> 0.18.1-1
- Update version

* Mon Dec 02 2024 Alesh Slovak <aleshslovak@gmail.com> 0.18.0-1
- Update version

* Wed Nov 20 2024 Alesh Slovak <aleshslovak@gmail.com> 0.17.1-1
- Update version

* Fri Nov 01 2024 Luke Short <ekultails@gmail.com> 0.17.0-1
- Update version

* Wed Oct 30 2024 Luke Short <ekultails@gmail.com> 0.16.11-1
- Update version

* Thu Oct 17 2024 Alesh Slovak <aleshslovak@gmail.com> 0.16.10-1
- Update version

* Fri Oct 11 2024 Alesh Slovak <aleshslovak@gmail.com> 0.16.9-1
- Update version

* Fri Sep 20 2024 Luke Short <ekultails@gmail.com> 0.16.8-2
- Disable debug package to fix builds on Fedora 41

* Thu Aug 29 2024 Luke Short <ekultails@gmail.com> 0.16.8-1
- Update version

* Wed Aug 28 2024 Luke Short <ekultails@gmail.com> 0.16.7-1
- Update version

* Thu Aug 22 2024 Alesh Slovak <aleshslovak@gmail.com> 0.16.6-1
- Update version

* Fri Aug 16 2024 Alesh Slovak <aleshslovak@gmail.com> 0.16.5-1
- Update version

* Fri Aug 9 2024 Luke Short <ekultails@gmail.com> 0.16.4-1
- Update version

* Thu Aug 1 2024 Alesh Slovak <aleshslovak@gmail.com> 0.16.3-1
- Update version

* Thu Jul 25 2024 Alesh Slovak <aleshslovak@gmail.com> 0.16.2-1
- Update version

* Wed Jun 26 2024 Alesh Slovak <aleshslovak@gmail.com> 0.16.1-1
- Update version

* Tue Jun 11 2024 Alesh Slovak <aleshslovak@gmail.com> 0.16.0.37-1
- Update version

* Thu Jun 6 2024 Alesh Slovak <aleshslovak@gmail.com> 0.15.0.36-1
- Update version

* Tue May 21 2024 Luke Short <ekultails@gmail.com> 0.14.5.35-1
- Update version

* Tue May 21 2024 Luke Short <ekultails@gmail.com> 0.14.4.34-1
- Update version

* Mon May 20 2024 Alesh Slovak <aleshslovak@gmail.com> 0.14.3.33-1
- Update version

* Fri May 17 2024 Alesh Slovak <aleshslovak@gmail.com> 0.14.2.32-1
- Update version

* Wed May 15 2024 Alesh Slovak <aleshslovak@gmail.com> 0.14.1.31-1
- Update version

* Wed May 8 2024 Alesh Slovak <aleshslovak@gmail.com> 0.14.0.30-1
- Update version

* Wed May 1 2024 Alesh Slovak <aleshslovak@gmail.com> 0.13.3.29-1
- Update version

* Thu Apr 25 2024 Alesh Slovak <aleshslovak@gmail.com> 0.13.2.28-1
- Update version

* Thu Apr 25 2024 Alesh Slovak <aleshslovak@gmail.com> 0.13.1.27-1
- Update version

* Wed Apr 24 2024 Alesh Slovak <aleshslovak@gmail.com> 0.13.0.26-1
- Update version

* Fri Apr 19 2024 Alesh Slovak <aleshslovak@gmail.com> 0.12.5.25-1
- Update version

* Fri Apr 19 2024 Alesh Slovak <aleshslovak@gmail.com> 0.12.4.24-1
- Update version

* Thu Apr 18 2024 Alesh Slovak <aleshslovak@gmail.com> 0.12.3.23-1
- Update version

* Wed Apr 17 2024 Alesh Slovak <aleshslovak@gmail.com> 0.12.2.22-1
- Update version

* Wed Apr 10 2024 Alesh Slovak <aleshslovak@gmail.com> 0.12.1.21-1
- Update version

* Wed Apr 3 2024 Alesh Slovak <aleshslovak@gmail.com> 0.12.0.20-1
- Update version

* Wed Mar 27 2024 Alesh Slovak <aleshslovak@gmail.com> 0.11.0.19-1
- Update version

* Fri Mar 15 2024 Alesh Slovak <aleshslovak@gmail.com> 0.7.1-1
- Update version

* Thu Feb 22 2024 Luke Short <ekultails@gmail.com> 0.7.0-2
- Add all of the managed system and user services
- Add version to the obsoletes field

* Wed Feb 21 2024 Luke Short <ekultails@gmail.com> 0.7.0-1
- Update version
- Add clatd-ipv6-check.service to be managed by systemd macros

* Tue Feb 20 2024 Luke Short <ekultails@gmail.com> 0.6.1-1
- Update version

* Wed Feb 14 2024 Luke Short <ekultails@gmail.com> 0.6.0-1
- Update version

* Wed Feb 14 2024 Alesh Slovak <aleshslovak@gmail.com> 0.5.2-1
- Update version
- Change git repository URL
- Change RPM name from "playtron-os-scripts" to "playtron-os-files"

* Tue Feb 13 2024 Alesh Slovak <aleshslovak@gmail.com> 0.5.1-1
- Update version

* Wed Feb 7 2024 Alesh Slovak <aleshslovak@gmail.com> 0.5.0-1
- Update version

* Thu Jan 25 2024 Alesh Slovak <aleshslovak@gmail.com> 0.4.0-1
- Update version

* Mon Jan 22 2024 Alesh Slovak <aleshslovak@gmail.com> 0.3.1-1
- Update version

* Mon Jan 22 2024 Alesh Slovak <aleshslovak@gmail.com> 0.3.0-1
- Update version

* Wed Oct 18 2023 Luke Short <ekultails@gmail.com> 0.2.1-1
- Update version

* Tue Jun 27 2023 Luke Short <ekultails@gmail.com> 0.2.0-2
- Change git repository URL
- Change RPM name from "gamingos-scripts" to "playtron-os-scripts"

* Thu Jun 01 2023 Luke Short <ekultails@gmail.com> 0.2.0-1
- Add the create swap files
- Change source code version to use a tag instead of a commit hash

* Thu Jun 01 2023 Luke Short <ekultails@gmail.com> 0.1.0-2
- Add cloud-utils-growpart as a required dependency

* Tue May 23 2023 Luke Short <ekultails@gmail.com> 0.1.0-1
- Initial RPM spec created
