#!/bin/bash

dnf install -y binutils-gold createrepo_c git kernel-devel openssl rpm-build rpm-sign wget

#FIXME: This hack installs the latest kernel and then downgrades to the
# Playtron OS kernel. This is the easiest way to install the correct
# kernel version.
dnf copr enable -y playtron/gaming
dnf install -y kernel-devel kernel-headers
dnf downgrade -y kernel-devel kernel-headers

#git clone https://github.com/NVIDIA/yum-packaging-precompiled-kmod.git
git clone --branch custom-kernel-name https://github.com/LukeShortCloud/yum-packaging-precompiled-kmod.git
cd yum-packaging-precompiled-kmod
mkdir -p ~/precompiled-kmod/SPECS/

# Workaround issues in the build script by manually generating some files.
## Copy and rename the kmod-nvidia.spec file. The old 'yum-kmond-nvidia.spec' is unused.
cp ./dnf-kmod-nvidia.spec ~/precompiled-kmod/SPECS/kmod-nvidia.spec
## Download 'primary.xml.gz' repository data.
baseURL="http://developer.download.nvidia.com/compute/cuda/repos"
### "fedora40" is not available yet.
distro="fedora39"
arch="x86_64"
curl "http://developer.download.nvidia.com/compute/cuda/repos/${distro}/${arch}/$(curl -sL http://developer.download.nvidia.com/compute/cuda/repos/${distro}/${arch}/repodata/repomd.xml | grep primary.xml | cut -d\" -f2)" --output primary.xml.gz
gunzip primary.xml.gz
# Find all available versions of the NVIDIA driver that can be re-packaged.
grep -o -P "5[0-9]+\.[0-9]+\.[0-9]+" primary.xml | sort | uniq
# Download and use a version from the NVIDIA driver archive:
# https://www.nvidia.com/en-us/drivers/unix/linux-amd64-display-archive/

# Download this dependency to help with creating a modular repository.
wget https://raw.githubusercontent.com/NVIDIA/cuda-repo-management/main/genmodules.py

# NVIDIA packages are not available for Fedora 40 yet.
# Instead, repackage Fedora 39 packages since they are forward compatible.
# The NVIDIA repository will be created at: ~/precompiled-kmod/repo/
bash build.sh ~/Downloads/NVIDIA-Linux-x86_64-560.35.03.run fedora39
