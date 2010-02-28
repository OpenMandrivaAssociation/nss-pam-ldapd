Name:		nss-pam-ldapd
Version:	0.7.3
Release:	%mkrel 1
Summary:	An nsswitch module which uses directory servers
Group:		System/Libraries
License:	LGPLv2+
URL:		http://arthurdejong.org/nss-ldapd/
Source0:	http://arthurdejong.org/nss-ldapd/%{name}-%{version}.tar.gz
Source2:	nslcd.init
BuildRequires:	openldap-devel
BuildRequires:	krb5-devel
BuildRequires:	pam-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The nss-ldapd daemon, nslcd, uses a directory server to look up name
service information (users, groups, etc.) on behalf of a lightweight
nsswitch module.

%prep
%setup -q

%build
%configure2_5x --libdir=/%{_lib}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -d -m 755 %{buildroot}%{_initrddir}
install -m 755 %{SOURCE2} %{buildroot}%{_initrddir}/nslcd

cat >> %{buildroot}%{_sysconfdir}/nss-ldapd.conf << EOF
uid nslcd
gid ldap
EOF

install -d -m 755 %{buildroot}%{_localstatedir}/run/nslcd

%clean
rm -rf %{buildroot}

%pre
%_pre_useradd nslcd / /bin/false

%post
%_post_service nslcd

%preun
%_preun_service nslcd

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING HACKING NEWS README TODO
%{_sbindir}/*
/%{_lib}/*.so.*
/%{_lib}/security/*.so
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/nss-ldapd.conf
%config(noreplace) %{_sysconfdir}/nslcd.conf
%{_initrddir}/nslcd
%attr(-,nslcd,root) %{_localstatedir}/run/nslcd

