%define major		0
%define libname		%mklibname %{name}_ %{major}
%define develname	%mklibname %{name} -d

Summary:	Utilities for accessing a Rio 500 player
Name:		rio500
Version:	0.9.1
Release:	7
License:	GPLv2+
Group:		Sound
Source0:	http://downloads.sourceforge.net/rio500/%{name}-%{version}.tar.bz2
Patch:		rio500-0.9.1-format-strings.patch
URL:		http://rio500.sourceforge.net/
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libusb)
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
%patch -p1

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



%changelog
* Mon Sep 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.1-5mdv2010.0
+ Revision: 439985
- fix format strings

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.1-3mdv2009.0
+ Revision: 260239
- rebuild

* Thu Jul 31 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.1-1mdv2009.0
+ Revision: 258612
- drop modified source (font freedom issue fixed upstream)
- drop link.patch (underlinking fixed upstream)
- new release 0.9.1

* Wed Jul 23 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.0-1mdv2009.0
+ Revision: 243100
- don't package COPYING
- new license policy
- rework package structure
- libify properly
- drop conditionals for libusb support (it's now mandatory)
- add link.patch to fix underlinking (has already been fixed in upstream CVS)
- use modified tarball with non-free fonts replaced
- drop gcc3.4-fix.patch (superseded upstream)
- new release 0.9.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.8.1-8mdv2008.1
+ Revision: 126611
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import rio500


* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.8.1-8mdk
- Rebuild

* Thu Jul  1 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.8.1-7mdk
- fix gcc3.4 patch

* Mon Jun 14 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.1-6mdk
- fix gcc-3.4 build (P0)
- fix buildrequires

* Mon Jul 21 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 0.8.1-5mdk
- Rebuild

* Fri Sep 27 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.8.1-4mdk
- Build librio500.a with PIC as it could be linked into a DSO that
  does require PIC, always. e.g. gnome-vfs-extras.

* Wed Jul 17 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8.1-3mdk
- Release 0.8.1

* Thu Apr 11 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8-3mdk
- New snapshot (it seems old 0.8 version was not released version)

* Thu Jul 19 2001 Stefan van der Eijk <stefan@eijk.nu> 0.8-2mdk
- BuildRequires:	glib-devel
- Copyright --> License

* Thu Apr 12 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8-1mdk
- Correct versionning and Description

* Thu Apr  5 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8-0.04052001.1mdk
- Snapshot release (04052001) which works with 2.4 kernel

* Tue Nov 21 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7-3mdk
- Correct path for fonts
- Use more macros

* Mon Oct  2 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7-2mdk
- Compiled with usbdevfs support

* Wed Aug 30 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.7-1mdk
- macros
- BM

* Mon Aug 11 2000 HA Quôc-Viêt <viet@mandrakesoft.com> 0.7-0mdk
- initial mdk release. no device created
- no usbdevfs support
- from Keith Clayton's spec file (kclayton@jps.net) for 0.7-1
