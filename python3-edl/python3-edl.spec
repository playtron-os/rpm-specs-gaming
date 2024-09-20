Name: python3-edl
Version: 3.52.1+243
%define commit 8f606dd1fe968371efe3ffdc2d1c7ebc7a888327
Release: 2%{?dist}
Summary: Qualcomm Arm SoC Emergency Download (EDL) client and diagnostic tools
License: GPL-3.0-only
URL: https://github.com/bkerler/edl
Source0: https://github.com/bkerler/edl/archive/%{commit}.tar.gz
BuildRequires: git python3-build python3-devel python3-installer python3-pip python3-setuptools python3-wheel xz-devel
# Possibly missing dependencies: python3-exscript, python3-keystone (optional), and python3-pycryptodome
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=edl-git
Requires: adb fastboot python3 python3-capstone python3-colorama python3-docopt python3-passlib python3-pycryptodomex python3-lxml python3-pyusb python3-pyserial python3-requests python3-wheel xz
Recommends: python3-qrcode
Suggests: dtc
# edl does not work at all with ModemManager installed.
Conflicts: ModemManager

# Disable the unused debug package.
%global debug_package %{nil}

%description
%{summary}.

%prep
# Use git instead of the source code to get the submodules.
rm -r -f edl
git clone https://github.com/bkerler/edl.git
cd edl
git checkout %{commit}
git submodule update --init --recursive

%build
cd edl
/usr/bin/python3 -m build --wheel

%install
mkdir -p %{buildroot}/etc/udev/rules.d/
mkdir -p %{buildroot}/usr/share/licenses/python3-edl/

cd %{_builddir}/edl/
/usr/bin/python3 -m installer --destdir="%{buildroot}" dist/*.whl
rm -r -f \
  %{buildroot}/usr/LICENSE \
  %{buildroot}/usr/README.md \
  %{buildroot}/usr/lib/python3.*/site-packages/Loaders/.git \
  %{buildroot}/usr/lib/python3.*/site-packages/Loaders/.gitignore

cp -Rv ./Drivers/*.rules %{buildroot}/etc/udev/rules.d/
cp ./LICENSE %{buildroot}/usr/share/licenses/python3-edl/

%files
/etc/udev/rules.d/50-android.rules
/etc/udev/rules.d/51-edl.rules
/usr/bin/beagle_to_loader
/usr/bin/boottodwnload
/usr/bin/edl
/usr/bin/enableadb
/usr/bin/fhloaderparse
/usr/bin/qc_diag.py
/usr/bin/sierrakeygen.py
/usr/lib/python3.*/site-packages/edlclient/*
/usr/lib/python3.*/site-packages/edlclient-*.dist-info/*
/usr/lib/python3.*/site-packages/Loaders/*
/usr/share/licenses/python3-edl/LICENSE

%changelog
* Fri Sep 20 2024 Luke Short <ekultails@gmail.com> 3.52.1+243-2
- Disable debug package to fix builds on Fedora 41

* Tue Mar 05 2024 Luke Short <ekultails@gmail.com> 3.52.1+243-1
- Initial RPM spec created
