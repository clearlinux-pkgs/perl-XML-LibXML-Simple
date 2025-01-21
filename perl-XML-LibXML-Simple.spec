#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-XML-LibXML-Simple
Version  : 1.01
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/XML-LibXML-Simple-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/XML-LibXML-Simple-1.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-libxml-simple-perl/libxml-libxml-simple-perl_0.99-1.debian.tar.xz
Summary  : 'XML::LibXML alternative to XML::Simple::XMLin()'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-LibXML-Simple-license = %{version}-%{release}
Requires: perl-XML-LibXML-Simple-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::LibXML)
BuildRequires : perl(XML::SAX::Exception)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=   Generated on Wed Jan 15 11:56:02 2020 by OODoc 2.02
There are various ways to install this module:

%package dev
Summary: dev components for the perl-XML-LibXML-Simple package.
Group: Development
Provides: perl-XML-LibXML-Simple-devel = %{version}-%{release}
Requires: perl-XML-LibXML-Simple = %{version}-%{release}

%description dev
dev components for the perl-XML-LibXML-Simple package.


%package license
Summary: license components for the perl-XML-LibXML-Simple package.
Group: Default

%description license
license components for the perl-XML-LibXML-Simple package.


%package perl
Summary: perl components for the perl-XML-LibXML-Simple package.
Group: Default
Requires: perl-XML-LibXML-Simple = %{version}-%{release}

%description perl
perl components for the perl-XML-LibXML-Simple package.


%prep
%setup -q -n XML-LibXML-Simple-1.01
cd %{_builddir}
tar xf %{_sourcedir}/libxml-libxml-simple-perl_0.99-1.debian.tar.xz
cd %{_builddir}/XML-LibXML-Simple-1.01
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/XML-LibXML-Simple-1.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-LibXML-Simple
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-XML-LibXML-Simple/f799fb75028ed1c3f97c2836c4d0d9defb473bd7 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::LibXML::Simple.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-LibXML-Simple/f799fb75028ed1c3f97c2836c4d0d9defb473bd7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
