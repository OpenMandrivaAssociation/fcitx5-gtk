Summary:    Fcitx5 gtk im module and glib dbus client library
Name:       fcitx5-gtk
Version:    5.1.4
Release:    1
Source0:    https://github.com/fcitx/fcitx5-gtk/archive/refs/tags/%{version}.tar.gz
URL:        https://github.com/fcitx/fcitx5-gtk
License:    LGPLv2
Group:      System/Internationalization
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)

%description
Fcitx5 gtk im module and glib based dbus client library.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   fcitx5-devel%{?_isa}

%description devel
Development files for %{name}

%package -n %{name}2
Summary:    Fcitx5 gtk 2.x module
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}2
Fcitx5 gtk 2.x module.

%package -n %{name}3
Summary:    Fcitx5 gtk 3.x module
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}3
Fcitx5 3.x module.

%package -n %{name}4
Summary:    Fcitx5 gtk 4.x module
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}4
Fcitx5 gtk 4.x module.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/libFcitx5GClient.so
%{_libdir}/libFcitx5GClient.so.*
%{_libdir}/girepository-1.0/FcitxG-1.0.typelib

%files devel
%{_includedir}/Fcitx5/GClient/fcitx-gclient/fcitxgclient.h
%{_includedir}/Fcitx5/GClient/fcitx-gclient/fcitxgwatcher.h
%{_libdir}/cmake/Fcitx5GClient/Fcitx5GClientConfig.cmake
%{_libdir}/cmake/Fcitx5GClient/Fcitx5GClientConfigVersion.cmake
%{_libdir}/cmake/Fcitx5GClient/Fcitx5GClientTargets-relwithdebinfo.cmake
%{_libdir}/cmake/Fcitx5GClient/Fcitx5GClientTargets.cmake
%{_libdir}/pkgconfig/Fcitx5GClient.pc
%{_datadir}/gir-1.0/FcitxG-1.0.gir

%files -n %{name}2
%{_bindir}/fcitx5-gtk2-immodule-probing
%{_libdir}/gtk-2.0/2.10.0/immodules/im-fcitx5.so

%files -n %{name}3
%{_bindir}/fcitx5-gtk3-immodule-probing
%{_libdir}/gtk-3.0/3.0.0/immodules/im-fcitx5.so

%files -n %{name}4
%{_bindir}/fcitx5-gtk4-immodule-probing
%{_libdir}/gtk-4.0/4.0.0/immodules/libim-fcitx5.so
