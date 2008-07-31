%define major		0
%define libname		%mklibname %{name}_ %{major}
%define develname	%mklibname %{name} -d

Summary:	Utilities for accessing a Rio 500 player
Name:		rio500
Version:	0.9.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Source0:	http://downloads.sourceforge.net/rio500/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://rio500.sourceforge.net/
BuildRequires:	libglib2.0-devel
BuildRequires:	libusb-devel
Obsoletes:	rio500-utils < %{version}-%{release}
Obsoletes:	rio500-share < %{version}-%{release}
Conflicts:	rio500-share < %{version}-%{release}

%description 
The Rio 500 support package consists of a static library (librio500)
containing low level rio access routines and a number of command
line utilities. These utilities will allow you to format the
memory in your rio, add/delete folders, and add/delete songs.

%package -n %{libname}
Summary:	Shared library for rio500
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library from the rio500 application
for accessing the Rio 500 music player.

%package -n %{develname}
Summary:	Development headers and static library for rio500
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	rio500-devel <= %{version}-%{release}

%description -n %{develname}
This package includes the header files and libraries needed for
developing programs accessing a Rio 500.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIC -DPIC"
%configure2_5x --with-id3support

%make

%install
[ -d %{buildroot} ] && rm -rf %{buildroot}

%{makeinstall_std}

%find_lang %{name}

%clean
rm -rf %{buildroot} 

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%{_bindir}/*
%{_mandir}/*/*
%{_sysconfdir}/udev/rules.d/60-rio500.rules
%{_datadir}/hal/fdi/information/20thirdparty/10-usb-music-players-rio500.fdi
%{_datadir}/%{name}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%{_libdir}/lib%{name}.*a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/rio500

