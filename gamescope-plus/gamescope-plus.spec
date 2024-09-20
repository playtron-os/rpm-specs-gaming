%global libliftoff_minver 0.4.1
%global reshade_commit 4245743a8c41abbe3dc73980c1810fe449359bf1
%global reshade_shortcommit %(c=%{reshade_commit}; echo ${c:0:7})

Name:           gamescope-plus
Version:        3.12.7
Release:        %autorelease
Summary:        Micro-compositor for video games on Wayland
Provides:       gamescope

License:        BSD
URL:            https://github.com/alkazar/gamescope-plus
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Create stb.pc to satisfy dependency('stb')
Source1:        stb.pc
Source2:        https://github.com/Joshua-Ashton/reshade/archive/%{reshade_commit}/reshade-%{reshade_shortcommit}.tar.gz

Patch01:        0001-cstdint.patch

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  libXmu-devel
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  (pkgconfig(wlroots) >= 0.16.0 with pkgconfig(wlroots) < 0.17)
BuildRequires:  (pkgconfig(libliftoff) >= 0.4.1 with pkgconfig(libliftoff) < 0.5)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  spirv-headers-devel
BuildRequires:  stb_image-devel
# Header-only library: -static is for tracking per guidelines
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-devel
BuildRequires:  stb_image_resize-static
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_write-static
BuildRequires:  vkroots-devel
BuildRequires:  /usr/bin/glslangValidator

# libliftoff hasn't bumped soname, but API/ABI has changed for 0.2.0 release
Requires:       libliftoff%{?_isa} >= %{libliftoff_minver}
Requires:       xorg-x11-server-Xwayland
Recommends:     mesa-dri-drivers
Recommends:     mesa-vulkan-drivers

# Disable the unused debug package.
%global debug_package %{nil}

%description
%{name} is the micro-compositor optimized for running video games on Wayland.

%prep
%autosetup -p1 -a2 -N
# Install stub pkgconfig file
mkdir -p pkgconfig
cp %{SOURCE1} pkgconfig/stb.pc

# Replace spirv-headers include with the system directory
sed -i 's^../thirdparty/SPIRV-Headers/include/spirv/^/usr/include/spirv/^' src/meson.build

# Push in reshade from sources instead of submodule
rm -rf src/reshade && mv reshade-%{reshade_commit} src/reshade

%autopatch -p1

%build
export PKG_CONFIG_PATH=pkgconfig
%meson -Dpipewire=enabled -Denable_openvr_support=false -Dforce_fallback_for=[]
%meson_build

%install
%meson_install

%post
# Give the gamescope process higher priority so it can run smoother
setcap 'cap_sys_nice=eip' /usr/bin/gamescope

%files
%license LICENSE
%doc README.md
%{_bindir}/gamescope
%{_libdir}/libVkLayer_FROG_gamescope_wsi_*.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_FROG_gamescope_wsi.*.json


%changelog
%autochangelog

