%include	/usr/lib/rpm/macros.perl
Summary:	Bruteforce Exploit Detector
Summary(pl):	"Brutalny" wykrywacz exploitów
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
Jest to kolekcja skryptów do automatycznego testowania implementacji
ró¿nych protoko³ów pod k±tem przepe³nienia buforów i/lub b³êdów typu
format string, poprzez wysy³anie ogromnej ilo¶ci d³ugich ci±gów znaków
w bardzo nudny, g³upi sposób... :)

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
