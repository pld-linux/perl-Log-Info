#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Log
%define		pnam	Info
Summary:	Log::Info - single interface for log output
Summary(pl.UTF-8):   Log::Info - pojedynczy interfejs do tworzenia logów
Name:		perl-Log-Info
Version:	1.19
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	80c2e6320e22e25310790d8a34cc65f6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Class-MethodMaker
BuildRequires:	perl-Term-ProgressBar
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

%build
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
%{perl_vendorlib}/Log/Info.pm
%dir %{perl_vendorlib}/Log/Info
%{perl_vendorlib}/Log/Info/Fork.pm
%{_mandir}/man3/*
