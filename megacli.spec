%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define up_name Linux_MegaCLI

Summary:	MegaCli is used to manage SAS RAID controllers
Name:		megacli
Version:	4.00.11
Release:	%mkrel 1
License:	Commercial
Group:		System/Configuration/Hardware
URL:		http://www.lsi.com
Source0:	http://www.lsi.com/support/downloads/megaraid/miscellaneous/%{version}_%{up_name}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package contains SAS MegaRAID Linux MegaCLI.

%prep

%setup -q -c
unzip MegaCliLin.zip
rpm2cpio MegaCli-%{version}-1.i386.rpm | cpio -id

%build

%install
rm -rf %{buildroot}

export DONT_STRIP=1

install -d -m 755 %{buildroot}/sbin
%ifarch x86_64
install -m 755 opt/MegaRAID/MegaCli/MegaCli64 %{buildroot}/sbin/megacli
%else
install -m 755 opt/MegaRAID/MegaCli/MegaCli %{buildroot}/sbin/megacli
%endif

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root) 
%doc %{version}_%{up_name}.txt
/sbin/megacli
