Name:          alacritty
Version:       0.4.3
Release:       1%{?dist}
Summary:       A cross-platform, GPU enhanced terminal emulator
License:       ASL 2.0
URL:           https://github.com/alacritty/alacritty
VCS:           https://github.com/alacritty/alacritty.git
Source0:       https://github.com/alacritty/%{name}/archive/v%{version}.tar.gz

BuildRequires: rust-packaging
BuildRequires: rust >= 1.32.0
BuildRequires: cargo
BuildRequires: cmake
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(xcb)
BuildRequires: desktop-file-utils
BuildRequires: %{python3}

%description
Alacritty is an OpenGL-based terminal emulator focused on performance. It
supports TrueColor and Wayland.

%prep
%setup -q -n alacritty-%{version}

%build
cargo build --release --offline

%install
install -p -D -m755 target/release/alacritty %{buildroot}%{_bindir}/alacritty
install -p -D -m644 extra/linux/alacritty.desktop %{buildroot}%{_datadir}/applications/alacritty.desktop
install -p -D -m644 extra/logo/alacritty-term.svg %{buildroot}%{_datadir}/pixmaps/Alacritty.svg
install -p -D -m644 alacritty.yml %{buildroot}%{_datadir}/alacritty/alacritty.yml
tic -xe alacritty,alacritty-direct extra/alacritty.info -o %{buildroot}%{_datadir}/terminfo
install -p -D -m644 extra/completions/alacritty.bash %{buildroot}%{_datadir}/bash-completion/completions/alacritty
install -p -D -m644 extra/completions/_alacritty %{buildroot}%{_datadir}/zsh/site-functions/_alacritty
install -p -D -m644 extra/completions/alacritty.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/alacritty.fish
install -p -D -m644 extra/alacritty.man %{buildroot}%{_mandir}/man1/alacritty.1

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/alacritty.desktop

%files
%{_bindir}/alacritty
%{_datadir}/applications/alacritty.desktop
%{_datadir}/pixmaps/Alacritty.svg
%{_datadir}/alacritty/alacritty.yml
%{_datadir}/terminfo/a/alacritty*
%{_datadir}/bash-completion/completions/alacritty
%{_datadir}/zsh/site-functions/_alacritty
%{_datadir}/fish/vendor_completions.d/alacritty.fish
%{_mandir}/man1/alacritty.1*

%changelog
* Wed Jun 24 2020 Nick Black <dankamongmen@gmail.com> - 0.4.3-1
- Initial packaging for Fedora 33 (with input from pschyska)
