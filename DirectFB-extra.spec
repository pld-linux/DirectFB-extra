#
# Conditional build:
%bcond_without	flash	# don't build FLASH video provider
%bcond_without	mpg	# don't build support for MPG/MPEG3
#
Summary:	Additional providers and drivers for DirectFB
Summary(pl):	DirectFB - dodatkowe wtyczki i sterowniki do DirectFB
Name:		DirectFB-extra
Version:	0.9.21
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/download/DirectFB-extra/%{name}-%{version}.tar.gz
# Source0-md5:	119f47a5c8684ea1c291002629d50348
Patch0:		%{name}-acfix.patch
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= %{version}
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_flash:BuildRequires:	flash-devel >= 0.4.10-5}
BuildRequires:	imlib2-devel
%{?with_mpg:BuildRequires:	libmpeg3-devel}
BuildRequires:	libtool
BuildRequires:	openquicktime-devel
BuildRequires:	xine-lib-devel >= 2:1.0-0.rc2
BuildRequires:	pkgconfig >= 1:0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dfbdir		%(pkg-config --variable=moduledir directfb-internal)

%description
This package contains additional image/video/font providers and
graphics/input drivers (currently Imlib2 image provider and
OpenQuicktime video provider).

%description -l pl
Ten pakiet zawiera dodatkowe wtyczki dostarczaj±ce grafikê, obraz i
fonty oraz sterowniki grafiki i wej¶ciowe (aktualnie: wtyczkê
dostarczaj±c± grafikê poprzez Imlib2 oraz wtyczkê dostarczaj±c± obraz
OpenQuicktime).

%package -n DirectFB-image-imlib2
Summary:	Imlib2 image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca grafikê poprzez Imlib2
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-image-imlib2
This package contains image provider based on Imlib2 for DirectFB.

%description -n DirectFB-image-imlib2 -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± grafikê poprzez
bibliotekê Imlib2.

%package -n DirectFB-image-pnm
Summary:	PNM image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca grafikê PNM
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-image-pnm
This package contains PNM image provider. It supports PBM, PGM and PPM
formats (both ASCII and RAW).

%description -n DirectFB-image-pnm -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± grafikê PNM.
Obs³uguje formaty PBM, PGM i PPM (zarówno ASCII, jak i binarne).

%package -n DirectFB-video-libmpeg3
Summary:	MPEG video provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca obraz MPEG
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-video-libmpeg3
This package contains MPEG (MPEG-1 and MPEG-2) video provider for
DirectFB. It uses libmpeg3 library.

%description -n DirectFB-video-libmpeg3 -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczajac± obraz MPEG
(MPEG-1 i MPEG-2) przy u¿yciu biblioteki libmpeg3.

%package -n DirectFB-video-openquicktime
Summary:	OpenQuicktime video provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca obraz OpenQuicktime
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-video-openquicktime
This package contains OpenQuicktime video provider for DirectFB. It
supports all RGB and YUV formats and does audio playback.

%description -n DirectFB-video-openquicktime -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± obraz
OpenQuicktime. Obs³uguje wszystkie formaty RGB i YUV oraz odtwarza
d¼wiêk.

%package -n DirectFB-video-swf
Summary:	ShockWave Flash video provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca obraz ShockWave Flash
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-video-swf
This package contains SWF (ShockWave Flash) video provider for
DirectFB. It uses flash library.

%description -n DirectFB-video-swf -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± obraz SWF
(ShockWave Flash) przy u¿yciu biblioteki flash.

%package -n DirectFB-video-xine
Summary:	XINE video provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca obraz XINE
Group:		Libraries
%requires_eq	DirectFB
Requires:	xine-lib >= 2:1.0-0.rc2

%description -n DirectFB-video-xine
This package contains video provider for DirectFB which uses XINE
library and plugins. It handles a wide range of video formats.

%description -n DirectFB-video-xine -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± obraz przy
u¿yciu biblioteki i wtyczek XINE. Obs³uguje szeroki zakres formatów
obrazu.

%package -n xine-ui-dfb
Summary:	DirectFB-based XINE UI
Summary(pl):	Interfejs u¿ytkownika XINE oparty na DirectFB
Group:		Applications/Multimedia
%requires_eq	DirectFB
Requires:	xine-lib >= 2:1.0-0.rc2

%description -n xine-ui-dfb
DirectFB-based XINE UI. This package contains also DirectFB video
output plugin for XINE.

%description -n xine-ui-dfb -l pl
Interfejs u¿ytkownika XINE oparty na DirectFB. Zawiera tak¿e wtyczkê
wyj¶cia obrazu DirectFB dla XINE.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/libmpeg3"
%configure \
	--disable-avifile \
	%{!?with_flash:--disable-flash} \
	%{!?with_mpg:--disable-libmpeg3}

%{__make} \
	MODULEDIR=%{dfbdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MODULEDIR=%{dfbdir}

rm -f $RPM_BUILD_ROOT%{dfbdir}/interfaces/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/xine/plugins/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n DirectFB-image-imlib2
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_imlib2.so

%files -n DirectFB-image-pnm
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_pnm.so

%files -n DirectFB-video-openquicktime
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_openquicktime.so

%if %{with mpg}
%files -n DirectFB-video-libmpeg3
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_libmpeg3.so
%endif

%if %{with flash}
%files -n DirectFB-video-swf
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_swf.so
%endif

%files -n DirectFB-video-xine
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_xine.so

%files -n xine-ui-dfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/df_xine
%attr(755,root,root) %{_libdir}/xine/plugins/*/xineplug_vo_out_dfb.so
