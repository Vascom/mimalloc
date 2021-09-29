%undefine __cmake_in_source_build

Name:           mimalloc
Version:        2.0.2
Release:        2%{?dist}
Summary:        A general purpose allocator with excellent performance

License:        MIT
URL:            https://github.com/microsoft/mimalloc
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/microsoft/mimalloc/pull/463
Patch0:         mimalloc-install-dirs.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
mimalloc (pronounced "me-malloc")
is a general purpose allocator with excellent performance characteristics.
Initially developed by Daan Leijen for the run-time systems.

%package devel
Summary:        Development environment for %name
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development package for mimalloc.

%prep
%autosetup -p1


%build
%cmake \
    -DMI_BUILD_OBJECT=OFF \
    -DMI_OVERRIDE=OFF \
    -DMI_INSTALL_TOPLEVEL=ON \
    -DMI_BUILD_STATIC=OFF \
    -DMI_BUILD_TESTS=OFF \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc readme.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_includedir}/*


%changelog
* Wed Sep 29 2021 Vasiliy Glazov <vascom2@gmail.com> - 2.0.2-2
- Clean spec to follow packaging guidelines

* Wed Sep 29 2021 Vasiliy Glazov <vascom2@gmail.com> - 2.0.2-1
- Initial packaging for Fedora
