%define upstream_name    Text-NeatTemplate
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    A fast, middleweight template engine

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(JSON::PP)
BuildArch:     noarch

%description
This module provides a simple, middleweight but fast template engine,
for when you need speed rather than complex features, yet need more features
than simple variable substitution.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find . -type f | xargs chmod +w

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install destdir=%{buildroot}

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Text



