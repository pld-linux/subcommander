Summary:	Qt based multiplatform subversion client
Summary(pl):	Wieloplatformowy klient subversion oparty na Qt
Name:		subcommander
Version:	0.14.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://subcommander.tigris.org/files/documents/1759/28737/%{name}-%{version}-src.tgz
# Source0-md5:	edc245c6be8f5bffd128df36e13d2692
URL:		http://subcommander.tigris.org/
BuildRequires:	boost-devel
BuildRequires:	qt-devel >= 3.2
BuildRequires:	sed >= 4.0
BuildRequires:	subversion-devel >= 1.2
Requires:	submerge = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt based multiplatform subversion client.

%description -l pl
Wieloplatformowy klient subversion oparty na Qt.

%package -n submerge
Summary:	submerge - visual diff and merge tool for text files
Summary(pl):	submerge - wizualne narzêdzie do porównywania i ³±czenia plików tekstowych
Group:		X11/Applications

%description -n submerge
submerge is visual diff and merge tool for text files.

%description -n submerge -l pl
submerge to wizualne narzêdzie do porównywania i ³±czenia plików
tekstowych.

%prep
%setup -q -n %{name}-%{version}-src

%{__sed} -i 's,include/qt3,include/qt,' configure
%{__sed} -i 's,-lk5crypto,,' subcommander/Makefile*

%build
%configure \
	--with-apr=%{_bindir}/apr-1-config \
	--with-apr-util=%{_bindir}/apu-1-config \
	--with-qt=%{_prefix}
%{__make} \
	CFLAGS="%{rpmcflags} -D_LARGEFILE64_SOURCE" \
	CXXFLAGS="%{rpmcxxflags} -I/usr/include/apr-util -Wno-deprecated"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREW README
%attr(755,root,root) %{_bindir}/sc

%files -n submerge
%defattr(644,root,root,755)
%doc CHANGES
%attr(755,root,root) %{_bindir}/sm
%{_datadir}/subcommander
