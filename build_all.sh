#!/bin/bash

# Enable shell debugging.
set -x

# Install RPM build dependencies
dnf install -y rpm-build rpmdevtools
# Create the necessary RPM build directories
mkdir -p ~/rpmbuild/SOURCES/
# Install the DNF build dependencies plugin
dnf -y install 'dnf-command(builddep)'
# Build RPMs
cd ~/
## Each RPM spec is stored in its own directory in this repository.
for pkg in $(ls -d -1 */ | cut -d\/ -f1)
    do cd ${pkg}
    # Copy internal source files.
    cp ./* ~/rpmbuild/SOURCES/
    # Download external source files.
    spectool -g -R *.spec
    # Build the source RPM.
    rpmbuild -bs *.spec
    # Install the required build dependencies.
    dnf builddep -y *.spec
    # Build the binary RPM.
    rpmbuild -bb *.spec
    cd ..
done
# Install RPMs
dnf -y install ~/rpmbuild/RPMS/*/*.rpm
