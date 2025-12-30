Name:		python-clickgen
Version:	2.2.5
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/c/clickgen/clickgen-%{version}.tar.gz
Summary:	The hassle-free cursor building toolbox.
URL:		https://pypi.org/project/clickgen/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
The hassle-free cursor building toolbox.

%files
%{_bindir}/clickgen
%{_bindir}/ctgen
%{py_sitedir}/clickgen
%{py_sitedir}/clickgen-*.*-info
