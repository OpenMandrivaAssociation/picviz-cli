%define name picviz-cli
%define version 0.6
%define release %mkrel 2

Name: %name
Version: %version
Release: %release
Summary: Command-line frontend for picviz
License: GPLv3+
Group: Graphics
URL: http://www.wallinfire.net/picviz
Source0: http://www.wallinfire.net/files/picviz/%{name}-%{version}.tar.gz
BuildRequires: libpicviz-devel
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Command-line frontend for picviz.

%prep
%setup -q

%build
pushd src
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 src/pcv %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 doc/*.1 %{buildroot}%{_mandir}/man1
install -d -m 755 %{buildroot}%{_datadir}/picviz-cli
install -m 644 templates/*.pgdt %{buildroot}%{_datadir}/picviz-cli

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/manual.html doc/picviz-arch.jpeg
%{_bindir}/pcv
%{_mandir}/man1/pcv.1*
%{_datadir}/picviz-cli



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-2mdv2011.0
+ Revision: 614542
- the mass rebuild of 2010.1 packages

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdv2010.1
+ Revision: 509068
- import picviz-cli


* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdv2010.1
- initial standalone package 
