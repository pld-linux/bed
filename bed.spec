%include	/usr/lib/rpm/macros.perl
Summary:	Bruteforce Exploit Detector
Summary(pl):	"Brutalny" wykrywacz exploit�w
Name:		bed
Version:	0.3
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.kryptocrew.de/snakebyte/bed/%{name}-%{version}.zip
URL:		http://www.kryptocrew.de/snakebyte/bed.html
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
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_sitelib}/mod,%{_bindir}}

install bed.pl		$RPM_BUILD_ROOT%{_bindir}
install mod/*.pm	$RPM_BUILD_ROOT%{perl_sitelib}/mod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{CHANGES,TODO,FAQ,dummy.pm} README
%attr(755,root,root) %{_bindir}/*.pl
%{perl_sitelib}/mod/*.pm
