#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Exporter
%define		pnam	Easy
Summary:	Exporter::Easy - takes the drudgery out of exporting symbols
Summary(pl.UTF-8):   Exporter::Easy - przejmujący harówkę eksportowania symboli
Name:		perl-Exporter-Easy
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	16f44909db2e85578ed2f26db490312b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exporter::Easy gets rid of the drudgery of exporting symbols allowing
you to eliminate those bits of code that exists in every single module
that uses Exporter.

It also allows you to define tags in terms of other tags and you no
longer have to worry about filling in @EXPORT_OK.

%description -l pl.UTF-8
Exporter::Easy pozwala pozbyć się harówki związanej z eksportowaniem
symboli, pozwalając wyeliminować te fragmenty kodu, istniejące w
każdym module używającym Exportera.

Pozwala także na definiowanie znaczników w kontekście innych
znaczników, więc nie trzeba się już martwić o wypełnianie @EXPORT_OK.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -pi -e "s/INSTALLDIRS => 'perl',//" Makefile.PL
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
