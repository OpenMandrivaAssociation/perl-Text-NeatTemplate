%define module   Text-NeatTemplate
%define version    0.08
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A fast, middleweight template engine
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Module::Build::Compat)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module provides a simple, middleweight but fast template engine,
for when you need speed rather than complex features, yet need more features
than simple variable substitution.

%prep
%setup -q -n %{module}-%{version} 
find . -type f | xargs chmod +w

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Text

