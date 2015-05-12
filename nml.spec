Summary:	A tool to compile nml files to grf or nfo files
Name:		nml
Version:	0.4.1
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://dev.openttdcoop.org/projects/nml
Source0:	http://bundles.openttdcoop.org/nml/releases/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	python-distribute
BuildRequires:	python-imaging
BuildRequires:	python-ply
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
%{python3_sitelib}/%{name}-%{version}*-py*.egg/

#----------------------------------------------------------------------------

%prep
%setup -q

%build
PYTHONDONTWRITEBYTECODE= python3 setup.py build

%install
mkdir -p %{buildroot}%{python3_sitelib}

export PYTHONPATH=%{buildroot}%{python3_sitelib}
PYTHONDONTWRITEBYTECODE= python3 setup.py install --prefix %{buildroot}%{_prefix}

#handle docs in files section
rm -rf %{buildroot}%{_defaultdocdir}

#man pages
install -Dpm655 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#unpackaged files
rm -rf docs/nmlc.1
rm -rf %{buildroot}%{python3_sitelib}/{easy-install.pth,site.py,site.pyc}
