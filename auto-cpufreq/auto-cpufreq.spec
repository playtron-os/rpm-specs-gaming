Name: auto-cpufreq
Version: 2.2.0
Release: 1
Summary: Automatic CPU speed & power optimizer for Linux
License: LGPL-3.0-or-later
URL: https://github.com/AdnanHodzic/auto-cpufreq
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz
Source1: auto-cpufreq.service
BuildRequires: cairo-devel cairo-gobject-devel dmidecode gcc gobject-introspection-devel git gtk3-devel python-build python-devel python-installer python-poetry-core python-poetry-dynamic-versioning python-setuptools
Requires: dmidecode gobject-introspection gtk3 python python-click python-distro python-gobject python-psutil python-requests

%description
%{summary}.

%prep
# This project only supports being built from the git repository.
# It helps to provide version information.
# https://github.com/AdnanHodzic/auto-cpufreq.git
git clone --branch v%{version} https://github.com/AdnanHodzic/auto-cpufreq.git
cd auto-cpufreq
sed -i 's|usr/local|usr|g' auto_cpufreq/core.py

%build
cd auto-cpufreq
POETRY_DYNAMIC_VERSIONING_BYPASS=1 python3 -m build --wheel --no-isolation

%install
cd %{_builddir}/auto-cpufreq
python3 -m installer --destdir="%{buildroot}" dist/*.whl
install -Dm644 scripts/org.auto-cpufreq.pkexec.policy -t "%{buildroot}/usr/share/polkit-1/actions/"
install -Dm644 images/icon.png "%{buildroot}/usr/share/pixmaps/auto-cpufreq.png"
install -Dm644 images/icon.png -t "%{buildroot}/usr/share/%{name}/"
mkdir -p %{buildroot}/opt/auto-cpufreq/
mkdir -p %{buidlroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/share/%{name}/scripts/
mkdir -p %{buildroot}/usr/share/doc/%{name}/
mkdir -p %{buildroot}/usr/share/licenses/%{name}/
install -Dm644 %{_sourcedir}/auto-cpufreq.service -t "%{buildroot}/usr/lib/systemd/system/"
install -Dm755 scripts/auto-cpufreq-install.sh "%{buildroot}/usr/share/%{name}/scripts/"
install -Dm755 scripts/auto-cpufreq-remove.sh "%{buildroot}/usr/share/%{name}/scripts/"
install -Dm755 scripts/cpufreqctl.sh "%{buildroot}/usr/share/%{name}/scripts/"
install -Dm644 scripts/style.css "%{buildroot}/usr/share/%{name}/scripts/"
install -Dm644 scripts/auto-cpufreq-gtk.desktop -t "%{buildroot}/usr/share/applications/"
install -Dm644 auto-cpufreq.conf-example "%{buildroot}/etc/auto-cpufreq.conf"
install -Dm644 LICENSE "%{buildroot}/usr/share/licenses/%{name}/"
install -Dm644 README.md "%{buildroot}/usr/share/doc/%{name}/"

%files
%config /etc/auto-cpufreq.conf
/usr/lib/python3.*/site-packages/auto_cpufreq*
/usr/lib/systemd/system/auto-cpufreq.service
/usr/bin/auto-cpufreq
/usr/bin/auto-cpufreq-gtk
/usr/share/applications/auto-cpufreq-gtk.desktop
/usr/share/auto-cpufreq/icon.png
/usr/share/auto-cpufreq/scripts/auto-cpufreq-install.sh
/usr/share/auto-cpufreq/scripts/auto-cpufreq-remove.sh
/usr/share/auto-cpufreq/scripts/cpufreqctl.sh
/usr/share/auto-cpufreq/scripts/style.css
/usr/share/doc/auto-cpufreq/README.md
/usr/share/licenses/auto-cpufreq/LICENSE
/usr/share/pixmaps/auto-cpufreq.png
/usr/share/polkit-1/actions/org.auto-cpufreq.pkexec.policy

%changelog
* Mon Apr 01 2024 Luke Short <ekultails@gmail.com> 2.2.0-1
- Initial RPM spec created
