# break circular dependency
%bcond_with	bootstrap

Summary:	The drakxtools (diskdrake, ...)
Name:		drakxtools
Version:	14.41
Release:	9
License:	GPLv2+
Group:		System/Configuration/Other
Url:		http://wiki.mandriva.com/en/Development/Docs/drakxtools_dev
Source0:	%{name}-%{version}.tar.xz
Source1:        drakxtools.rpmlintrc
Patch1:		drakxtools-14.22.timeout.patch
Patch2:		drakxtools-14.22-grub-password.patch
Patch3:		drakxtools-14.41-release.sh-rename.patch
#Patch4:		rosa-theme-fix.patch
Patch5:		drakxtools-13.51-split-root-user.patch
Patch6:		drakxtools-14.22.initrdinstall.patch
Patch7:         drakxtools.background-and-lang.patch
Patch8:         drakxtools-14.41.remove_unused_locales.patch
Patch9:		drakxtools.remove-openvpn-selection.patch
Patch10:	drakxtools.temporary-update-license.patch
Patch11:	drakbug.openmandriva.patch

BuildRequires:	gettext
BuildRequires:	ldetect-devel >= 0.9.0
BuildRequires:	ncurses-devel
BuildRequires:	perl-devel
BuildRequires:	perl-MDK-Common perl-MDK-Common-devel
BuildRequires:	parted-devel
%if !%{with bootstrap}
BuildRequires:	drakx-installer-binaries
%endif
BuildRequires:	intltool
BuildRequires:	pkgconfig(libtirpc)

# usermode 1.92-4mdv2008.0 has the /etc/pam.d/%{_vendor}-{simple,console}-auth
# files to which we symlink
Requires:	%{name}-curses = %{version}-%{release}
Requires:	usermode
Requires:	%{_vendor}-doc-common
Requires:	perl-Net-DBus
Requires:	perl-Gtk2-WebKit
# needed by drakfont (eg: type1inst):
Requires:	font-tools
Requires:	libxxf86misc
# needed by any::enable_x_screensaver()
Requires:	xset
Requires:	drakconf-icons
# needed for installing packages through do_pkgs -> urpmi -> gmessage
Requires:	gurpmi
Requires:	ldetect-lst >= 0.1.272
Suggests:	drakx-net

Conflicts:	drakx-kbd-mouse-x11 < 0.91
%define __noautoreq 'perl\\((Net::FTP|Time::localetime|URPM|Xconfig.*|Gtk2::WebKit)\\)'

%package	curses
Summary:	The drakxtools (diskdrake, ...)
Group:		System/Configuration/Other
Requires:	perl-base
Requires:	usermode-consoleonly
Requires:	urpmi
Requires:	perl-Locale-gettext
Requires:	module-init-tools
Requires:	%{name}-backend = %{version}-%{release}
Suggests:	drakx-net-text

%package	backend
Summary:	Drakxtools libraries and background tools 
Group:		System/Configuration/Other
Requires:	dmidecode
Requires:	perl-File-FnMatch

%package	http
Summary:	The drakxtools via http
Group:		System/Configuration/Other
Requires:	%{name}-curses = %{version}-%{release}
Requires:	perl(Net::SSLeay)
Requires:	perl-Authen-PAM
Requires(pre,post):rpm-helper

%package -n	drakx-finish-install
Summary:	First boot configuration
Group:		System/Configuration/Other
Requires:	%{name} = %{version}-%{release}
Requires:	drakx-installer-matchbox

%package -n	harddrake
Summary:	Main Hardware Configuration/Information Tool
Group:		System/Configuration/Hardware
Requires:	%{name}-curses = %{version}-%{release}
Requires(pre,post):rpm-helper
Requires:	drakx-kbd-mouse-x11 
Requires:	meta-task
Suggests:	libdrakx-net 
Suggests:	drak3d

%package -n	harddrake-ui
Summary:	Main Hardware Configuration/Information Tool
Group:		System/Configuration/Hardware
Requires:	%{name} = %{version}-%{release}
Requires:	sane-backends
Requires:	drakx-kbd-mouse-x11 
Suggests:	libdrakx-net 
Suggests:	drak3d

