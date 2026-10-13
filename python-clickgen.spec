Name:		python-clickgen
Version:	2.2.5
Release:	4
Source0:	https://files.pythonhosted.org/packages/source/c/clickgen/clickgen-%{version}.tar.gz
Summary:	The hassle-free cursor building toolbox.
URL:		https://pypi.org/project/clickgen/
License:	MIT
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
The hassle-free cursor building toolbox.

%files
%license LICENSE
%{_bindir}/clickgen
%{_bindir}/ctgen
%{py_sitedir}/clickgen
%{py_sitedir}/clickgen-*.*-info
