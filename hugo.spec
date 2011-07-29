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