%description
Contains many %{vendor} Linux applications simplifying users and
administrators life on a %{vendor} Linux machine. Nearly all of
them work both under XFree (graphical environment) and in console
(text environment), allowing easy distant work.

- drakbug: interactive bug report tool
- drakbug_report: help find bugs in DrakX
- drakclock: date & time configurator
- drakfloppy: boot disk creator
- drakfont: import fonts in the system
- draklog: show extracted information from the system logs
- draksec: security options managment

%description	backend
See package %{name}

%description	curses
Contains many %{vendor} Linux applications simplifying users and
administrators life on a %{vendor} Linux machine. Nearly all of
them work both under XFree (graphical environment) and in console
(text environment), allowing easy distant work.

- adduserdrake: help you adding a user
- diskdrake: DiskDrake makes hard disk partitioning easier. It is
  graphical, simple and powerful. Different skill levels are available
  (newbie, advanced user, expert). It's written entirely in Perl and
  Perl/Gtk. It uses resize_fat which is a perl rewrite of the work of
  Andrew Clausen (libresize).
- drakauth: configure authentification (LDAP/NIS/...)
- drakautoinst: help you configure an automatic installation replay
- drakboot: configures your boot configuration (Lilo/GRUB,
  Bootsplash, X, autologin)
- drakkeyboard: configure your keyboard (both console and X)
- draklocale: language configurator, available both for root
  (system wide) and users (user only)
- drakmouse: autodetect and configure your mouse
- drakscanner: scanner configurator
- draksound: sound card configuration
- drakx11: menu-driven program which walks you through setting up
  your X server; it autodetects both monitor and video card if
  possible
- drakxservices: SysV services and daemons configurator
- drakxtv: auto configure tv card for xawtv grabber
- lsnetdrake: display available nfs and smb shares
- lspcidrake: display your pci information, *and* the corresponding
  kernel module

%description	http
This package lets you configure your computer through your Web browser:
it provides an HTTP interface to the %{vendor} tools found in the drakxtools
package.

%description -n	drakx-finish-install
For OEM-like duplications, it allows at first boot:
- network configuration
- creating users
- setting root password
- choosing authentication

%description -n	harddrake
The harddrake service is a hardware probing tool run at system boot
time to determine what hardware has been added or removed from the
system.
It then offer to run needed config tool to update the OS
configuration.

%description -n	harddrake-ui
This is the main configuration tool for hardware that calls all the
other configuration tools.
It offers a nice GUI that show the hardware configuration splitted by
hardware classes.

%prep
%setup -q
%apply_patches

%build
%make -C perl-install CFLAGS="$RPM_OPT_FLAGS"

%install
%make -C perl-install PREFIX=%{buildroot} install
mkdir -p %{buildroot}%{_sysconfdir}/{X11/xinit.d,X11/wmsession.d,sysconfig/harddrake2}
touch %{buildroot}/etc/sysconfig/harddrake2/previous_hw

dirs1="usr/lib/libDrakX usr/share/libDrakX"
(cd %{buildroot} ; find $dirs1 usr/bin usr/sbin ! -type d -printf "/%%p\n")|egrep -v 'bin/.*harddrake' > %{name}.list
(cd %{buildroot} ; find $dirs1 -type d -printf "%%%%dir /%%p\n") >> %{name}.list

perl -ni -e '/dbus_object\.pm|Xdrakres|clock|display_help|display_release_notes.pl|drak(bug|clock|dvb|floppy|font|hosts|log|sec|splash)|gtk|icons|logdrake|pixmaps|\.png$/ ? print STDERR $_ : print' %{name}.list 2> %{name}-gtk.list
perl -ni -e '/http/ ? print STDERR $_ : print' %{name}.list 2> %{name}-http.list
perl -ni -e 'm!lib/libDrakX|bootloader-config|fileshare|lsnetdrake|drakupdate_fstab|rpcinfo|serial_probe! && !/curses/i ? print STDERR $_ : print' %{name}.list 2> %{name}-backend.list
perl -pi -e 's|^(/usr/sbin/fileshareset)$|%%attr(4755,root,root) $1|;' %{name}-backend.list
perl -ni -e '/finish-install/ ? print STDERR $_ : print' %{name}.list 2> finish-install.list

