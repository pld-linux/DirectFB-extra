#
# Conditional build:
%bcond_without	flash	# don't build FLASH video provider
%bcond_without	mpg	# don't build support for MPG/MPEG3
%bcond_without	swfdec	# don't build swfdec video provider
#
# broken currently (needs update for DirectFB 1.2.x)
%undefine	with_flash
# needs update for swfdec 0.6.x
%undefine	with_swfdec
Summary:	Additional providers and drivers for DirectFB
Summary(pl.UTF-8):	DirectFB - dodatkowe wtyczki i sterowniki do DirectFB
Name:		DirectFB-extra
Version:	1.2.0
%define	subver	rc1
Release:	0.%{subver}.0.1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Extras/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	c3c160c167c20f320b0c0562168d0579
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-mpeg3_open.patch
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= 1:%{version}
BuildRequires:	FusionSound-devel >= 1.1.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
%{?with_flash:BuildRequires:	gplflash-devel >= 0.4.10-5}
BuildRequires:	imlib2-devel
BuildRequires:	jasper-devel
%{?with_mpg:BuildRequires:	libmpeg3-devel}
BuildRequires:	libsvg-cairo-devel >= 0.1.6
BuildRequires:	libtool
BuildRequires:	openquicktime-devel
BuildRequires:	pkgconfig >= 1:0.9
%{?with_swfdec:BuildRequires:	swfdec-devel >= 0.5.0}
BuildRequires:	xine-lib-devel >= 2:1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dfbdir		%(pkg-config --variable=moduledir directfb-internal)

%description
This package contains additional image/video/font providers and
graphics/input drivers (currently Imlib2 image provider and
OpenQuicktime video provider).

%description -l pl.UTF-8
Ten pakiet zawiera dodatkowe wtyczki dostarczające grafikę, obraz i
fonty oraz sterowniki grafiki i wejściowe (aktualnie: wtyczkę
dostarczającą grafikę poprzez Imlib2 oraz wtyczkę dostarczającą obraz
OpenQuicktime).

%package -n DirectFB-image-bmp
Summary:	BMP image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę BMP
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-image-bmp
This package contains BMP mage provider for DirectFB.

%description -n DirectFB-image-bmp -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę BMP.

%package -n DirectFB-image-imlib2
Summary:	Imlib2 image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę poprzez Imlib2
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-image-imlib2
This package contains image provider based on Imlib2 for DirectFB.

%description -n DirectFB-image-imlib2 -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę poprzez
bibliotekę Imlib2.

%package -n DirectFB-image-jpeg2000
Summary:	JPEG-2000 image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę JPEG-2000
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-image-jpeg2000
This package contains JPEG-2000 image provider.

%description -n DirectFB-image-jpeg2000 -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę
JPEG-2000.

%package -n DirectFB-image-mpeg2
Summary:	MPEG-2 image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę MPEG-2
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-image-mpeg2
This package contains MPEG-2 image provider.

%description -n DirectFB-image-mpeg2 -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę MPEG-2.

%package -n DirectFB-image-pnm
Summary:	PNM image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę PNM
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-image-pnm
This package contains PNM image provider. It supports PBM, PGM and PPM
formats (both ASCII and RAW).

%description -n DirectFB-image-pnm -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę PNM.
Obsługuje formaty PBM, PGM i PPM (zarówno ASCII, jak i binarne).

%package -n DirectFB-image-svg
Summary:	SVG image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę SVG
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-image-svg
This package contains SVG image provider using Cairo library.

%description -n DirectFB-image-svg -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę SVG przy
użyciu biblioteki Cairo.

%package -n DirectFB-video-ffmpeg
Summary:	FFmpeg video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz FFmpeg
Group:		Libraries
%requires_eq	DirectFB
%requires_eq	FusionSound

%description -n DirectFB-video-ffmpeg
DirectFB video provider using FFmpeg codecs.

%description -n DirectFB-video-ffmpeg -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczajacą obraz przy
użyciu kodeków FFmpeg.

