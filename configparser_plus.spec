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
echo "Nothing to do"

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%attr(0644,root,root) %{_prefix}/lib/python2.7/site-packages/configparser_plus-1.0-py2.7.egg-info
%attr(0644,root,root) %{_prefix}/lib/python2.7/site-packages/configparser_plus.py
%attr(0644,root,root) %{_prefix}/lib/python2.7/site-packages/configparser_plus.pyc
%attr(0644,root,root) %{_prefix}/lib/python2.7/site-packages/configparser_plus.pyo

%changelog

