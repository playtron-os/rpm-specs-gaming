Name: hid-msi-claw-dkms
Version: 0.1.0+65
Release: 1%{?dist}
Summary: Kernel module for managing built-in MSI Claw controllers
License: LicenseRef-Unspecified
URL: https://github.com/NeroReflex/hid-msi-claw-dkms
%define ver f63771d21806aefd93364506bb9087f2f4961609
Source0: https://github.com/NeroReflex/hid-msi-claw-dkms/archive/%{ver}.zip
Requires: dkms kernel-devel make gcc

# Disable the unused debug package.
%define debug_package %{nil}

%description
%{summary}.

%prep
%setup -q -c

%install
#install -D -m 0644 Makefile -t "%{buildroot}%{_usrsrc}/hid-msi-claw/"
#install -D -m 0644 dkms.conf -t "%{buildroot}%{_usrsrc}/hid-msi-claw/"
#install -D -m 0644 hid-msi-claw.c -t "%{buildroot}%{_usrsrc}/hid-msi-claw/"
mkdir -p "%{buildroot}%{_usrsrc}/hid-msi-claw-%{version}/"
cp -R -v hid-msi-claw-dkms-%{ver}/* "%{buildroot}%{_usrsrc}/hid-msi-claw-%{version}/"
echo %{version} > "%{buildroot}%{_usrsrc}/hid-msi-claw-%{version}/VERSION"

%post
/usr/bin/env dkms add -m hid-msi-claw -v %{version} --rpm_safe_upgrade
/usr/bin/env dkms build -m hid-msi-claw -v %{version}
/usr/bin/env dkms install -m hid-msi-claw -v %{version} --force

%preun
/usr/bin/env rmmod hid-msi-claw || :
/usr/bin/env dkms remove -m hid-msi-claw -v %{version} --all --rpm_safe_upgrade || :

%postun
rm -r -f -v /var/lib/dkms/hid-msi-claw/%{version}

%files
%{_usrsrc}/hid-msi-claw-%{version}/Makefile
%{_usrsrc}/hid-msi-claw-%{version}/dkms.conf
%{_usrsrc}/hid-msi-claw-%{version}/hid-msi-claw.c
%{_usrsrc}/hid-msi-claw-%{version}/VERSION

%changelog
* Fri Dec 19 2025 Luke Short <ekultails@gmail.com> 0.1.0+65-1
- Initial RPM spec created
