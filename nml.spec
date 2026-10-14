Summary:	A tool to compile nml files to grf or nfo files
Name:		nml
Version:	0.9.0
Release:	2
License:	GPLv2+
Group:		Graphics
Url:		https://github.com/OpenTTD/nml
Source0:	https://github.com/OpenTTD/nml/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(ply)
BuildRequires:	python%{pyver}dist(pillow)
Requires:	python%{pyver}dist(pillow)

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
%{python_sitearch}/%{name}-*.dist-info
%{python_sitearch}/%{name}/
%{python_sitearch}/nml_lz77.cpython-*.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

#handle docs in files section
rm -rf %{buildroot}%{_docdir}

#man pages
install -Dpm644 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#unpackaged files
rm -rf %{buildroot}%{python_sitelib}/{easy-install.pth,site.py}

