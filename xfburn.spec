Summary:	Xfburn - a simple CD/DVD burning tool
Summary(pl.UTF-8):	Xfburn - proste narzędzie do wypalania CD/DVD
Name:		xfburn
Version:	0.4.3
Release:	5
License:	GPL v2+
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfburn/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	147cdc2d909e751125be16103b8dc81f
Patch0:		%{name}-po.patch
Patch1:		%{name}-gio.patch
Patch2:		%{name}-ui.patch
Patch3:		glib-2.32.patch
URL:		http://goodies.xfce.org/projects/applications/xfburn/
BuildRequires:	Thunar-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	exo-devel >= 0.6.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.2
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool
BuildRequires:	libburn-devel >= 0.5.6
BuildRequires:	libisofs-devel >= 0.6.2
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	udev-glib-devel
Requires(post,postun):	desktop-file-utils
Requires:	Thunar >= 1.2.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Suggests:	dvd+rw-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfburn is a simple CD/DVD burning tool based on libburnia libraries.
It can blank CD/DVD-RWs, burn and create iso images, as well as burn
personal compositions of data to either CD or DVD. It Is currently
under heavy development, and audio CD support will be included in the
next release.

%description -l pl.UTF-8
Xfburn to proste narzędzie służące do wypalania płyt CD/DVD
wykorzystujące biblioteki libburnia. Obsługuje wymazywanie CD/DVD-RW,
tworzenie obrazów płyt, jak również przygotowywanie własnych zestawów
danych. Program znajduje się obecnie w fazie gwałtownego rozwoju,
obsługa płyt audio CD zostanie dodana w kolejnej wersji.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# unsupported Urdu Pakistan dialect
%{__rm} po/ur_PK.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_iconsdir}/hicolor/*/stock/media/*.png
%{_iconsdir}/hicolor/*/stock/media/*.svg
%{_datadir}/%{name}
%{_datadir}/Thunar/sendto/thunar-sendto-%{name}.desktop
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/xfburn.1*
