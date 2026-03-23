%global pdfium_version 7733

Name:           libpdfium
Version:        %{pdfium_version}
Release:        1
Summary:        Open-source PDF rendering library from the Chromium project

License:        BSD-3-Clause
URL:            https://pdfium.googlesource.com/pdfium/

Patch0: add-fpdf-implementation-to-export-guard.patch

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
BuildRequires:  xz

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

%patch 0 -p1

# Configure GN args (Release build, minimal features for smaller lib)
mkdir -p out/Release
cat > out/Release/args.gn <<ARGS
use_remoteexec = false
is_debug = false
is_component_build = false
clang_use_chrome_plugins = false
pdf_enable_v8 = false
pdf_enable_xfa = false
pdf_is_standalone = true
pdf_is_complete_lib = true
use_custom_libcxx = false
ARGS


%build
# Help linker find libgcc_s
export LIBRARY_PATH="$(dirname $(gcc -print-file-name=libgcc_s.so)):${LIBRARY_PATH:-}"

# Generate Ninja build files and build the library
cd %{_builddir}/pdfium_repo/pdfium
gn gen out/Release
ninja -C out/Release pdfium

# Create .so file
cd out/Release
../../third_party/llvm-build/Release+Asserts/bin/clang++ \
  -shared -fuse-ld=lld \
  -o libpdfium.so \
  -Wl,--whole-archive obj/libpdfium.a -Wl,--no-whole-archive \
  -lm -lpthread -ldl


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


%package devel
Summary:        Development files for PDFium
Requires:       %{name} = %{version}-%{release}

%description devel
Header files for developing applications that use PDFium.

%files devel
%{_libdir}/pkgconfig/pdfium.pc
%{_includedir}/pdfium/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
* Mon Mar 23 2026 Alesh Slovak <alesh@playtron.one> 7733-1
- Initial RPM spec created
