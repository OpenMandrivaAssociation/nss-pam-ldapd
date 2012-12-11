Name:		nss-pam-ldapd
Version:	0.8.3
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
%configure2_5x --libdir=/%{_lib} --with-pam-seclib-dir=/%{_lib}/security
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



%changelog
* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.3-1mdv2011.0
+ Revision: 674629
- update to new version 0.8.3

* Mon Mar 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-1
+ Revision: 648674
- new version

* Fri Mar 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.0-2
+ Revision: 648530
- fix CVE-2011-0438 (official patch)

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 626830
- update to new version 0.8.0

* Mon Dec 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.13-2mdv2011.0
+ Revision: 623435
- update to new version 0.7.13

* Tue Nov 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.12-1mdv2011.0
+ Revision: 591966
- update to new version 0.7.12

* Sun Oct 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.11-1mdv2011.0
+ Revision: 586216
- update to new version 0.7.11

* Fri Oct 01 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.10-1mdv2011.0
+ Revision: 582408
- update to new version 0.7.10

* Thu Aug 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.8-1mdv2011.0
+ Revision: 571343
- update to new version 0.7.8

* Sat Jul 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.7-1mdv2011.0
+ Revision: 554590
- update to new version 0.7.7

* Sun Feb 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.3-1mdv2010.1
+ Revision: 512707
- update to new version 0.7.3

* Thu Dec 31 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.2-1mdv2010.1
+ Revision: 484534
- new version

* Mon Nov 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.1-1mdv2010.1
+ Revision: 466597
- import nss-pam-ldapd


* Thu Sep 24 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6.11-2
- rebuild

* Wed Sep 16 2009 Nalin Dahyabhai <nalin@redhat.com> 
- apply Mitchell Berger's patch to clean up the init script, use %%{_initddir},
  and correct the %%post so that it only thinks about turning on nslcd when
  we're first being installed (#522947)
- tell status() where the pidfile is when the init script is called for that

* Tue Sep  8 2009 Nalin Dahyabhai <nalin@redhat.com>
- fix typo in a comment, capitalize the full name for "LDAP Client User" (more
  from #516049)

* Wed Sep  2 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6.11-1
- update to 0.6.11

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6.10-3
- update URL: and Source:

* Mon Jun 15 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6.10-2
- add and own /var/run/nslcd
- convert hosts to uri during migration

* Thu Jun 11 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6.10-1
- update to 0.6.10

* Fri Apr 17 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6.8-1
- bump release number to 1 (part of #491767)
- fix which group we check for during %%pre (part of #491767)

* Tue Mar 24 2009 Nalin Dahyabhai <nalin@redhat.com>
- require chkconfig by package rather than path (Jussi Lehtola, part of #491767)

* Mon Mar 23 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6.8-0.1
- update to 0.6.8

* Mon Mar 23 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6.7-0.1
- start using a dedicated user

* Wed Mar 18 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6.7-0.0
- initial package (#445965)
