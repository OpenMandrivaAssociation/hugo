Summary:	Hu-Go! - TurboGrafx 16/PC-Engine Emulator
Name:		hugo
Version:	2.12
Release:	12
License:	GPLv2+
Group:		Emulators
Url:		http://www.zeograd.com/
Source0:	http://www.zeograd.com/download/%{name}-%{version}.tar.bz2
Source1:	%{name}-48.png
Patch0:		hugo-2.12-gcc4.patch
Patch1:		hugo-2.12-x86_64fix.patch
Patch2:		hugo-2.12-x86_64-fixes-backport.patch
Patch3:		hugo-2.12-sfmt.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)

%description
Hu-Go! is a TurboGrafx 16/PC-Engine Emulator. There is some public domain roms
you play with. The other games need that you own the original card or CD.

%files
%doc AUTHORS NEWS README
%attr(0755,root,games) %{_gamesbindir}/%{name}
%{_gamesbindir}/hugod
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_iconsdir}/*.png
%{_mandir}/man6/%{name}*.6*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
autoconf

%build
%configure2_5x
%make

%install
%makeinstall bindir=%{buildroot}/%{_gamesbindir}

install -d -m 755 %{buildroot}%{_mandir}/man6/
install -m 644 %{name}*.6 %{buildroot}%{_mandir}/man6/

install -D -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat<<EOF>%{buildroot}%{_datadir}/applications/%{name}.desktop
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

