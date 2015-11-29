Summary:	ASCII art to image converter
Summary(pl.UTF-8):	Konwerter ASCII art do obrazków
Name:		python-aafigure
Version:	0.5
Release:	1
License:	BSD
Group:		Applications
Source0:	http://pypi.python.org/packages/source/a/aafigure/aafigure-%{version}.tar.gz
# Source0-md5:	5322888a21eb0bb2e749fbf98eddf574
URL:		https://launchpad.net/aafigure/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Suggests:	python-PIL >= 1.1.7
Suggests:	python-ReportLab
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a module "aafigure", that can be used from other
programs, and a command line tool "aafigure".

%description -l pl.UTF-8
Ten pakiet dostarcza moduł "aafigure", który może być wykorzystywany z
poziomu innych programów, oraz działające z linii poleceń narzędzie
"aafigure".

%prep
%setup -q -n aafigure-%{version}

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
%doc CHANGES.txt LICENSE.txt README.txt
%attr(755,root,root) %{_bindir}/aafigure
%{py_sitescriptdir}/aafigure
%{py_sitescriptdir}/aafigure-%{version}-py*.egg-info
