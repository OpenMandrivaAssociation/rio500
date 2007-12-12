%define enable_usbdevfs 0

Summary:	Rio 500 Support
Name:		rio500
Version:	0.8.1
Release:	8mdk
License:	GPL
Group:		Sound
Source0:	%{name}-%{version}.tar.bz2
Patch0:		rio500-gcc3.4-fix.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://rio500.sourceforge.net/
BuildRequires:	libglib2.0-devel
%if %{enable_usbdevfs}
BuildRequires:	libusb-devel
%endif

%description 
The Rio 500 support package consists of a static library (librio500)
containing low level rio access routines and a number of command
line utilities. These utilities will allow you to format the
memory in your rio, add/delete folders, and add/delete songs.

%package	utils
Summary:	%{summary}
Group:		%{group}
Obsoletes:	%{name}
Provides:	%{name} = %{version}-%{name}
Requires:	%{name}-share = %{version}-%{release}

%description	utils
The Rio 500 support package consists of a static library (librio500)
containing low level rio access routines and a number of command
line utilities. These utilities will allow you to format the
memory in your rio, add/delete folders, and add/delete songs.

%package	share
Summary:	%{summary}
Group:		%{group}

%description 	share
The Rio 500 support package consists of a static library (librio500)
containing low level rio access routines and a number of command
line utilities. These utilities will allow you to format the
memory in your rio, add/delete folders, and add/delete songs.

%package	devel
Summary:	Header files and static libraries needed for rio500 development
Group:		Development/Other
Requires:	%{name} = %{version}

%description	devel
This package includes the header files and libraries needed for
developing programs accesing a rio500.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC -DPIC"
%configure2_5x --with-id3support --with-psffont=%{_datadir}/rio500/fonts/font-bitmaps.psf --with-usbdevfs=%{enable_usbdevfs}

%make

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%{makeinstall_std}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/*
%{_mandir}/*/*

%files share -f %{name}.lang
%defattr(-,root,root)
%{_datadir}/rio500

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_libdir}/*
%{_includedir}/rio500

