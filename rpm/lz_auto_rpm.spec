%define __os_install_post /usr/lib/rpm/brp-compress
%define __key_version 0.0.1

Name: lz_auto_rpm
Version: 0.0.1
Release: 1

Group: Productivity/Networking/API
Summary: Auto Rpm
License: Commercial

BuildArch: noarch

AutoReqProv:no

Requires: rpm >= 4.0.0

%description
Generating specific directory structure for rpm-create

%prep
cd $OLDPWD/.. && make dist

%install
cp -rf $OLDPWD/../_dist/* .%{_prefix}
mkdir -p .%{_prefix}/../../../usr/local/bin
cp .%{_prefix}/lz_rpm_init .%{_prefix}/../../../usr/local/bin/
rm -f .%{_prefix}/lz_rpm_init

%files
%defattr(777,admin,admin)
%{_prefix}
%{_prefix}/../../../usr/local/bin/lz_rpm_init

%post

%changelog
