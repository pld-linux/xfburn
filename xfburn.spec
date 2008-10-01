#
#
Summary:	Xfburn is a simple CD/DVD burning tool
Summary(pl.UTF-8):	Xfburn to proste narzędzie do wypalania CD/DVD
Name:		xfburn
Version:	0.3.2
Release:	0.2
License:	GPL v2
Group:		Applications
Source0:	http://goodies.xfce.org/releases/xfburn/%{name}-%{version}.tar.gz
# Source0-md5:	b70219d92c6cdbe0c89c8ae073395ea4
URL:		http://goodies.xfce.org/projects/applications/xfburn/	
BuildRequires:	libburn-devel
BuildRequires:	libisofs-devel
BuildRequires:	libxfcegui4-devel
BuildRequires:	libexo-devel
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
tworzenie obrazów płyt jak również przygotowywanie własnych zestawów danych.
Program znajduje się obecnie w fazie gwałtownego rozwoju, obsługa
płyt audio CD zostanie dodana w kolejnej wersji.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_iconsdir}/hicolor/*/*/*/*.png
%{_iconsdir}/hicolor/*/*/*/*.svg
%{_datadir}/%{name}/%{name}-toolbars.ui
%{_datadir}/%{name}/%{name}.ui
%{_desktopdir}/%{name}.desktop
