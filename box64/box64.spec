# Tests are disabled as they require x86_64 libraries to run
%bcond tests 0

%global forgeurl https://github.com/ptitSeb/box64

%global common_description %{expand:
Box64 lets you run x86_64 Linux programs (such as games) on non-x86_64 Linux
systems, like ARM (host system needs to be 64-bit little-endian).}

%define hash 6af34e0c4394991d58ac782ab020aad5ad3fa2a3

Name:           box64
Version:        0.3.8+7298
Release:        %autorelease
Summary:        Linux userspace x86_64 emulator with a twist, targeted at ARM64

License:        MIT
URL:            https://box86.org
Source:         %{forgeurl}/archive/%{hash}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  systemd-rpm-macros

# box64 only supports these architectures
ExclusiveArch:  aarch64 riscv64 ppc64le %{x86_64}

Requires:       %{name}-data = %{version}-%{release}
# These should not be pulled in on x86_64 as they can cause a loop and prevent
# any binary from successfully executing (#2344770)
%ifnarch %{x86_64}
Recommends:     %{name}-binfmts = %{version}-%{release}
%endif
%ifarch aarch64
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%endif

%description    %{common_description}

%package        data
Summary:        Common files for %{name}
BuildArch:      noarch

%description    data %{common_description}

This package provides common data files for box64.

%ifnarch %{x86_64}
%package        binfmts
Summary:        binfmt_misc handler configurations for box64

%description    binfmts %{common_description}

This package provides binfmt_misc handler configurations to use box64 to
execute x86_64 binaries.
%endif

%ifarch aarch64
%package        adlink
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    adlink %{common_description}

This package contains a version of box64 targeting ADLink AmpereAltra systems.

%package        asahi
Summary:        Apple Silicon version of box64

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    asahi %{common_description}

This package contains a version of box64 targeting Apple Silicon systems using
a 16k page size.

%package        lx2160a
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    lx2160a %{common_description}

This package contains a version of box64 targeting NXP LX2160A systems.

%package        odroidn2
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    odroidn2 %{common_description}

This package contains a version of box64 targeting ODROID-N2/N2+ systems.

%package        phytium
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    phytium %{common_description}

This package contains a version of box64 targeting Phytium (D2000 or FT2000/4)
systems.

%package        rk3326
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    rk3326 %{common_description}

This package contains a version of box64 targeting Rockchip RK3326 systems.

%package        rk3399
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    rk3399 %{common_description}

This package contains a version of box64 targeting Rockchip RK3399 systems.

%package        rk3588
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    rk3588 %{common_description}

This package contains a version of box64 targeting Rockchip RK3588 / RK3588S
systems.

%package        rpi3
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    rpi3 %{common_description}

This package contains a version of box64 targeting Raspberry Pi 3 systems.

%package        rpi4
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    rpi4 %{common_description}

This package contains a version of box64 targeting Raspberry Pi 4 systems.

%package        rpi5
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    rpi5 %{common_description}

This package contains a version of box64 targeting Raspberry Pi 5 systems.

%package        sd845
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    sd845 %{common_description}

This package contains a version of box64 targeting Qualcomm Snapdragon 845
systems.

%package        sd865
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    sd865 %{common_description}

This package contains a version of box64 targeting Qualcomm Snapdragon 865
systems.

%package        sd888
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    sd888 %{common_description}

This package contains a version of box64 targeting Qualcomm Snapdragon 888
systems.

%package        sd8g2
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    sd8g2 %{common_description}

This package contains a version of box64 targeting Qualcomm Snapdragon 8 Gen 2
systems.

%package        sdoryon1
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    sdoryon1 %{common_description}

This package contains a version of box64 targeting Qualcomm Snapdragon Oryon 1
(X1E80100/X1E78100) systems.

%package        tegrat194
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    tegrat194 %{common_description}

This package contains a version of box64 targeting Nvidia Tegra Xavier systems.

%package        tegrat234
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    tegrat234 %{common_description}

This package contains a version of box64 targeting Nvidia Tegra Orion systems.

%package        tegrax1
Summary:        %{summary}

Requires:       %{name}-data = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description    tegrax1 %{common_description}

This package contains a version of box64 targeting Nvidia Tegra X1 systems.
%endif

