%define upstream_name    Text-NeatTemplate
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A fast, middleweight template engine
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build::Compat)
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Text


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 405712
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.08-4mdv2009.0
+ Revision: 258618
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.08-3mdv2009.0
+ Revision: 246635
- rebuild
- fix summary-not-capitalized
- fix summary-ended-with-dot

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.1
+ Revision: 138068
- import perl-Text-NeatTemplate


* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.1
- first mdv release
