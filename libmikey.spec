%define name	libmikey
%define oname	mikey
%define version 0.4.1
%define cvs	20061210
%define release %mkrel 0.%cvs.2

%define major	0
%define libname %mklibname %oname %major

Name: 	 	%{name}
Summary: 	IKey library from MiniSip
Version: 	%{version}
Release: 	%{release}

Source:		http://www.minisip.org/source/%{name}-%{version}-%cvs.tar.bz2
URL:		http://www.minisip.org/
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libmcrypto-devel >= 0.3.1-0.20061210.0
BuildRequires:	libmutil-devel >= 0.3.1-0.20061210.0

%description
IKey library from MiniSip

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %name

%build
./bootstrap
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README 
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


