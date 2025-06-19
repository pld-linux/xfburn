Summary:	Xfburn - a simple CD/DVD burning tool
Summary(pl.UTF-8):	Xfburn - proste narzędzie do wypalania CD/DVD
Name:		xfburn
Version:	0.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/xfburn/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	0ae5e3e94c71857b7cd8555f9f18625f
URL:		https://goodies.xfce.org/projects/applications/xfburn/
BuildRequires:	Thunar-devel >= 1.6.6
BuildRequires:	exo-devel >= 0.11.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.66.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	libburn-devel >= 0.5.6
BuildRequires:	libisofs-devel >= 0.6.2
BuildRequires:	libxfce4ui-devel >= 4.18.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	udev-glib-devel >= 145
Requires(post,postun):	desktop-file-utils
Requires:	Thunar >= 1.6.6
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

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# not supported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK}

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
%doc AUTHORS ChangeLog NEWS README.md TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_iconsdir}/hicolor/*/stock/media/*.png
%{_iconsdir}/hicolor/*/stock/media/*.svg
%{_datadir}/%{name}
%{_datadir}/Thunar/sendto/thunar-sendto-%{name}.desktop
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/xfburn.1*
%{_datadir}/metainfo/org.xfce.xfburn.appdata.xml
