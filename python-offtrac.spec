%define 	module	offtrac
Summary:	Trac xmlrpc library
Name:		python-%{module}
Version:	0.0.3
Release:	4
License:	GPL v2+
Group:		Development/Languages
URL:		http://fedorahosted.org/offtrac
BuildRequires:	rpmbuild(macros) >= 1.710
# No tarballs are made, generate them from scm
# git clone git://git.fedorahosted.org/git/offtrac
# cd offtrac
# git checkout -b tarball %{version}
# python setup.py sdist --formats=bztar
Source0:	%{module}-%{version}.tar.bz2
# Source0-md5:	3e4cdcbf50ba492b93748d2e08cbbc9c
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
There is the offtrac Python library which offers the TracServer class.
This object is how one interacts with a Trac instance via xmlrpc.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
%endif
