%include	/usr/lib/rpm/macros.perl
Summary:	Bruteforce Exploit Detector
Summary(pl):	"Brutalny" wykrywacz exploit�w
Name:		bed
Version:	0.42
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.snake-basket.de/bed/%{name}-%{version}.tar.bz2
# Source0-md5:	b2903345f3db03f5a4ef580a3f829486
URL:		http://www.snake-basket.de/bed/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of scripts to automatically test implementations
of different protocols for buffer overflows and / or format string
vulnerabilities, by sending a lot of long strings to a server in a
boring, stupid way... :)

%description -l pl
Jest to kolekcja skrypt�w do automatycznego testowania implementacji
r�nych protoko��w pod k�tem przepe�nienia bufor�w i/lub b��d�w typu
format string, poprzez wysy�anie ogromnej ilo�ci d�ugich ci�g�w znak�w
w bardzo nudny, g�upi spos�b... :)

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/bedmod,%{_bindir}}

install bed.pl		$RPM_BUILD_ROOT%{_bindir}
install bedmod/*.pm	$RPM_BUILD_ROOT%{perl_vendorlib}/bedmod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{CHANGES,FAQ,HOWTO,TODO,dummy.pm} README
%attr(755,root,root) %{_bindir}/*.pl
%attr(755,root,root) %{perl_vendorlib}/bedmod/*.pm
