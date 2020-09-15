Summary:	A tool to compile nml files to grf or nfo files
Name:		nml
Version:	0.5.3
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		https://github.com/OpenTTD/nml
Source0:	https://github.com/OpenTTD/nml/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:	python-distribute
BuildRequires:	python-imaging
BuildRequires:	python-ply
BuildRequires:	python-pillow
BuildRequires:	python-setuptools
Requires:	python-ply
Requires:	python-imaging
Requires:	python-pkg-resources
Requires:	python-pillow

%description
A tool to compile nml files to grf and/or nfo files.

NML is a meta-language that aims to be a lot simpler to learn and use than nfo.

%files
%license LICENSE
%doc README*
%doc examples/
%doc docs/changelog.txt
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1*
%{python_sitearch}/%{name}-*-py%{python_version}.egg-info/
%{python_sitearch}/%{name}/
%{python_sitearch}/nml_lz77.cpython-*.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%py3_build

%install
%py3_install

#handle docs in files section
rm -rf %{buildroot}%{_docdir}

#man pages
install -Dpm644 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#unpackaged files
rm -rf %{buildroot}%{python_sitelib}/{easy-install.pth,site.py}

