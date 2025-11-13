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
  %{name}.sd888 \
  %{name}.sd8g2 \
  %{name}.sdoryon1

%post
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}.aarch64 20

%postun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.aarch64
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
%files sd888
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.sd888

%files sd8g2
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.sd8g2

%files sdoryon1
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}.sdoryon1
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
