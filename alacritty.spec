Name:          alacritty
Version:       0.5.0
Release:       1%{?dist}
Summary:       A fast OpenGL-based terminal emulator
License:       ASL 2.0
URL:           https://github.com/alacritty/alacritty
VCS:           https://github.com/alacritty/alacritty.git
Source0:       https://github.com/alacritty/%{name}/archive/v%{version}.tar.gz

ExclusiveArch: %{rust_arches}

BuildRequires: rust-packaging
BuildRequires: rust >= 1.36.0
BuildRequires: cargo
BuildRequires: cmake
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(xcb)
BuildRequires: desktop-file-utils
BuildRequires: %{python3}
BuildRequires: (crate(clap/default) >= 2.0.0 with crate(clap/default) < 3.0.0)
BuildRequires: (crate(copypasta/default) >= 0.7.0 with crate(copypasta/default) < 1.0.0)
BuildRequires: (crate(crossfont/default) >= 0.1.0 with crate(crossfont/default) < 1.0.0)
BuildRequires: (crate(env_logger/default) == 0.7.1)
BuildRequires: (crate(fnv/default) >= 1.0.0)
BuildRequires: (crate(glutin_egl_sys/default) >= 0.1.5 with crate(glutin_egl_sys/default) < 1.0.0)
BuildRequires: (crate(log/std) >= 0.4 with crate(log/std) < 1.0.0)
BuildRequires: (crate(notify/default) >= 4.0.0)
BuildRequires: (crate(parking_lot/default) >= 0.10.2)
BuildRequires: (crate(serde/derive) >= 1.0.0)
BuildRequires: (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0)
BuildRequires: (crate(serde_yaml/default) >= 0.8.0 with crate(serde_yaml/default) < 1.0.0)
BuildRequires: (crate(time/default) >= 0.1.40)
BuildRequires: (crate(unicode-width/default) >= 0.1.0)
BuildRequires: (crate(urlocator/default) >= 0.1.4)

%description
Alacritty is an OpenGL-based terminal emulator focused on performance. It
supports TrueColor and Wayland.

%prep
%autosetup -n alacritty-%{version_no_tilde}
%cargo_prep

%build
%cargo_build -a

%install
%cargo_install -a
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

%triggerun -- bash-completion
[ $2 -gt 0 ] && exit 0
rm -f %{bash_completion_path}/alacritty

%triggerun -- zsh
[ $2 -gt 0 ] && exit 0
rm -f %{zsh_completion_path}/_alacritty

%triggerun -- fish
[ $2 -gt 0 ] && exit 0
rm -f %{fish_completion_path}/alacritty.fish

%changelog
* Wed Jun 24 2020 Nick Black <dankamongmen@gmail.com> - 0.4.3-1
- Initial packaging for Fedora 33 (with input from pschyska)
