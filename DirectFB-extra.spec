#
# Conditional build:
%bcond_without	flash	# don't build FLASH video provider
#
Summary:	Additional providers and drivers for DirectFB
Summary(pl):	DirectFB - dodatkowe wtyczki i sterowniki do DirectFB
Name:		DirectFB-extra
Version:	0.9.16
Release:	3
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/download/DirectFB-extra/%{name}-%{version}.tar.gz
# Source0-md5:	e5084d213dfd309987d139f816930340
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-updates.patch
URL:		http://www.directfb.org/
#BuildRequires:	DirectFB-devel >= %{version}
BuildRequires:	DirectFB-devel >= 0.9.20
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_flash:BuildRequires:	flash-devel >= 0.4.10-5}
BuildRequires:	imlib2-devel
BuildRequires:	libtool
BuildRequires:	openquicktime-devel
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

%package -n DirectFB-video-openquicktime
Summary:	OpenQuicktime video provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca obraz OpenQuicktime
Group:		Libraries
%requires_eq	DirectFB

%description -n DirectFB-video-openquicktime
This package contains OpenQuicktime video provider for DirectFB.

%description -n DirectFB-video-openquicktime -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± obraz
OpenQuicktime.

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# paths for libflash
CPPFLAGS="-I/usr/X11R6/include"
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
%configure \
	--disable-avifile \
	%{!?with_flash:--disable-flash}

%{__make} \
	MODULEDIR=%{dfbdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MODULEDIR=%{dfbdir}

rm -f $RPM_BUILD_ROOT%{dfbdir}/interfaces/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n DirectFB-image-imlib2
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_imlib2.so

%files -n DirectFB-video-openquicktime
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_openquicktime.so

%if %{with flash}
%files -n DirectFB-video-swf
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_swf.so
%endif
