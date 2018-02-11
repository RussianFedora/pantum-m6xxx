%global debug_package %{nil}
%global tgzdir ADF_LinuxInstaller

Name: pantum-m6xxx
Version: 3.0
Release: 1%{?dist}
Summary: Pantum M6500 Series drivers

Source0: https://www.prink.it/images/FILES/IT/driver/Pantum-M6200-M6500-M6550-M6600-MS6000-Series-LINUX-Driver-V1-4-0-tar.gz

URL: http://pantum.com/
License: Proprietary

%package cups
Summary: Pantum M6500 Series CUPS drivers

%description
%{summary}.

%description cups
%{summary}.

%prep
%setup -q -n %{tgzdir}

# Extracting DEB packages:
pushd Resources
    %ifarch x86_64
        ar p Pantum-M6500-Series-3.0.x86_64.deb data.tar.gz > %{name}-%{version}-driver.tar.gz
        mkdir driver
        tar -xf %{name}-%{version}-driver.tar.gz -C driver
        rm -f *.tar.gz
    %else
        ar p Pantum-M6500-Series-3.0.i386.deb data.tar.gz > %{name}-%{version}-driver.tar.gz
        mkdir driver
        tar -xf %{name}-%{version}-driver.tar.gz -C driver
        rm -f *.tar.gz
    %endif
popd

%build
# Do nothing...

%install
# Installing executables...
pushd Resources/driver
    mkdir -p %{buildroot}%{_usr}/lib/cups/filter
    install -m 0755 -p usr/lib/cups/filter/ptm6500Filter %{buildroot}%{_usr}/lib/cups/filter
popd

%files cups
%doc Resources/locale/en_US.UTF-8/license.txt
%{_usr}/lib/cups/filter/ptm6500Filter

%changelog
* Sat Oct 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.3143-2
- Use alternatives to provide /usr/bin/sublime_text binary.
