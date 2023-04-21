srpm:
  dnf -y install mock rpm-build rpmdevtools
  mock --init
  spectool -g -R mesa.spec
  rpmbuild -bs mesa.spec
