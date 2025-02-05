Name: valve-firmware
# There are two source packages that use a date version. Set the RPM version to mirror whichever source is newer.
Version: 20240917.1
Release: 3%{?dist}
Summary: Linux firmware files for the Steam Deck OLED
License: GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL: https://steamdeck-packages.steamos.cloud/archlinux-mirror/jupiter-main/os/x86_64/
Source0: https://steamdeck-packages.steamos.cloud/archlinux-mirror/jupiter-main/os/x86_64/linux-firmware-neptune-jupiter.%{version}-2-any.pkg.tar.zst
Source1: https://steamdeck-packages.steamos.cloud/archlinux-mirror/jupiter-main/os/x86_64/linux-firmware-neptune-20230121.1f01c88-1-any.pkg.tar.zst
Source2: https://steamdeck-packages.steamos.cloud/archlinux-mirror/jupiter-main/os/x86_64/steamdeck-dsp-0.49.5-1-any.pkg.tar.zst
BuildArch: x86_64
BuildRequires: xz zstd
Requires: atheros-firmware cirrus-audio-firmware linux-firmware
Recommends: pipewire-alsa systemd wireplumber
Conflicts: steamdeck-dsp steamdeck-firmware

# Disable the unused debug package.
%global debug_package %{nil}

%description
%{summary}.

%prep
# Extract both source archives.
%setup -q -c -a 0
%setup -q -c -a 1

%install
mkdir -p \
  %{buildroot}/%{_prefix}/lib/firmware/ath11k \
  %{buildroot}/%{_prefix}/lib/firmware/cirrus

