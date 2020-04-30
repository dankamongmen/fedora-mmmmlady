Name:           doctest-devel
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
BuildArch: noarch

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -n doctest-%{version}

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
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_includedir}/doctest/
%{_libdir}/cmake/doctest/
%{_docdir}/doctest/

%changelog
* Thu Apr 30 2020 Nick Black <dank@qemfd.net> - 2.3.7-1
- Initial RPM release

