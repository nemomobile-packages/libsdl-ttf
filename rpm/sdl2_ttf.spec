Summary: Simple DirectMedia Layer - Sample TrueType Font Library
Name: SDL2_ttf
Version: 2.0.12
Release: 1
Source: http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
URL: http://www.libsdl.org/projects/SDL_ttf/
License: zlib
Group: Applications/Multimedia
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(freetype2)

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package devel
Summary: Simple DirectMedia Layer - Sample TrueType Font Library (Development)
Group: Development/Libraries
Requires: %{name}

%description devel
This library allows you to use TrueType fonts to render text in SDL
applications.

%prep
%setup -q

%build
./autogen.sh
%configure
make

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*

