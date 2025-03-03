%define name xmms-crossfade
%define version 0.3.14
%define release %mkrel 6
%define build_audacious 0

Name:          %name
Summary:       Crossfade output plugin for XMMS
Version:       %version
Release:       %release
Group:         Sound
License:       GPLv2+
BuildRequires: xmms 
BuildRequires: libxmms-devel
BuildRequires: libsamplerate-devel
BuildRequires: automake1.8
Requires:      xmms
Url:		https://www.eisenlohr.org/xmms-crossfade/news.html
Source:        http://www.eisenlohr.org/xmms-crossfade/%name-%version.tar.gz
BuildRoot:     %_tmppath/%name-buildroot


%description
xmms-crossfade is an XMMS Output Plugin for Crossfading / Continuous Output.

It features:

* Crossfading
* Continuous output
* Gap-Killer: Some mp3-encoders produce small gaps of silence at the
  beginning or end of the stream. They can automatically be detected
  and removed.

%if %build_audacious
%package -n audacious-crossfade
Group: Sound
Summary: Crossfade output plugin for Audacious
BuildRequires: audacious-devel
BuildRequires: audacious
Requires: audacious
Provides: beep-media-player-crossfade
Obsoletes: beep-media-player-crossfade

%description -n audacious-crossfade
This is an Audacious Output Plugin for Crossfading / Continuous Output.

It features:

  * Crossfading
  * Continuous output
  * Gap-Killer: Some mp3-encoders produce small gaps of silence at the
    beginning or end of the stream. They can automatically be detected
    and removed.
%endif

%prep
%setup -q
mkdir xmms-build audacious-build

%build
%define _disable_ld_no_undefined 1
cd xmms-build
CONFIGURE_TOP=.. %configure2_5x --enable-player=xmms
%make
%if %build_audacious
cd ../audacious-build
CONFIGURE_TOP=.. %configure2_5x --enable-player=audacious
%make
%endif

%install
rm -rf $RPM_BUILD_ROOT
cd xmms-build
%makeinstall libdir=%buildroot%{_libdir}/xmms/Output/
%if %build_audacious
cd ../audacious-build
%makeinstall libdir=%buildroot%{_libdir}/audacious/Output/
%endif
rm -f %buildroot%{_libdir}/*/Output/libcrossfade.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_libdir}/xmms/Output/libcrossfade.so

%if %build_audacious
%files -n audacious-crossfade
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_libdir}/audacious/Output/libcrossfade.so
%endif


