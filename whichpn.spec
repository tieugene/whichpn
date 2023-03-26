%global module whicpn
Name:		python-%{module}
Version:	0.0.1
Release:	1%{?dist}
License:	GLPv3
Summary:	Which phone number
URL:		https://github.com/tieugene/%{module}
Source0:	%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  pyproject-rpm-macros
# python3-wheel
BuildRequires:	%{py3_dist wheel}
# python3-django
BuildRequires:	%{py3_dist django}

%description
%{summary}.


%package -n python3-%{module}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{module}}

%description -n python3-%{module}
%{summary}.


%prep
%autosetup -n %{module}-%{version}
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module}


%files -n python3-%{module} -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Sun Mar 26 2023 TI_Eugene <ti.eugene@gmail.com> - 0.0.1-1
- Initial packaging
