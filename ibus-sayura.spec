Name:       ibus-sayura
Version:    1.2.99.20100209
Release:    3%{?dist}
Summary:    The Sinhala engine for IBus input platform
License:    GPLv2+
Group:      System Environment/Libraries
URL:        https://fedorahosted.org/ibus-sayura
Source0:    https://fedorahosted.org/releases/i/b/ibus-sayura/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  ibus-devel

Requires:   ibus
Patch1: bug-601568.patch
Patch2: bug-613510.patch
%description
The Sayura engine for IBus platform. It provides Sinhala input method.

%prep
%setup -q
%patch1 -p1 -b .1-fix-for-64-bit
%patch2 -p1 -b .1-fix-for-right-shift-key

%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-sayura
%{_datadir}/ibus-sayura
%{_datadir}/ibus/component/*

%changelog
* Wed Jul 14 2010 Pravin Satpute <psatpute@redhat.com> - 1.2.99.20100209-3
- Resolves: bug 613510

* Thu Jun 16 2010 Pravin Satpute <psatpute@redhat.com> - 1.2.99.20100209-2
- Resolves: bug 604076

* Tue Feb 09 2010 Pravin Satpute <pravin.d.s@gmail.com> - 1.2.99.20100209-1
- updated patches for code enhancements from phuang for ibus-1.2.99

* Mon Feb 08 2010 Adam Jackson <ajax@redhat.com> 1.2.0.20090703-4
- Rebuild for new libibus.so.2 ABI

* Tue Nov 17 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-3
- fixed bug 528405

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090703-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-1
- upstream release 1.2.0

* Mon Jun 29 2009 Pravin Satpute <pravin.d.s@gmail.com> - @VERSON@-4
- fix for bug 507209

* Mon Jun 29 2009 Parag <panemade@gmail.com> - 1.0.0.20090326-3
- Rebuild against newer ibus

* Thu Mar 26 2009 Pravin Satpute <pravin.d.s@gmail.com> - @VERSON@-2
- updated as per fedora spec review

* Fri Mar 20 2009 Pravin Satpute <pravin.d.s@gmail.com> - 1.0.0.20090326-1
- The first version.
