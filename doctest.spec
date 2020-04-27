Name:           doctest
Version:        2.3.7
Release:        1%{?dist}
Summary:        C++ header-only unit testing framework
License:        MIT
URL:            https://github.com/onqtam/doctest
Source0:        https://github.com/onqtam/doctest/archive/%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/dankamongmen/fedora-mmmmlady/master/%{version}.tar.gz.asc
Source2:        https://nick-black.com/dankamongmen.gpg

BuildRequires: cmake

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
mkdir build
cd build
%cmake ..
%make_build

%install
cd build
%make_install

%files
%doc CHANGELOG.md README.md
%license COPYRIGHT LICENSE
%{_includedir}/*.h
%{_libdir}/cmake/doctest