%prep
%autosetup -p1 -n box64-%{hash}

# Remove prebuilt libraries
rm -r x64lib

# Fix encoding
sed -i 's/\r$//' docs/*.md

# Fix install paths
sed -i 's:/etc/binfmt.d:%{_binfmtdir}:g' CMakeLists.txt

%build
%global common_flags -DNOGIT=ON -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBOX32=ON -DBOX32_BINFMT=ON
%ifarch aarch64
%global common_flags -DARM_DYNAREC=ON %{common_flags}

# ADLink AmpereAltra
%cmake %{common_flags} -DADLINK=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.adlink
rm -r %{__cmake_builddir}

# Apple Silicon
%cmake %{common_flags} -DM1=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.asahi
rm -r %{__cmake_builddir}

# NXP LX2160A
%cmake %{common_flags} -DLX2160A=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.lx2160a
rm -r %{__cmake_builddir}

# ODROID-N2/N2+
%cmake %{common_flags} -DODROIDN2=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.odroidn2
rm -r %{__cmake_builddir}

# Phytium (D2000 or FT2000/4)
%cmake %{common_flags} -DPHYTIUM=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.phytium
rm -r %{__cmake_builddir}

# Rockchip RK3326
%cmake %{common_flags} -DRK3326=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.rk3326
rm -r %{__cmake_builddir}

# Rockchip RK3399
%cmake %{common_flags} -DRK3399=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.rk3399
rm -r %{__cmake_builddir}

# Rockchip RK3588/RK3588S
%cmake %{common_flags} -DRK3588=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.rk3588
rm -r %{__cmake_builddir}

# Raspberry PI 3
%cmake %{common_flags} -DRPI3ARM64=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.rpi3
rm -r %{__cmake_builddir}

# Raspberry PI 4
%cmake %{common_flags} -DRPI4ARM64=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.rpi4
rm -r %{__cmake_builddir}

# Raspberry PI 5
%cmake %{common_flags} -DRPI5ARM64=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.rpi5
rm -r %{__cmake_builddir}

# Qualcomm Snapdragon 845
%cmake %{common_flags} -DSD845=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.sd845
rm -r %{__cmake_builddir}

# Qualcomm Snapdragon 865
%cmake %{common_flags} -DSD865=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.sd865
rm -r %{__cmake_builddir}

# Qualcomm Snapdragon 888
%cmake %{common_flags} -DSD888=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.sd888
rm -r %{__cmake_builddir}

# Qualcomm Snapdragon 8 Gen 2
%cmake %{common_flags} -DSD8G2=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.sd8g2
rm -r %{__cmake_builddir}

# Qualcomm Snapdragon Oryon 1 (X1E80100/X1E78100)
%cmake %{common_flags} -DSDORYON1=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.sdoryon1
rm -r %{__cmake_builddir}

# Nvidia Tegra Xavier
%cmake %{common_flags} -DTEGRA_T194=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.tegrat194
rm -r %{__cmake_builddir}

# Nvidia Tegra Orion
%cmake %{common_flags} -DTEGRA_T234=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.tegrat234
rm -r %{__cmake_builddir}

# Nvidia Tegra X1
%cmake %{common_flags} -DTEGRAX1=ON
%cmake_build
cp -p %{__cmake_builddir}/%{name} %{name}.tegrax1
rm -r %{__cmake_builddir}
%endif

%cmake %{common_flags} -DNO_LIB_INSTALL=ON \
%ifarch aarch64
  -DARM64=ON
%endif
%ifarch riscv64
  -DRV64=ON
%endif
%ifarch ppc64le
  -DPPC64LE=ON
%endif
%ifarch %{x86_64}
  -DLD80BITS=ON \
  -DNOALIGN=ON
%endif
%cmake_build

# Build manpage
pod2man --stderr docs/%{name}.pod > docs/%{name}.1

%install
%ifarch %{x86_64}
# Install manually as cmake_install doesn't seem to work on x86_64
install -Dpm0755 -t %{buildroot}%{_bindir} %{__cmake_builddir}/%{name}
install -Ddpm0755 %{buildroot}%{_binfmtdir}
sed 's:${CMAKE_INSTALL_PREFIX}/bin/${BOX64}:%{_bindir}/%{name}:' \
  < system/box32.conf.cmake > system/box32.conf
sed 's:${CMAKE_INSTALL_PREFIX}/bin/${BOX64}:%{_bindir}/%{name}:' \
  < system/box64.conf.cmake > system/box64.conf
install -Dpm0644 -t %{buildroot}%{_sysconfdir} system/box64.box64rc
%else
%cmake_install
%endif

# Install manpage
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/%{name}.1

%ifarch aarch64
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}.aarch64
touch %{buildroot}%{_bindir}/%{name}
chmod +x %{buildroot}%{_bindir}/%{name}
install -Dpm0755 -t %{buildroot}%{_bindir} \
  %{name}.adlink \
  %{name}.asahi \
  %{name}.lx2160a \
  %{name}.odroidn2 \
  %{name}.phytium \
  %{name}.rk3326 \
  %{name}.rk3399 \
  %{name}.rk3588 \
  %{name}.rpi3 \
  %{name}.rpi4 \
  %{name}.rpi5 \
  %{name}.sd845 \
  %{name}.sd865 \
  %{name}.sd888 \
  %{name}.sd8g2 \
  %{name}.sdoryon1 \
  %{name}.tegrat194 \
  %{name}.tegrat234 \
  %{name}.tegrax1

%post
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.aarch64 20

%postun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.aarch64
fi

%post adlink
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.adlink 10

%postun adlink
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.adlink
fi

%post asahi
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.asahi 10

%postun asahi
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.asahi
fi

%post lx2160a
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.lx2160a 10

%postun lx2160a
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.lx2160a
fi

%post odroidn2
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.odroidn2 10

%postun odroidn2
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.odroidn2
fi

%post phytium
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.phytium 10

%postun phytium
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.phytium
fi

%post rk3326
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.rk3326 10

%postun rk3326
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.rk3326
fi

%post rk3399
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.rk3399 10

%postun rk3399
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.rk3399
fi

%post rk3588
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.rk3588 10

%postun rk3588
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.rk3588
fi

%post rpi3
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.rpi3 10

%postun rpi3
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.rpi3
fi

%post rpi4
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.rpi4 10

%postun rpi4
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.rpi4
fi

%post rpi5
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.rpi5 10

%postun rpi5
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.rpi5
fi

%post sd845
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.sd845 10

%postun sd845
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.sd845
fi

%post sd865
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.sd865 10

%postun sd865
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.sd865
fi

%post sd888
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.sd888 10

%postun sd888
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.sd888
fi

%post sd8g2
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.sd8g2 10

%postun sd8g2
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.sd8g2
fi

%post sdoryon1
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.sdoryon1 10

%postun sdoryon1
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.sdoryon1
fi

%post tegrat194
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.tegrat194 10

%postun tegrat194
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.tegrat194
fi

%post tegrat234
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.tegrat234 10

%postun tegrat234
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.tegrat234
fi

%post tegrax1
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.tegrax1 10

%postun tegrax1
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.tegrax1
fi
%endif

%if %{with tests}
%check
%ctest
%endif

%files
%ifarch aarch64
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.aarch64
%else
%{_bindir}/%{name}
%endif

%ifarch aarch64
%files adlink
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.adlink

%files asahi
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.asahi

%files lx2160a
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.lx2160a

%files odroidn2
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.odroidn2

%files phytium
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.phytium

%files rk3326
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.rk3326

%files rk3399
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.rk3399

%files rk3588
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.rk3588

%files rpi3
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.rpi3

%files rpi4
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.rpi4

%files rpi5
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.rpi5

%files sd845
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.sd845

%files sd865
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.sd865

%files sd888
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.sd888

%files sd8g2
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.sd8g2

%files sdoryon1
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.sdoryon1

%files tegrat194
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.tegrat194

%files tegrat234
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.tegrat234

%files tegrax1
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.tegrax1
%endif

%files data
%license LICENSE
%doc README.md
%doc %lang(cn) README_CN.md
%doc %lang(uk) README_UK.md
%doc docs/*.md docs/img
%{_mandir}/man1/box64.1*
%config(noreplace) %{_sysconfdir}/box64.box64rc

%ifnarch %{x86_64}
%files binfmts
%{_binfmtdir}/box32.conf
%{_binfmtdir}/box64.conf
%endif

%changelog
%autochangelog
