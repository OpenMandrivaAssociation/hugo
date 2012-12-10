Name:			hugo
Version:		2.12
Release:		%mkrel 11

Summary:	Hu-Go! - TurboGrafx 16/PC-Engine Emulator
License:	GPLv2+
Group:		Emulators
URL:		http://www.zeograd.com/
Source0:	http://www.zeograd.com/download/%{name}-%{version}.tar.bz2
Source1:	%{name}-48.png
Patch0:		hugo-2.12-gcc4.patch
Patch1:		hugo-2.12-x86_64fix.patch
Patch2:		hugo-2.12-x86_64-fixes-backport.patch

BuildRequires:	gtk+2-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf2.5

BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Hu-Go! is a TurboGrafx 16/PC-Engine Emulator.
There is some public domain roms you play with.
The other games need that you own the original card or CD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
autoconf

%build
./configure --prefix=%{buildroot}/%{_prefix} --bindir=%{buildroot}/%{_gamesbindir} --libdir=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall bindir=%{buildroot}/%{_gamesbindir}

install -d -m 755 %{buildroot}%{_mandir}/man6/
install -m 644 %{name}*.6 %{buildroot}%{_mandir}/man6/

install -D -m 644 %{_sourcedir}/%{name}-48.png %{buildroot}%{_iconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat<<EOF>%{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Hugo
Comment=Hu-Go!
Exec=%{_gamesbindir}/hugo
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;Emulator;
EOF

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL NEWS README
%attr(0755,root,games) %{_gamesbindir}/%{name}
%{_gamesbindir}/hugod
%{_datadir}/applications/mandriva-%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_iconsdir}/*.png
%{_mandir}/man6/%{name}*.6*


%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}

%postun
%{clean_menus}
%endif



%changelog
* Fri Jul 29 2011 Andrey Bondrov <abondrov@mandriva.org> 2.12-11mdv2012.0
+ Revision: 692192
- imported package hugo


* Thu Jul 21 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 2.12-11mdv2011.0
- Import from PLF
- Remove PLF reference

* Wed Jan 20 2010 Götz Waschk <goetz@zarb.org> 2.12-10plf2010.1
- update menu

* Tue Jan 13 2009 Guillaume Bedot <littletux@zarb.org> 2.12-9plf2009.1
- utf8 changelog

* Tue Jan 13 2009 Guillaume Bedot <littletux@zarb.org> 2.12-8plf2009.1
- fixed 64bit build (segfaulted)
- added man pages
- fixed license
- dropped old-style menu

* Sun Dec 21 2008 Götz Waschk <goetz@zarb.org> 2.12-7plf2009.1
- rebuild

* Sun Dec 16 2007 Guillaume Bedot <littletux@zarb.org> 2.12-6plf2008.1
- fix desktop file

* Tue Aug  1 2006 Götz Waschk <goetz@zarb.org> 2.12-5plf2007.0
- xdg menu

* Mon Dec 19 2005 Götz Waschk <goetz@zarb.org> 2.12-4plf
- fix directory conflict
- Rebuild

* Mon Nov  7 2005 Anssi Hannula <anssi@zarb.org> 2.12-3plf
- fix x86_64 build (patch2)
- distsuffix

* Mon Nov  7 2005 Götz Waschk <goetz@zarb.org> 2.12-2plf
- fix buildrequires
- patch for gcc 4

* Sun Apr 10 2005 Guillaume Bedot <littletux@zarb.org> 2.12-1plf
- New release with some bug fixes :)

* Mon Mar 14 2005 Götz Waschk <goetz@zarb.org> 2.11-1plf
- update file list
- fix buildrequires
- drop patches
- fix URL
- fix License
- new version

* Thu Feb 17 2005 Götz Waschk <goetz@zarb.org> 2.10-4plf
- fix build

* Mon Jul 21 2003 Götz Waschk <goetz@plf.zarb.org> 2.10-3plf
- buildrequires fix

* Fri Jul 18 2003 Götz Waschk <goetz@plf.zarb.org> 2.10-2plf
- patch to fix build with current gcc
- quiet tar

* Thu Apr 10 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.10-1plf
- => plf
- games path
- somes minor fix

* Tue Mar 04 2003 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 2.10-1mdk
- Update to 2.10.

* Tue Feb 25 2003 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 2.10-0-20030225
- Update to latest CVS.
- Added menu entry and icons for the GUI.

* Thu Feb 13 2003 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 2.10-0-13022003
- First try to package Hu-Go!
