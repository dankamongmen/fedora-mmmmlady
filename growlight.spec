Name:          growlight
Version:       1.2.6
Release:       1%{?dist}
Summary:       Disk manipulation and system setup tool
License:       GPL3
URL:           https://nick-black.com/dankwiki/index.php/Growlight
Source0:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/%{name}_%{version}.tar.xz
Source1:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/%{name}_%{version}.tar.xz.asc
Source2:       https://nick-black.com/dankamongmen.gpg

BuildRequires: gnupg2
BuildRequires: gcc-c++
BuildRequires: readline-devel
BuildRequires: libpciaccess-devel
BuildRequires: cmake
# for xsltproc
BuildRequires: libxslt
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(notcurses)
BuildRequires: pkgconfig(libatasmart)
BuildRequires: pkgconfig(libudev)
BuildRequires: device-mapper-devel
BuildRequires: cryptsetup-devel
BuildRequires: docbook5-style-xsl
BuildRequires: docbook-utils

%description
Growlight can manipulate both physical (NVMe, SATA, etc.) and virtual (mdadm,
device-mapper, etc.) block devices, help identify bottlenecks in a storage
topology, create and destroy filesystems, and prepare a machine for initial
boot when run in an installer context. Both full-screen and REPL readline UIs
are available.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure --disable-zfs
%make_build

%install
%make_install

%files
%doc COPYING README
%{_bindir}/growlight
%{_bindir}/growlight-readline
%{_mandir}/man1/*.1*

%changelog
* Thu Jun 18 2020 Nick Black <dankamongmen@gmail.com> - 1.2.6-1
- Initial packaging for Fedora 33