%package -n DirectFB-video-libmpeg3
Summary:	MPEG video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz MPEG
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-video-libmpeg3
This package contains MPEG (MPEG-1 and MPEG-2) video provider for
DirectFB. It uses libmpeg3 library.

%description -n DirectFB-video-libmpeg3 -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczajacą obraz MPEG
(MPEG-1 i MPEG-2) przy użyciu biblioteki libmpeg3.

%package -n DirectFB-video-openquicktime
Summary:	OpenQuicktime video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz OpenQuicktime
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-video-openquicktime
This package contains OpenQuicktime video provider for DirectFB. It
supports all RGB and YUV formats and does audio playback.

%description -n DirectFB-video-openquicktime -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą obraz
OpenQuicktime. Obsługuje wszystkie formaty RGB i YUV oraz odtwarza
dźwięk.

%package -n DirectFB-video-swf
Summary:	ShockWave Flash video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz ShockWave Flash
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-video-swf
This package contains SWF (ShockWave Flash) video provider for
DirectFB. It uses flash library.

%description -n DirectFB-video-swf -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą obraz SWF
(ShockWave Flash) przy użyciu biblioteki flash.

%package -n DirectFB-video-swfdec
Summary:	ShockWave Flash video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz ShockWave Flash
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-video-swfdec
This package contains SWF (ShockWave Flash) video provider for
DirectFB. It uses swfdec library.

%description -n DirectFB-video-swfdec -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą obraz SWF
(ShockWave Flash) przy użyciu biblioteki swfdec.

%package -n DirectFB-video-xine
Summary:	XINE video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz XINE
Group:		Libraries
%requires_eq	DirectFB
%requires_eq	xine-lib

%description -n DirectFB-video-xine
This package contains video provider for DirectFB which uses XINE
library and plugins. It handles a wide range of video formats.

%description -n DirectFB-video-xine -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą obraz przy
użyciu biblioteki i wtyczek XINE. Obsługuje szeroki zakres formatów
obrazu.

%package -n xine-ui-dfb
Summary:	DirectFB-based XINE UI
Summary(pl.UTF-8):	Interfejs użytkownika XINE oparty na DirectFB
Group:		Applications/Multimedia
%requires_eq	DirectFB
Requires:	xine-lib >= 2:1.0-0.rc3

%description -n xine-ui-dfb
DirectFB-based XINE UI. This package contains also DirectFB video
output plugin for XINE.

%description -n xine-ui-dfb -l pl.UTF-8
Interfejs użytkownika XINE oparty na DirectFB. Zawiera także wtyczkę
wyjścia obrazu DirectFB dla XINE.

%prep
%setup -q -n %{name}-%{version}-%{subver}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/libmpeg3"
%configure \
	--disable-avifile \
	%{?with_flash:--enable-flash} \
	%{?with_mpg:--enable-libmpeg3} \
	--enable-openquicktime \
	%{!?with_swfdec:--disable-swfdec}

%{__make} \
	FFMPEG_CFLAGS="-I/usr/include/libavcodec -I/usr/include/libavformat" \
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

%files -n DirectFB-image-bmp
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_bmp.so

%files -n DirectFB-image-imlib2
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_imlib2.so

%files -n DirectFB-image-jpeg2000
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_jpeg2000.so

%files -n DirectFB-image-mpeg2
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_mpeg2.so

%files -n DirectFB-image-pnm
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_pnm.so

%files -n DirectFB-image-svg
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_svg.so

%files -n DirectFB-video-ffmpeg
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_ffmpeg.so

%if %{with mpg}
%files -n DirectFB-video-libmpeg3
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_libmpeg3.so
%endif

%files -n DirectFB-video-openquicktime
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_openquicktime.so

%if %{with flash}
%files -n DirectFB-video-swf
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_swf.so
%endif

%if %{with swfdec}
%files -n DirectFB-video-swfdec
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_swfdec.so
%endif

%files -n DirectFB-video-xine
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_xine.so

%files -n xine-ui-dfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/df_xine
%attr(755,root,root) %{_libdir}/xine/plugins/*/xineplug_vo_out_dfb.so
