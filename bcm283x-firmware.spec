%global debug_package %{nil}

# Tarfile created using git 		
# git clone https://github.com/raspberrypi/firmware.git
# cd firmware/boot
# tar cJvf ../bcm283x-firmware-%{gitshort}.tar.xz *bin *dat *elf LICENCE.broadcom overlays/README
%define gitshort 8b9d7b8

Name:          bcm283x-firmware
Version:       20150619
Release:       1.%{gitshort}%{?dist}
Summary:       Broadcom bcm283x firmware for the Raspberry Pi

Group:         System Environment/Kernel
# see LICENSE.broadcom
License:       Redistributable, no modification permitted
URL:           https://github.com/raspberrypi/

Source0:       %{name}-%{gitshort}.tar.xz
Source1:       config.txt
Source2:       cmdline.txt

ExclusiveArch: %{arm}

%description
Firmware for the Broadcom bcm283x SoC as shipped in devices such as the
Raspberry Pi.

%prep
%setup -q -n %{name}-%{gitshort} -c %{name}-%{gitshort}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}/overlays
install -p %{SOURCE1} %{buildroot}/%{_datadir}/%{name}
install -p %{SOURCE2} %{buildroot}/%{_datadir}/%{name}
install -p *bin %{buildroot}/%{_datadir}/%{name}
install -p *dat %{buildroot}/%{_datadir}/%{name}
install -p *elf %{buildroot}/%{_datadir}/%{name}
install -p overlays/README %{buildroot}/%{_datadir}/%{name}/overlays

%files
%license LICENCE.broadcom
%{_datadir}/%{name}

%changelog
* Sun Jun 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150619-1.8b9d7b8
- Latest firmware update
- update config.txt for default kernel name

* Fri Jun 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150617-2.fc6c989
- Add cmdline.txt, update config.txt

* Fri Jun 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150617-1.fc6c989
- Latest firmware update
- Add default config.txt

* Thu Jun 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150615-3.37600d5
- Fix license field

* Thu Jun 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150615-2.37600d5
- Updates for review

* Mon Jun 15 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150615-1.37600d5
- Initial version