# Fedora uses XZ compression by default for kernel modules to save space.
# Some files are already compressed with Zstandard. Change them to XZ.
zstd --decompress --rm usr/lib/firmware/ath11k/QCA206X/hw2.1/*
xz --check=crc32 usr/lib/firmware/ath11k/QCA206X/hw2.1/{amss.bin,board-2.bin,board.bin,regdb.bin}
## Recreate symlinks.
rm -f \
  usr/lib/firmware/ath11k/QCA206X/hw2.1/boardg.bin.zst \
  usr/lib/firmware/ath11k/QCA206X/hw2.1/m3.bin.zst
ln -s board.bin.xz usr/lib/firmware/ath11k/QCA206X/hw2.1/boardg.bin.xz
ln -s ../../QCA2066/hw2.1/m3.bin.xz usr/lib/firmware/ath11k/QCA206X/hw2.1/m3.bin.xz
mv usr/lib/firmware/ath11k/QCA206X %{buildroot}/%{_prefix}/lib/firmware/ath11k/

xz --check=crc32 usr/lib/firmware/cs35l41-dsp1-spk-{cali.bin,cali.wmfw}
mv usr/lib/firmware/cs35l41-dsp1-spk-{cali.bin,cali.wmfw}.xz %{buildroot}/%{_prefix}/lib/firmware/cirrus/

tar -xvf %{_sourcedir}/steamdeck-dsp-0.49.5-1-any.pkg.tar.zst -C %{buildroot}/
rm -f %{buildroot}/.BUILDINFO %{buildroot}/.MTREE %{buildroot}/.PKGINFO %{buildroot}/etc/wireplumber

cp %{_sourcedir}/pipewire-pulse.conf %{buildroot}%{_prefix}/share/pipewire/hardware-profiles/valve-jupiter/pipewire.conf.d/

%files
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/amss.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/board-2.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/board.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/boardg.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/m3.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/regdb.bin.xz
%{_prefix}/lib/firmware/cirrus/cs35l41-dsp1-spk-cali.bin.xz
%{_prefix}/lib/firmware/cirrus/cs35l41-dsp1-spk-cali.wmfw.xz
%{_prefix}/lib/firmware/amd/sof/sof-vangogh-data.bin
%{_prefix}/lib/firmware/amd/sof/sof-vangogh.ldc
%{_prefix}/lib/firmware/amd/sof-tplg/sof-vangogh-nau8821-max.tplg
%{_prefix}/lib/firmware/amd/sof/sof-logger
%{_prefix}/lib/firmware/amd/sof/sof-vangogh-code.bin
%{_prefix}/lib/lv2/valve_binaural.lv2/manifest.ttl
%{_prefix}/lib/lv2/valve_binaural.lv2/valve_binaural.so
%{_prefix}/lib/lv2/valve_binaural.lv2/valve_binaural.ttl
%{_prefix}/lib/lv2/valve_deck_microphone.dsp/manifest.ttl
%{_prefix}/lib/lv2/valve_deck_microphone.dsp/valve_deck_microphone.so
%{_prefix}/lib/lv2/valve_deck_microphone.dsp/valve_deck_microphone.ttl
%{_prefix}/lib/lv2/valve_deck_speakers.lv2/manifest.ttl
%{_prefix}/lib/lv2/valve_deck_speakers.lv2/valve_deck_speakers.so
%{_prefix}/lib/lv2/valve_deck_speakers.lv2/valve_deck_speakers.ttl
%{_prefix}/lib/systemd/system/multi-user.target.wants/pipewire-sysconf.service
%{_prefix}/lib/systemd/system/multi-user.target.wants/wireplumber-sysconf.service
%{_prefix}/lib/systemd/system/pipewire-sysconf.service
%{_prefix}/lib/systemd/system/wireplumber-sysconf.service
%{_prefix}/share/alsa/ucm2/conf.d/acp5x/HiFi-upstream.conf
%{_prefix}/share/alsa/ucm2/conf.d/acp5x/HiFi.conf
%{_prefix}/share/alsa/ucm2/conf.d/acp5x/acp5x.conf
%{_prefix}/share/alsa/ucm2/conf.d/sof-nau8821-max/HiFi.conf
%{_prefix}/share/alsa/ucm2/conf.d/sof-nau8821-max/sof-nau8821-max.conf
%{_prefix}/share/pipewire/hardware-profiles/default
%{_prefix}/share/pipewire/hardware-profiles/pipewire-hwconfig
%{_prefix}/share/pipewire/hardware-profiles/valve-galileo/pipewire.conf.d/filter-chain-sink.conf
%{_prefix}/share/pipewire/hardware-profiles/valve-galileo/pipewire.conf.d/filter-chain.conf
%{_prefix}/share/pipewire/hardware-profiles/valve-galileo/pipewire.conf.d/virtual-sink.conf
%{_prefix}/share/pipewire/hardware-profiles/valve-galileo/pipewire.conf.d/virtual-source.conf
%{_prefix}/share/pipewire/hardware-profiles/valve-jupiter/pipewire.conf.d/filter-chain.conf
%{_prefix}/share/pipewire/hardware-profiles/valve-jupiter/pipewire.conf.d/pipewire-pulse.conf
%{_prefix}/share/pipewire/hardware-profiles/valve-jupiter/pipewire.conf.d/virtual-source.conf
%{_prefix}/share/wireplumber/hardware-profiles/default
%{_prefix}/share/wireplumber/hardware-profiles/valve-galileo/wireplumber.conf.d/alsa-card0.conf
%{_prefix}/share/wireplumber/hardware-profiles/valve-galileo/wireplumber.conf.d/alsa-card1.conf
%{_prefix}/share/wireplumber/hardware-profiles/valve-galileo/wireplumber.conf.d/alsa-ps-controller.conf
%{_prefix}/share/wireplumber/hardware-profiles/valve-galileo/wireplumber.conf.d/bluez.conf
%{_prefix}/share/wireplumber/hardware-profiles/valve-galileo/wireplumber.conf.d/component-rules.conf
%{_prefix}/share/wireplumber/hardware-profiles/valve-jupiter/wireplumber.conf.d/alsa-card0.conf
%{_prefix}/share/wireplumber/hardware-profiles/valve-jupiter/wireplumber.conf.d/alsa-card1.conf
%{_prefix}/share/wireplumber/hardware-profiles/valve-jupiter/wireplumber.conf.d/alsa-ps-controller.conf
%{_prefix}/share/wireplumber/hardware-profiles/valve-jupiter/wireplumber.conf.d/bluez.conf
%{_prefix}/share/wireplumber/hardware-profiles/valve-jupiter/wireplumber.conf.d/component-rules.conf
%{_prefix}/share/wireplumber/hardware-profiles/wireplumber-hwconfig

%changelog
* Wed Feb 05 2025 Luke Short <ekultails@gmail.com> 20240917.1-3
- Add Steam Deck OLED specific configuration with a faster polling rate to fix crackling audio issues

* Wed Feb 05 2025 Luke Short <ekultails@gmail.com> 20240917.1-2
- Conflict with Nobara packages

* Thu Nov 21 2024 Luke Short <ekultails@gmail.com> 20240917.1-1
- Update to SteamOS 3.6.20 packages

* Fri Sep 20 2024 Luke Short <ekultails@gmail.com> 20231113.1-5
- Disable debug package to fix builds on Fedora 41

* Fri Sep 13 2024 Luke Short <ekultails@gmail.com> 20231113.1-4
- Revert Steam Deck OLED Wi-Fi firmware support now that it is upstream in linux-firmware-20240909

* Tue Jul 23 2024 Luke Short <ekultails@gmail.com> 20231113.1-3
- Fix Steam Deck OLED Wi-Fi firmware support

* Tue Jul 23 2024 Luke Short <ekultails@gmail.com> 20231113.1-2
- Add Steam Deck OLED audio firmware and configuration files

* Wed May 01 2024 Luke Short <ekultails@gmail.com> 20231113.1-1
- Initial RPM spec created
