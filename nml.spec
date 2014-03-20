Summary:	A tool to compile nml files to grf or nfo files
Name:		nml
Version:	0.2.4
Release:	2
License:	GPLv2+
Group:		Graphics
Url:		http://dev.openttdcoop.org/projects/nml
Source0:	http://bundles.openttdcoop.org/nml/releases/LATEST/%{name}-%{version}.src.tar.gz
BuildRequires:	python-setuptools
Requires:	python-ply
Requires:	python-imaging
Requires:	python-pkg-resources
BuildArch:	noarch

%description
A tool to compile nml files to grf and/or nfo files.

NML is a meta-language that aims to be a lot simpler to learn and use than nfo.

%files
%doc docs/* examples/
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1.*
%{python_sitelib}/%{name}-%{version}-py*.egg/

#----------------------------------------------------------------------------

%prep
%setup -q

%build
PYTHONDONTWRITEBYTECODE= python setup.py build

%install
mkdir -p %{buildroot}%{python_sitelib}

export PYTHONPATH=%{buildroot}%{python_sitelib}
PYTHONDONTWRITEBYTECODE= python setup.py install --prefix %{buildroot}%{_prefix}

#handle docs in files section
rm -rf %{buildroot}%{_defaultdocdir}

#man pages
install -Dpm655 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#unpackaged files
rm -rf docs/nmlc.1
rm -rf %{buildroot}%{python_sitelib}/{easy-install.pth,site.py,site.pyc}


