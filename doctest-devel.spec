%global debug_package %{nil}

Name:           doctest-devel
Version:        2.3.7
Release:        1%{?dist}
Summary:        C++ header-only unit testing framework
License:        MIT
URL:            https://github.com/onqtam/doctest
Source0:        https://github.com/onqtam/doctest/archive/%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%prep
%setup -q -n doctest-%{version}

%build
mkdir build
cd build
%cmake ..
%make_build

%check
cd build
make_check

%install
cd build
%make_install
mkdir -p %{buildroot}/%{_docdir}/doctest
install -m 0644 ../CHANGELOG.md ../README.md %{buildroot}/%{_docdir}/doctest/

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_includedir}/doctest/
%{_libdir}/cmake/doctest
%{_docdir}/doctest/

%check
pushd build
ctest --output-on-failure
popd

%changelog
* Thu Apr 30 2020 Nick Black <dank@qemfd.net> - 2.3.7-1
- Initial RPM release
