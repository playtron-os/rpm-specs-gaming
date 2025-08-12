ARG FEDORA_VERSION="41"
FROM docker.io/library/fedora:${FEDORA_VERSION}

RUN dnf install -y make sudo copr-cli rpm-build rpmdevtools 'dnf-command(builddep)'
