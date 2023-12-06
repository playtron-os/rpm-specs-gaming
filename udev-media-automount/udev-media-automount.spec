Name: udev-media-automount
# GitVersion versioning is to show how many commits have been made to the git repository.
Version: 0.1.0+59
Release: 2%{?dist}
%define ver 66e0dc6f54dbc23451ef6350f7ba437ec7005bd1
Summary: udev rules for automatically mounting filesystems
License: BSD-2-Clause
URL: https://github.com/Ferk/udev-media-automount
Source0: https://github.com/Ferk/udev-media-automount/archive/%{ver}.zip
BuildRequires: make

%description
%{summary}.

%prep
%setup -q -c

%install
mkdir -p \
  %{buildroot}/etc/media-automount.d/ \
  %{buildroot}/usr/lib/udev/rules.d/ \
  %{buildroot}/usr/share/licenses/udev-media-automount/
cd udev-media-automount-%{ver}
cp LICENSE %{buildroot}/usr/share/licenses/udev-media-automount/
make PREFIX=/usr DESTDIR="%{buildroot}" install

%files
%config /etc/media-automount.d/auto
%config /etc/media-automount.d/hfsplus
%config /etc/media-automount.d/ntfs
%config /etc/media-automount.d/vfat
/usr/bin/media-automount
/usr/bin/umount_dmenu
/usr/lib/udev/rules.d/99-media-automount.rules
/usr/lib/systemd/system/media-automount@.service
/usr/share/licenses/udev-media-automount/LICENSE

%post
# Only run udevadm commands if the udevd socket is available.
if [ -S /run/udev/control ]; then
    udevadm control --reload-rules
    udevadm trigger
fi

%postun
if [ -S /run/udev/control ]; then
    udevadm control --reload-rules
fi

%changelog
* Wed Nov 29 2023 Luke Short <ekultails@gmail.com> 0.1.0+59-2
- Do not run udevadm transactions without udevd running
- Use the upstream URL for the source

* Tue Nov 21 2023 Luke Short <ekultails@gmail.com> 0.1.0+59-1
- Initial RPM spec created
