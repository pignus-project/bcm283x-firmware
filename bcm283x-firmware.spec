%global debug_package %{nil}

# Tarfile created using git 		
# git clone https://github.com/raspberrypi/firmware.git
# cd firmware/boot
# tar cJvf ../bcm283x-firmware-%{gitshort}.tar.xz *bin *dat *elf LICENCE.broadcom overlays/README
%define gitshort c93fb48

Name:          bcm283x-firmware
Version:       20160913
Release:       2.%{gitshort}%{?dist}
Summary:       Broadcom bcm283x firmware for the Raspberry Pi

Group:         System Environment/Kernel
# see LICENSE.broadcom
License:       Redistributable, no modification permitted
URL:           https://github.com/raspberrypi/

Source0:       %{name}-%{gitshort}.tar.xz
Source1:       config.txt
Source2:       cmdline.txt

ExclusiveArch: %{arm} aarch64

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
* Sat Sep 24 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160913-2.c93fb48
- Minor config tweaks

* Wed Sep 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160913-1.c93fb48
- Numerous config enhancements
- Latest firmware fixes

* Sat Aug 27 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160823-1.d0bc6ce
- Latest firmware fixes

* Tue Jul 12 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160712-1.6ab4d20
- Latest firmware fixes

* Mon May 16 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160513-1.c17fa41
- Config options for HW rev 3
- Latest firmware fixes

* Sat Apr 30 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160430-1.611d798
- Latest firmware update

* Mon Mar  7 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160307-1.a192a05
- Latest firmware update

* Wed Mar  2 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160229-1.9cd1c6c
- Latest firmware update
- Build for aarch64

* Mon Feb  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160201-1.cb2ffaa
- Latest firmware update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151219-2.1efc1ec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20151219-1.1efc1ec
- Latest firmware update

* Mon Oct  5 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20151004-1.b06b317
- Latest firmware update

* Fri Aug 28 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150824-1.c6ae1d6
- Latest firmware update

* Fri Jul 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150723-1.43c4847
- Latest firmware update

* Tue Jun 30 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150630-1.89881b5
- Latest firmware update

* Wed Jun 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150623-1.856e2e1
- Latest firmware update

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
