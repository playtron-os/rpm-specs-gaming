%global pdfium_version 7733

Name:           libpdfium
Version:        %{pdfium_version}
Release:        1
Summary:        Open-source PDF rendering library from the Chromium project

License:        BSD-3-Clause
URL:            https://pdfium.googlesource.com/pdfium/

# depot_tools provides gclient
BuildRequires:  git
BuildRequires:  python3
BuildRequires:  which
BuildRequires:  clang
BuildRequires:  libgcc
BuildRequires:  gn
BuildRequires:  ninja-build
BuildRequires:  fontconfig-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  xz

Requires:       pkgconfig(nspr)
Requires:       pkgconfig(nss)

ExclusiveArch:  x86_64 aarch64

%description
PDFium is an open-source library for PDF manipulation and rendering, developed
as part of the Chromium project. It is used by Google Chrome, Foxit Reader,
and many other applications.

This package provides the shared library and headers for embedding PDFium
in your own projects. Built from source without JavaScript/V8 or XFA support
for a smaller, more portable library.


%prep
cd %{_builddir}

# Fetch depot_tools (provides gclient)
git clone --depth 1 https://chromium.googlesource.com/chromium/tools/depot_tools.git depot_tools
export PATH="%{_builddir}/depot_tools:$PATH"

# Configure and fetch PDFium source
mkdir -p pdfium_repo && cd pdfium_repo
gclient config --unmanaged https://pdfium.googlesource.com/pdfium.git
gclient sync -r "origin/chromium/%{pdfium_version}" --no-history --shallow -D

cd pdfium

# Configure GN args (Release build, minimal features for smaller lib)
mkdir -p out/Release
cat > out/Release/args.gn <<ARGS
is_debug = false
is_component_build = true
use_sysroot = false
use_lld = false
clang_use_chrome_plugins = false
pdf_enable_v8 = false
pdf_enable_xfa = false
pdf_use_skia = true
pdf_is_standalone = false
ARGS


%build
# Help linker find libgcc_s
export LIBRARY_PATH="$(dirname $(gcc -print-file-name=libgcc_s.so)):${LIBRARY_PATH:-}"

# Generate Ninja build files and build the library
cd %{_builddir}/pdfium_repo/pdfium
gn gen out/Release
ninja -C out/Release pdfium


%install
cd %{_builddir}/pdfium_repo/pdfium

# Install library
install -Dpm 755 out/Release/libpdfium.so "%{buildroot}%{_libdir}/libpdfium.so"

# Install headers
install -d %{buildroot}%{_includedir}/pdfium
cp -a public/. %{buildroot}%{_includedir}/pdfium/

# Install pkgconfig file
install -d %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/pdfium.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: pdfium
Description: PDF manipulation and rendering library
Version: %{version}
Libs: -L\${libdir} -lpdfium
Cflags: -I\${includedir}/pdfium
EOF


%files
%{_libdir}/libpdfium.so
%{_libdir}/pkgconfig/pdfium.pc
%{_includedir}/pdfium/


%changelog
* Fri Mar 13 2026 Alesh Slovak <alesh@playtron.one> 7733-1
- Initial RPM spec created