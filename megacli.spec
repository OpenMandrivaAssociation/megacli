%define name    megacli
%define up_name Linux_Cli
%define version 1.01.39
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        LSI MegaRAID Storage Manager
License:	Commercial
Group:		System/Configuration/Hardware
Source0:        http://www.lsi.com/support/downloads/megaraid/miscellaneous/linux/%{version}_%{up_name}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Those diagnostic tools include debug scripts and the sanlun utility, which
provide information about the Linux host, storage system configuration, and
LUNs. You can send the output from these scripts to NetApp Customer Support to
troubleshoot your configuration.

%prep
%setup -q -c
rpm2cpio MegaCli-%{version}-0.i386.rpm | cpio -id

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_sbindir}
%ifarch x86_64
install -m 755 opt/MegaRAID/MegaCli/MegaCli64 %{buildroot}%{_sbindir}/megacli
%else
install -m 755 opt/MegaRAID/MegaCli/MegaCli %{buildroot}%{_sbindir}/megacli
%endif

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root) 
%doc %{version}_Linux_Cli.txt
%{_sbindir}/megacli