#mdk menu entry
mkdir -p %{buildroot}%{_datadir}/autostart

cat > %{buildroot}%{_sysconfdir}/X11/xinit.d/harddrake2 <<EOF
#!/bin/sh
exec /usr/share/harddrake/service_harddrake X11
EOF

cat > %{buildroot}%{_sysconfdir}/sysconfig/harddrake2/kernel <<EOF
KERNEL=2.6
EOF

mv %{buildroot}%{_sbindir}/service_harddrake_confirm %{buildroot}%{_datadir}/harddrake/confirm

chmod +x %{buildroot}{%{_datadir}/harddrake/{conf*,service_harddrake},%{_sysconfdir}/X11/xinit.d/harddrake2}
# temporary fix until we reenable this feature
rm -f %{buildroot}%{_sysconfdir}/X11/xinit.d/harddrake2

perl -I perl-install -mharddrake::data -e 'print "DETECT_$_->{class}=yes\n" foreach @harddrake::data::tree' |sort > %{buildroot}%{_sysconfdir}/sysconfig/harddrake2/service.conf
echo -e "AUTORECONFIGURE_RIGHT_XORG_DRIVER=yes\n" >> %{buildroot}%{_sysconfdir}/sysconfig/harddrake2/service.conf

# consolehelper config
#

# - console user, no password
for pak in drakclock drakkeyboard drakmouse; do
	ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/$pak
	mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps/
	cat > %{buildroot}%{_sysconfdir}/security/console.apps/$pak <<EOF
USER=<user>
PROGRAM=%{_sbindir}/$pak
FALLBACK=false
SESSION=true
EOF
	mkdir -p %{buildroot}%{_sysconfdir}/pam.d/
	ln -sf %{_sysconfdir}/pam.d/%{_vendor}-console-auth %{buildroot}%{_sysconfdir}/pam.d/$pak
done

# console user, ask for user password
for pak in drakfont; do
	ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/$pak
	mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps/
	cat > %{buildroot}%{_sysconfdir}/security/console.apps/$pak <<EOF
USER=<user>
PROGRAM=%{_sbindir}/$pak
FALLBACK=false
SESSION=true
EOF
	mkdir -p %{buildroot}%{_sysconfdir}/pam.d/
	ln -sf %{_sysconfdir}/pam.d/%{_vendor}-simple-auth %{buildroot}%{_sysconfdir}/pam.d/$pak
done

# console user, ask for root password
for pak in drakups drakauth draklog drakxservices drakboot; do
	ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/$pak
	mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
	cat > %{buildroot}%{_sysconfdir}/security/console.apps/$pak <<EOF
USER=root
PROGRAM=/usr/sbin/$pak
FALLBACK=false
SESSION=true
EOF
	mkdir -p %{buildroot}%{_sysconfdir}/pam.d
	ln -sf %{_sysconfdir}/pam.d/%{_vendor}-simple-auth %{buildroot}%{_sysconfdir}/pam.d/$pak
done

%find_lang libDrakX libDrakX.lang
%find_lang libDrakX-standalone libDrakX-standalone.lang
cat libDrakX.lang libDrakX-standalone.lang >> %{name}.list

%check
cd perl-install
%make check

%post
%make_session
[[ ! -e %{_sbindir}/kbdconfig ]] && %__ln_s -f keyboarddrake %{_sbindir}/kbdconfig
[[ ! -e %{_sbindir}/mouseconfig ]] && %__ln_s -f mousedrake %{_sbindir}/mouseconfig
:

%postun
%make_session
for i in %{_sbindir}/kbdconfig %{_sbindir}/mouseconfig %{_bindir}/printtool;do
    [[ -L $i ]] && %__rm -f $i
