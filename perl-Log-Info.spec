
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define pnam	Info
Summary:	Log::Info - Single interface for log output
Name:		perl-Log-Info
Version:	1.19
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	80c2e6320e22e25310790d8a34cc65f6
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Log::Info is intended to be a single interface for all logging 
action.  Each instance of Log::Info is intended to be an output 
for a particular type of log; some defaults are provided, and 
custom ones may be generated.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Log/Info.pm
%dir %{perl_vendorlib}/Log/Info
%{perl_vendorlib}/Log/Info/Fork.pm
%{_mandir}/man3/*
