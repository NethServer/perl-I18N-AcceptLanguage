Name:           perl-I18N-AcceptLanguage
Version:        1.04
Release:        1%{?dist}
Summary:        Matches language preference to available languages
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/I18N-AcceptLanguage/
Source0:        http://www.cpan.org/authors/id/C/CG/CGILMORE/I18N-AcceptLanguage-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.45
BuildRequires:  perl(CPAN)
Requires:       perl(Test::More) >= 0.45
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
I18N::AcceptLanguage matches language preference to available languages per
rules defined in RFC 2616, section 14.4: HTTP/1.1 - Header Field
Definitions - Accept-Language.

%prep
%setup -q -n I18N-AcceptLanguage-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue May 05 2015 Davide Principi <davide.principi@nethesis.it> 1.04-1
- Specfile autogenerated by cpanspec 1.78.
