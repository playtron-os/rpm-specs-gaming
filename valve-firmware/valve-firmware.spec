Name: valve-firmware
# There are two source packages. Set the RPM version to mirror whichever source is newer.
Version: 20231113.1
Release: 1%{?dist}
Summary: Linux firmware files for the Steam Deck OLED
License: GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL: https://steamdeck-packages.steamos.cloud/archlinux-mirror/jupiter-main/os/x86_64/
Source0: https://steamdeck-packages.steamos.cloud/archlinux-mirror/jupiter-main/os/x86_64/linux-firmware-neptune-jupiter.%{version}-1-any.pkg.tar.zst
Source1: https://steamdeck-packages.steamos.cloud/archlinux-mirror/jupiter-main/os/x86_64/linux-firmware-neptune-20230121.1f01c88-1-any.pkg.tar.zst
BuildArch: noarch
BuildRequires: xz zstd

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
xz --check=crc32 usr/lib/firmware/ath11k/QCA206X/hw2.1/*
mv usr/lib/firmware/ath11k/QCA206X %{buildroot}/%{_prefix}/lib/firmware/ath11k/

xz --check=crc32 usr/lib/firmware/cs35l41-dsp1-spk-{cali.bin,cali.wmfw}
mv usr/lib/firmware/cs35l41-dsp1-spk-{cali.bin,cali.wmfw}.xz %{buildroot}/%{_prefix}/lib/firmware/cirrus/

%files
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/amss.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/board-2.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/board.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/boardg.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/m3.bin.xz
%{_prefix}/lib/firmware/ath11k/QCA206X/hw2.1/regdb.bin.xz
%{_prefix}/lib/firmware/cirrus/cs35l41-dsp1-spk-cali.bin.xz
%{_prefix}/lib/firmware/cirrus/cs35l41-dsp1-spk-cali.wmfw.xz

%changelog
* Wed May 01 2024 Luke Short <ekultails@gmail.com> 20231113.1-1
- Initial RPM spec created
