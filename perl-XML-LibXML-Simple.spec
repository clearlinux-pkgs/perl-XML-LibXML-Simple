#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-LibXML-Simple
Version  : 0.99
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/XML-LibXML-Simple-0.99.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/XML-LibXML-Simple-0.99.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-libxml-simple-perl/libxml-libxml-simple-perl_0.99-1.debian.tar.xz
Summary  : 'XML::LibXML based XML::Simple clone'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-LibXML-Simple-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::LibXML)
BuildRequires : perl(XML::SAX::Exception)

%description
=   Generated on Wed Nov  8 10:39:34 2017 by OODoc 2.02
There are various ways to install this module:

%package dev
Summary: dev components for the perl-XML-LibXML-Simple package.
Group: Development
Provides: perl-XML-LibXML-Simple-devel = %{version}-%{release}

%description dev
dev components for the perl-XML-LibXML-Simple package.


%package license
Summary: license components for the perl-XML-LibXML-Simple package.
Group: Default

%description license
license components for the perl-XML-LibXML-Simple package.


%prep
%setup -q -n XML-LibXML-Simple-0.99
cd ..
%setup -q -T -D -n XML-LibXML-Simple-0.99 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/XML-LibXML-Simple-0.99/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-LibXML-Simple
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-XML-LibXML-Simple/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/XML/LibXML/Simple.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/LibXML/Simple.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::LibXML::Simple.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-LibXML-Simple/deblicense_copyright
