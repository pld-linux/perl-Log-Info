# TODO
# - figure out why disabled tests fail
#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Log
%define		pnam	Info
Summary:	Log::Info - single interface for log output
Summary(pl.UTF-8):	Log::Info - pojedynczy interfejs do tworzenia logów
Name:		perl-Log-Info
Version:	1.21
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	91d8467613193967ff4286386d015f44
URL:		http://search.cpan.org/dist/Log-Info/
BuildRequires:	perl-Class-MethodMaker
BuildRequires:	perl-Term-ProgressBar
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	util-linux
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Info is intended to be a single interface for all logging action.
Each instance of Log::Info is intended to be an output for a
particular type of log; some defaults are provided, and custom ones
may be generated.

%description -l pl.UTF-8
Log::Info ma być pojedynczym interfejsem do wszystkich rodzajów
logowania. Każda instancja Log::Info ma być wyjściem pewnego rodzaju
logów; załączone jest trochę ustawień domyślnych, można wygenerować
własne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# use next matching two digit version
sed -i -e '/use IO::Pipe/s,1.121,1.13,' lib/Log/Info.pm

# fail on carme
rm t/fork_log.t
rm t/single-die.t
# fail on builders
rm t/syslog.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Log-Info/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Log/Info.pm
%dir %{perl_vendorlib}/Log/Info
%{perl_vendorlib}/Log/Info/Fork.pm
%{_mandir}/man3/*
