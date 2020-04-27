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
BuildRequires: gnupg2
BuildRequires: gcc-c++

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%global debug_package %{nil}

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
mkdir -p %{buildroot}/%{_docdir}/doctest
install -m 0644 ../CHANGELOG.md ../README.md %{buildroot}/%{_docdir}/doctest/

%files
%docdir %{_docdir}/doctest
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_includedir}/doctest/
%{_libdir}/cmake/doctest/
%{_docdir}/doctest/CHANGELOG.md
%{_docdir}/doctest/README.md
