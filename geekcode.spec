Summary:	Generates your geek code.
Summary(pl):	Generuje Twój geek code.
Name:		geekcode
Version:	1.7
Release:	1
License:	GPL
Group:		Applications/Games
URL:		http://geekcode.sourceforge.net
Source0:	http://download.sourceforge.net/geekcode/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will generate a geek code block for you by simply
choosing which codes suit you from the screen.

%description -l pl
Program generuje blok geek code dla Ciebie przez proste wybieranie zestawu
kodów z ekranu.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D geekcode $RPM_BUILD_ROOT/%{_bindir}/geekcode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README geekcode.txt
%attr(755,root,root) %{_bindir}/*
