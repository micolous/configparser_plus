
%global eggpath $RPM_BUILD_ROOT%{_prefix}/lib/python2.7/site-packages/

Name:		configparser_plus
Version:	1.0.0
Release:	1%{?dist}
Summary:	An extension library to Python's SafeConfigParser.

BuildArch: noarch
Group:		System Environment/Daemons
License:	LGPLv3
URL:		https://github.com/micolous/configparser_plus
#Source0:	
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	python, python-setuptools
Requires:	python

%description
An extension library to Python's SafeConfigParser to provide defaults as a two dimensional dict, making it a little bit easier to use.

%prep
%setup -q -n %{name}


%build
python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{eggpath}
export PYTHONPATH=%{eggpath}
python setup.py install --prefix=$RPM_BUILD_ROOT%{_prefix}
#Setup.py leaves a bunch of shit left over. ... we need to clean it up.
#rm %{eggpath}/easy-install.pth
#rm %{eggpath}/site.py*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%attr(0644,root,root) %{_prefix}/lib/python2.7/site-packages/configparser_plus-1.0-py2.7.egg-info
%attr(0644,root,root) %{_prefix}/lib/python2.7/site-packages/configparser_plus.py
%attr(0644,root,root) %{_prefix}/lib/python2.7/site-packages/configparser_plus.pyc
%attr(0644,root,root) %{_prefix}/lib/python2.7/site-packages/configparser_plus.pyo

%changelog

