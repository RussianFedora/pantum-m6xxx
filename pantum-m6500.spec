%global debug_package %{nil}
%global tgzdir ADF_LinuxInstaller

Name: pantum-m6xxx
Version: 1.4.0
Release: 1%{?dist}
Summary: Pantum M6500 Series drivers

Source0: https://www.prink.it/images/FILES/IT/driver/Pantum-M6200-M6500-M6550-M6600-MS6000-Series-LINUX-Driver-V1-4-0-tar.gz

URL: http://pantum.com/
License: Proprietary

%package cups
Summary: Pantum M6500 Series CUPS drivers

%package sane
Summary: Pantum M6500 Series Sane drivers

%description
%{summary}.

%description cups
%{summary}.

%description sane
%{summary}.

%prep
%setup -q -n %{tgzdir}

# Extracting DEB packages:
pushd Resources
    mkdir {driver,sane}
    %ifarch x86_64
        ar p Pantum-M6500-Series-3.0.x86_64.deb data.tar.gz > %{name}-%{version}-driver.tar.gz
        ar p Pantum-M6500-Series-Sane-3.7.x86_64.deb data.tar.gz > %{name}-%{version}-sane.tar.gz
    %else
        ar p Pantum-M6500-Series-3.0.i386.deb data.tar.gz > %{name}-%{version}-driver.tar.gz
        ar p Pantum-M6500-Series-Sane-3.7.i386.deb data.tar.gz > %{name}-%{version}-sane.tar.gz
    %endif
    tar -xf %{name}-%{version}-driver.tar.gz -C driver
    tar -xf %{name}-%{version}-sane.tar.gz -C sane
popd

%build
# Do nothing...

%install
# Installing CUPS driver...
pushd Resources/driver
    mkdir -p %{buildroot}%{_usr}/lib/cups/filter
    install -m 0755 -p usr/lib/cups/filter/ptm6500Filter %{buildroot}%{_usr}/lib/cups/filter
popd

# Installing Sane driver...
pushd Resources/sane
    mkdir -p %{buildroot}%{_sysconfdir}/sane.d/dll.d
    find etc/sane.d -maxdepth 1 -type f -name "*.conf" -exec install -m 0644 -p '{}' %{buildroot}%{_sysconfdir}/sane.d \;
    find etc/sane.d/dll.d -maxdepth 1 -type f -name "*" -exec install -m 0644 -p '{}' %{buildroot}%{_sysconfdir}/sane.d/dll.d \;
popd

%files cups
%doc Resources/locale/en_US.UTF-8/license.txt
%{_usr}/lib/cups/filter/ptm6500Filter

%files sane
%doc Resources/locale/en_US.UTF-8/license.txt
%{_sysconfdir}/sane.d/*.conf
%{_sysconfdir}/sane.d/dll.d/*

%changelog
* Sun Feb 11 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4.0-1
- Use alternatives to provide /usr/bin/sublime_text binary.
