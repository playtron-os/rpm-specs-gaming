#!/bin/bash


#DELME!


# Install generic RPM build dependencies.
dnf install -y fedora-packager fedpkg grubby ncurses-devel pesign rpm-build rpmdevtools 'dnf-command(builddep)'
# Download the kernel package repository. This requires first increasing the buffer size that git uses.
git config --global http.postBuffer 314572800
fedpkg clone -a kernel
cd kernel
# This is the last commit for Linux 6.3.13 before it was rebased to Linux 6.4.4.
git checkout e0412c4338e57bc8271c644b56a0a10f220b015c
# Install build dependencies for the Linux kernel.
dnf builddep -y kernel.spec
# Download the source files.
mkdir -p ~/rpmbuild/SOURCES/
fedpkg sources --outdir ~/rpmbuild/SOURCES/
cp -R -v ~/rpmbuild/SOURCES/* ./
# Copy all local source files.
cp -R -v ./* ~/rpmbuild/SOURCES/
# Customize the kernel to be a Playtron release kernel.
sed -i 's/# define buildid .local/%define buildid .playtron/g' kernel.spec
sed -i s'/%define with_debug     %{?_without_debug:     0} %{?!_without_debug:     1}/%define with_debug 0/'g kernel.spec
sed -i s'/%define with_debuginfo %{?_without_debuginfo: 0} %{?!_without_debuginfo: 1}/%define with_debuginfo 0/'g kernel.spec
sed -i s'/%define with_release   %{?_with_release:      1} %{?!_with_release:      0}/%define with_release 1/'g kernel.spec
sed -i s'/%define with_headers   %{?_without_headers:   0} %{?!_without_headers:   1}/%define with_headers 1/'g kernel.spec
sed -i s'/with_headers 0/with_headers 1/'g kernel.spec
# Fix permissions for files relating to RPM signing.
/usr/libexec/pesign/pesign-authorize
# Build a source RPM.
fedpkg --release f38 srpm
