Summary:	Generates your geek code
Summary(pl):	Program generuj±cy geek code
Name:		geekcode
Version:	1.7.3
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/geekcode/%{name}-%{version}.tar.gz
# Source0-md5:	b794916a8875f71f1442f6e70432d6de
URL:		http://geekcode.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will generate a geek code block for you by simply
choosing which codes suit you from the screen.

%description -l pl
Program generuje blok geek code dla u¿ytkownika poprzez proste
wybieranie pasuj±cych kodów z ekranu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D geekcode $RPM_BUILD_ROOT%{_bindir}/geekcode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README geekcode.txt
%attr(755,root,root) %{_bindir}/*
