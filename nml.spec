%define rev r5242-f6a3ae1163ab

Summary:	A tool to compile nml files to grf or nfo files
Name:		nml
Version:	0.3.1
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://dev.openttdcoop.org/projects/nml
Source0:	http://bundles.openttdcoop.org/nml/releases/%{version}/%{name}-%{version}.%{rev}.tar.gz
BuildRequires:	python2-distribute
Requires:	python2-ply
Requires:	python2-imaging
Requires:	python2-pkg-resources
BuildArch:	noarch

%description
A tool to compile nml files to grf and/or nfo files.

NML is a meta-language that aims to be a lot simpler to learn and use than nfo.

%files
%doc docs/* examples/
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1.*
%{python2_sitelib}/%{name}-%{version}*-py*.egg/

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}.%{rev}

%build
PYTHONDONTWRITEBYTECODE= python2 setup.py build

%install
mkdir -p %{buildroot}%{python2_sitelib}

export PYTHONPATH=%{buildroot}%{python2_sitelib}
PYTHONDONTWRITEBYTECODE= python2 setup.py install --prefix %{buildroot}%{_prefix}

#handle docs in files section
rm -rf %{buildroot}%{_defaultdocdir}

#man pages
install -Dpm655 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#unpackaged files
rm -rf docs/nmlc.1
rm -rf %{buildroot}%{python2_sitelib}/{easy-install.pth,site.py,site.pyc}
