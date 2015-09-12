%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define up_name Linux_MegaCLI

Summary:	Manage SAS RAID controllers
Name:		megacli
Version:	8.02.21
Release:	4
License:	Commercial
Group:		System/Configuration/Hardware
URL:		http://www.lsi.com
Source0:	http://www.lsi.com/support/downloads/megaraid/miscellaneous/%{version}_MegaCLI.zip

%description
MegaCli is used to manage SAS RAID controllers.

%prep
%setup -q -c
cd %{version}_%{up_name}/
unzip MegaCliLin.zip
rpm2cpio MegaCli-%{version}-1.noarch.rpm | cpio -id

%build

%install
export DONT_STRIP=1

install -d -m 755 %{buildroot}/sbin
%ifarch x86_64
install -m 755 %{version}_%{up_name}/opt/MegaRAID/MegaCli/MegaCli64 %{buildroot}/sbin/megacli
%else
install -m 755 %{version}_%{up_name}/opt/MegaRAID/MegaCli/MegaCli %{buildroot}/sbin/megacli
%endif

%files 
%doc %{version}_MegaCLI.txt
/sbin/megacli
