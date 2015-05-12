%define rev r5242-f6a3ae1163ab

Name:		nml
Summary:	A tool to compile nml files to grf or nfo files
Version:	0.3.1
Release:	2
License:	GPLv2+
Group:		Graphics
URl:		http://dev.openttdcoop.org/projects/nml
Source0:	http://bundles.openttdcoop.org/nml/releases/LATEST/%{name}-%{version}.%{rev}.tar.gz
# patch for OPENTTD_RECOLOUR used in opengfx
# we cant up to 0.4.1 on 2014 as it requires py3
Patch1:		nml-0.3.1-openttd_recolour.patch
BuildArch:	noarch
BuildRequires:	python-setuptools
Requires:	python-ply
Requires:	python-imaging
Requires:	python-pkg-resources

%description
A tool to compile nml files to grf and/or nfo files.

NML is a meta-language that aims to be a lot simpler to learn and use than nfo.

%prep
%setup -qn %{name}-%{version}.%{rev}
%apply_patches

%build
PYTHONDONTWRITEBYTECODE= python setup.py build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{python_sitelib}

export PYTHONPATH=%{buildroot}%{python_sitelib}
PYTHONDONTWRITEBYTECODE= python setup.py install --prefix %{buildroot}%{_prefix}

#handle docs in files section
rm -rf %{buildroot}%{_defaultdocdir}

#man pages
install -Dpm655 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#unpackaged files
rm -rf docs/nmlc.1
rm -rf %{buildroot}%{python_sitelib}/{easy-install.pth,site.py,site.pyc}

%files
%doc docs/* examples/
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1.*
%{python_sitelib}/%{name}-%{version}*-py*.egg/

