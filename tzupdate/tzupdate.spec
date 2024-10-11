Name: tzupdate
Version: 3.1.0
Release: 1%{?dist}
Summary: A command to automatically set the timezone based on GeoIP information
License: MIT
URL: https://github.com/cdown/tzupdate
Source0: https://github.com/cdown/tzupdate/archive/refs/tags/%{version}.tar.gz
BuildRequires: cargo rust

# Disable the unused debug package.
%global debug_package %{nil}

%description
%{summary}.

%prep
%setup -q -c

%build
cd tzupdate-%{version}
cargo build --release

%install
mkdir -p %{buildroot}/usr/bin
cp tzupdate-%{version}/target/release/tzupdate %{buildroot}/usr/bin/

%files
/usr/bin/tzupdate

%changelog
* Fri Oct 11 2024 Luke Short <ekultails@gmail.com> 3.1.0-1
- Initial RPM spec created
