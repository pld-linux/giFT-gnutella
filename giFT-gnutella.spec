
%define		sname	gift-gnutella

Summary:	The generic interface to FastTrack: gnutella plugin
Summary(pl):	Interfejs do FastTracka: plugin gnutelli
Name:		giFT-gnutella
Version:	0.0.5
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gift/%{sname}-%{version}.tar.bz2
# Source0-md5:	6f597001389020eb6130eddafb8d9a70
URL:		http://giFT.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giFT-devel >= 0.11.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The generic interface to FastTrack network. This package contains
gnutella plugin.

%description -l pl
Og�lny interfejs do sieci FastTrack. Ten pakiet zawiera plugin sieci
gnutella.

%prep
%setup -q -n %{sname}-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS TODO ChangeLog
%attr(755,root,root) %{_libdir}/giFT/*.so
%{_datadir}/giFT/*
