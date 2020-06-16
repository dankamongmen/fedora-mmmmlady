Name:           libtsm
Version:        4.0.1
Release:        4%{?dist}
Summary:        Terminal-emulator State Machine
License:        MIT
URL:            https://github.com/Aetf/libtsm
Source0:        https://github.com/Aetf/%{name}/archive/v%{version}.tar.gz
BuildRequires:  libxkbcommon-devel

%description
TSM is a state machine for DEC VT100-VT520 compatible terminal emulators. 
It tries to support all common standards while keeping compatibility to 
existing emulators like xterm, gnome-terminal, konsole...

TSM itself does not provide any rendering nor window management. It is a 
simple plain state machine without any external dependencies. It can be 
used to implement terminal emulators, but also to implement other applications
that need to interpret terminal escape sequences.

This library is very similar to libvte of the gnome project. However, 
libvte is highly bound to GTK+, which makes it unsuitable for non-graphics 
projects that need to parse escape sequences. Instead, TSM tries to restrict 
its API to terminal emulation only. Furthermore, TSM does not try to 
establish a new terminal emulation standard, but instead keeps compatibility 
as close to xterm as possible. This is why the TERM variable can be set to 
xterm-color256 with any TSM based terminal emulator.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.*a' -delete -print

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README
%{_libdir}/libtsm.so.*

%files devel
%{_includedir}/libtsm.h
%{_libdir}/libtsm.so
%{_libdir}/pkgconfig/libtsm.pc

%changelog
* Tue Jun 16 2020 Nick Black <dankamongmen@gmail.com> - 4.0.1-1
- Revived package, new upstream source, new upstream 4.0.1
