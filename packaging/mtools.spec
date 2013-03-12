Summary: Programs for accessing MS-DOS disks without mounting the disks
Name: mtools
Version: 4.0.12
Release: 4
License: GPLv2+
Group: Applications/System
Source: ftp://ftp.gnu.org/gnu/mtools/mtools-%{version}.tar.bz2
Url: http://mtools.linux.lu/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch0: mtools-3.9.6-config.patch
Patch1: mtools-3.9.7-bigdisk.patch
Patch2: fix_mlabel_initialisation.patch

BuildRequires: texinfo, autoconf

%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 XDF disks, and 2m disks

Mtools should be installed if you need to use MS-DOS disks

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -fiv
%configure --disable-floppyd
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/%{_infodir}
%makeinstall
install -m644 mtools.conf $RPM_BUILD_ROOT/etc

# We aren't shipping this.
find $RPM_BUILD_ROOT -name "floppyd*" -exec rm {} \;

%remove_docs

%files
%defattr(-,root,root)
%config(noreplace) /etc/mtools.conf
%doc COPYING README Release.notes
/usr/bin/*

