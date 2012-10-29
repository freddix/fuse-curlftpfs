%define		rname	curlftpfs

Summary:	A filesystem for accessing FTP sites
Name:		fuse-curlftpfs
Version:	0.9.2
Release:	14
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/curlftpfs/%{rname}-%{version}.tar.gz
# Source0-md5:	b452123f755114cd4461d56c648d9f12
URL:		http://curlftpfs.sourceforge.net/
BuildRequires:	curl-devel
BuildRequires:	fuse-devel
BuildRequires:	glib-devel
BuildRequires:	libstdc++-devel
Requires:	fuse
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A filesystem for accessing FTP sites. You can "mount" FTP shared
directories in your very personal file system and take advantage of
local files ops. It's based on libcurl and automatically reconnects
when the server times out.

%prep
%setup -qn %{rname}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install curlftpfs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/curlftpfs
%{_mandir}/man1/curlftpfs.1*