done
:

%post http
%_post_service drakxtools_http

%preun http
%_preun_service drakxtools_http

%postun -n harddrake
file /etc/sysconfig/harddrake2/previous_hw | fgrep -q perl && %{_datadir}/harddrake/convert || :

%files backend -f %{name}-backend.list
%config(noreplace) /etc/security/fileshare.conf

%files curses -f %{name}.list
%{_datadir}/applications/localedrake*.desktop
%doc perl-install/diskdrake/diskdrake.html
%{_iconsdir}/localedrake.png
%{_iconsdir}/large/localedrake.png
%{_iconsdir}/mini/localedrake.png
%{_bindir}/drakkeyboard
%{_bindir}/drakmouse
%{_bindir}/drakups
%{_bindir}/drakauth
%{_bindir}/draklog
%{_bindir}/drakxservices
%{_bindir}/drakboot
%config(noreplace) %{_sysconfdir}/security/console.apps/drakkeyboard
%config(noreplace) %{_sysconfdir}/security/console.apps/drakmouse
%config(noreplace) %{_sysconfdir}/security/console.apps/drakups
%config(noreplace) %{_sysconfdir}/security/console.apps/drakauth
%config(noreplace) %{_sysconfdir}/security/console.apps/draklog
%config(noreplace) %{_sysconfdir}/security/console.apps/drakxservices
%config(noreplace) %{_sysconfdir}/security/console.apps/drakboot
%config(noreplace) %{_sysconfdir}/pam.d/drakkeyboard
%config(noreplace) %{_sysconfdir}/pam.d/drakmouse
%config(noreplace) %{_sysconfdir}/pam.d/drakups
%config(noreplace) %{_sysconfdir}/pam.d/drakauth
%config(noreplace) %{_sysconfdir}/pam.d/draklog
%config(noreplace) %{_sysconfdir}/pam.d/drakxservices
%config(noreplace) %{_sysconfdir}/pam.d/drakboot

%files -f %{name}-gtk.list
%{_bindir}/drakclock
%{_bindir}/drakfont
%config(noreplace) %{_sysconfdir}/security/console.apps/drakclock
%config(noreplace) %{_sysconfdir}/security/console.apps/drakfont
%config(noreplace) %{_sysconfdir}/pam.d/drakclock
%config(noreplace) %{_sysconfdir}/pam.d/drakfont

%files -n harddrake
%dir /etc/sysconfig/harddrake2/
%config(noreplace) /etc/sysconfig/harddrake2/previous_hw
%config(noreplace) /etc/sysconfig/harddrake2/service.conf
%config(noreplace) %{_sysconfdir}/sysconfig/harddrake2/kernel
%dir %{_datadir}/harddrake/
%{_datadir}/harddrake/*
%{_sysconfdir}/X11/xsetup.d/??notify-x11-free-driver-switch.xsetup
#%{_sysconfdir}/X11/xinit.d/harddrake2

%files -n harddrake-ui
%dir /etc/sysconfig/harddrake2/
%{_sbindir}/harddrake2
%{_datadir}/pixmaps/harddrake2
%{_datadir}/applications/harddrake.desktop
%{_iconsdir}/large/harddrake.png
%{_iconsdir}/mini/harddrake.png
%{_iconsdir}/harddrake.png

%files -n drakx-finish-install
%config(noreplace) %{_sysconfdir}/sysconfig/finish-install
%{_sysconfdir}/X11/xsetup.d/??finish-install.xsetup
%{_sbindir}/finish-install

%files http -f %{name}-http.list
%dir %{_sysconfdir}/drakxtools_http
%config(noreplace) %{_sysconfdir}/pam.d/miniserv
%{_sysconfdir}/init.d/drakxtools_http
%config(noreplace) %{_sysconfdir}/drakxtools_http/conf
%config(noreplace) %{_sysconfdir}/drakxtools_http/authorised_progs
%config(noreplace) %{_sysconfdir}/logrotate.d/drakxtools-http
