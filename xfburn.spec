Summary:	Xfburn - a simple CD/DVD burning tool
Summary(pl.UTF-8):	Xfburn - proste narzędzie do wypalania CD/DVD
Name:		xfburn
Version:	0.4.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfburn/%{name}-%{version}.tar.bz2
# Source0-md5:	f5ed76149fd348504d4a75830b4996dc
Patch0:		%{name}-po.patch
URL:		http://goodies.xfce.org/projects/applications/xfburn/
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	hal-devel >= 0.5.7
BuildRequires:	libburn-devel >= 0.5.6
BuildRequires:	libexo-devel >= 0.3.0
BuildRequires:	libisofs-devel >= 0.6.2
BuildRequires:	libxfcegui4-devel >= 4.4.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):  desktop-file-utils
Requires(post,postun):  gtk+2
Requires(post,postun):  hicolor-icon-theme
Requires:       hal >= 0.5.7
Requires:	Thunar >= 0.9.3
Suggests:       dvd+rw-tools
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

%build
# fix locale names
mv -f po/{pt_PT.po,pt.po}
mv -f po/{nb_NO.po,nb.po}

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
