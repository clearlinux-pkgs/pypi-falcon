#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-falcon
Version  : 3.1.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/36/53/4fd90c6c841bc2e4be29ab92c65e5406df9096c421f138bef9d95d43afc9/falcon-3.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/36/53/4fd90c6c841bc2e4be29ab92c65e5406df9096c421f138bef9d95d43afc9/falcon-3.1.0.tar.gz
Summary  : The ultra-reliable, fast ASGI+WSGI framework for building data plane APIs at scale.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-falcon-bin = %{version}-%{release}
Requires: pypi-falcon-license = %{version}-%{release}
Requires: pypi-falcon-python = %{version}-%{release}
Requires: pypi-falcon-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(pecan)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. raw:: html
<a href="https://falconframework.org" target="_blank">
<img
src="https://raw.githubusercontent.com/falconry/falcon/master/logo/banner.jpg"
alt="Falcon web framework logo"
style="width:100%"
>
</a>

%package bin
Summary: bin components for the pypi-falcon package.
Group: Binaries
Requires: pypi-falcon-license = %{version}-%{release}

%description bin
bin components for the pypi-falcon package.


%package license
Summary: license components for the pypi-falcon package.
Group: Default

%description license
license components for the pypi-falcon package.


%package python
Summary: python components for the pypi-falcon package.
Group: Default
Requires: pypi-falcon-python3 = %{version}-%{release}

%description python
python components for the pypi-falcon package.


%package python3
Summary: python3 components for the pypi-falcon package.
Group: Default
Requires: python3-core
Provides: pypi(falcon)
Requires: pypi(pecan)

%description python3
python3 components for the pypi-falcon package.


%prep
%setup -q -n falcon-3.1.0
cd %{_builddir}/falcon-3.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649744254
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-falcon
cp %{_builddir}/falcon-3.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-falcon/2b8b815229aa8a61e483fb4ba0588b8b6c491890
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/falcon-bench
/usr/bin/falcon-inspect-app
/usr/bin/falcon-print-routes

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-falcon/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
