Name:		nml
Summary:	A tool to compile nml files to grf or nfo files
Version:	0.2.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphics
URl:		http://dev.openttdcoop.org/projects/nml
Source0:	http://bundles.openttdcoop.org/nml/releases/LATEST/%{name}-%{version}.src.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
Requires:	python-ply
Requires:	python-imaging

%description
A tool to compile nml files to grf and/or nfo files.

NML is a meta-language that aims to be a lot simpler to learn and use than nfo.

%prep
%setup -q

%build
PYTHONDONTWRITEBYTECODE= python setup.py build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{python_sitelib}

export PYTHONPATH=%{buildroot}%{python_sitelib}
PYTHONDONTWRITEBYTECODE= python setup.py install --prefix %{buildroot}%{_prefix}

#handle docs in files section
%__rm -rf %{buildroot}%{_defaultdocdir}

#man pages
%__install -Dpm655 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#unpackaged files
%__rm -rf docs/nmlc.1
%__rm -rf %{buildroot}%{python_sitelib}/{easy-install.pth,site.py,site.pyc}

%clean
%__rm -rf %{buildroot}

%files
%doc docs/* examples/
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1.*
%{python_sitelib}/%{name}-%{version}-py*.egg/

