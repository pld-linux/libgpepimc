Summary:	GPE PIM Categories library
Summary(pl.UTF-8):	Biblioteka kategorii GPE PIM
Name:		libgpepimc
Version:	0.9
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	0d22564e0a897b3be2eb9d2fc71fbd65
Source1:	%{name}.pl.po
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	gtk+2-devel >= 2:2.2
BuildRequires:	intltool >= 0.23
BuildRequires:	libgpewidget-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite-devel
# hildon-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE PIM Categories library.

%description -l pl.UTF-8
Biblioteka kategorii GPE PIM.

%package devel
Summary:	Header files for libgpepimc
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgpepimc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.2
Requires:	libgpewidget-devel
Requires:	sqlite-devel

%description devel
Header files for libgpepimc.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgpepimc.

%package static
Summary:	Static libgpepimc library
Summary(pl.UTF-8):	Statyczna biblioteka libgpepimc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgpepimc library.

%description static -l pl.UTF-8
Statyczna biblioteka libgpepimc.

%package apidocs
Summary:	libgpepimc API documentation
Summary(pl.UTF-8):	Dokumentacja API libgpepimc
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgpepimc API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgpepimc.

%prep
%setup -q

cp %{SOURCE1} po/pl.po
sed -i -e 's/ALL_LINGUAS=""/ALL_LINGUAS="pl"/' configure.ac

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libgpepimc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpepimc.so
%{_libdir}/libgpepimc.la
%{_includedir}/gpe/pim-categories-ui.h
%{_includedir}/gpe/pim-categories.h
%{_pkgconfigdir}/libgpepimc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpepimc.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgpepimc
