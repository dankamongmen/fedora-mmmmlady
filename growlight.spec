Name:           growlight
Version:        1.2.5
Release:        1%{?dist}
Summary:        Disk manipulation and system setup tool
License:        GPL3
URL:            https://nick-black.com/dankwiki/index.php/Growlight
Source0:        https://github.com/dankamongmen/%{name}/archive/v%{version}.tar.gz
BuildRequires:  autoconf-archive, readline-devel, pkgconfig(libpciaccess),
                 xsltproc, pkgconfig(libpci), pkgconfig(notcurses), pkgconfig(libatasmart),
                 pkgconfig(libudev), device-mapper-devel, cryptsetup-devel,

%description
Growlight can manipulate both physical (NVMe, SATA, etc.) and virtual (mdadm,
device-mapper, etc.) block devices, help identify bottlenecks in a storage
topology, create and destroy filesystems, and prepare a machine for initial
boot when run in an installer context. Both full-screen and REPL readline UIs
are available.

%prep
%setup -q

%build
%configure --disable-zfs
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc COPYING README
%{_bindir}/growlight
%{_bindir}/growlight-readline

%changelog
* Thu Jun 18 2020 Nick Black <dankamongmen@gmail.com> - 1.2.5-1
- Initial packaging for Fedora 33
