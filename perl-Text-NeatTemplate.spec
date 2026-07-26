%define upstream_name    Text-NeatTemplate
Name:       perl-%{upstream_name}
Version:    0.11
Release:    4

Summary:    A fast, middleweight template engine

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(JSON::PP)
BuildArch:     noarch

%description
This module provides a simple, middleweight but fast template engine,
for when you need speed rather than complex features, yet need more features
than simple variable substitution.

%prep
%setup -q -n %{upstream_name}-%{version}
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



