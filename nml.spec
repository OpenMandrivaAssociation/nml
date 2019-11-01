Summary:	A tool to compile nml files to grf or nfo files
Name:		nml
Version:	0.4.5
Release:	2
License:	GPLv2+
Group:		Graphics
Url:		https://github.com/OpenTTD/nml
Source0:	http://bundles.openttdcoop.org/nml/releases/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:	python-distribute
BuildRequires:	python-imaging
BuildRequires:	python-ply
Requires:	python-ply
Requires:	python-imaging
Requires:	python-pkg-resources

%description
A tool to compile nml files to grf and/or nfo files.

NML is a meta-language that aims to be a lot simpler to learn and use than nfo.

%files
%doc examples/
%doc docs/changelog.txt docs/index.html docs/readme.txt docs/license.txt
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1.*
%{python3_sitearch}/%{name}-*-py%{py3ver}.egg-info/
%{python3_sitearch}/%{name}/
%{python3_sitearch}/nml_lz77.cpython-*.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
PYTHONDONTWRITEBYTECODE= python3 setup.py build

%install
mkdir -p %{buildroot}%{python3_sitelib}

PYTHONDONTWRITEBYTECODE= python3 setup.py install --root %{buildroot} --prefix %{_prefix}

#handle docs in files section
rm -rf %{buildroot}%{_defaultdocdir}

#man pages
install -Dpm655 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#unpackaged files
rm -rf %{buildroot}%{python3_sitelib}/{easy-install.pth,site.py,site.pyc}
