Summary:	Additional providers and drivers for DirectFB
Summary(pl):	DirectFB - dodatkowe wtyczki i sterowniki do DirectFB
Name:		DirectFB-extra
Version:	0.9.9
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/download/DirectFB-extra/%{name}-%{version}.tar.gz
Patch0:		%{name}-acfix.patch
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= %{version}
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	imlib2-devel
BuildRequires:	openquicktime-devel
BuildRequires:	pkgconfig >= 0.5
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

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-imlib2

%{__make} MODULEDIR=%{dfbdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MODULEDIR=%{dfbdir}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -n DirectFB-image-imlib2
#%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog README
#%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_imlib2.??

%files -n DirectFB-video-openquicktime
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_openquicktime.??
