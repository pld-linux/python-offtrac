Summary:	Trac xmlrpc library
Name:		python-offtrac
Version:	0.0.3
Release:	1
License:	GPL v2+
Group:		Development/Languages
URL:		http://fedorahosted.org/offtrac
# No tarballs are made, generate them from scm
# git clone git://git.fedorahosted.org/git/offtrac
# cd offtrac
# git checkout -b tarball %{version}
# python setup.py sdist --formats=bztar
Source0:	offtrac-%{version}.tar.bz2
# Source0-md5:	3e4cdcbf50ba492b93748d2e08cbbc9c
BuildRequires:	python-devel
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
There is the offtrac Python library which offers the TracServer class.
This object is how one interacts with a Trac instance via xmlrpc.

%prep
%setup -q -n offtrac-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
%endif
