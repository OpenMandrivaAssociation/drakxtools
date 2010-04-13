Summary: The drakxtools (diskdrake, ...)
Name:    drakxtools
Version: 13.19
Release: %mkrel 1
Url:     http://wiki.mandriva.com/en/Development/Docs/drakxtools_dev
Source0: %name-%version.tar.lzma
License: GPLv2+
Group: System/Configuration/Other
# usermode 1.92-4mdv2008.0 has the /etc/pam.d/mandriva-{simple,console}-auth
# files to which we symlink
Requires: %{name}-curses = %version-%release, perl-Gtk2 >= 1.220, perl-Glib >= 1.072-1mdk, usermode >= 1.92-4mdv2008.0, mandriva-doc-common >= 9.2-5mdk, perl-Net-DBus, perl-Gtk2-WebKit
# needed by drakfont (eg: type1inst):
Requires: font-tools
Requires: libxxf86misc
# needed by any::enable_x_screensaver()
Requires: xset
Requires: drakx-net
Requires: drakconf-icons
# needed for installing packages through do_pkgs -> urpmi -> gmessage
Requires: gurpmi >= 5.7
Conflicts: drakconf < drakconf-11.7.2
Conflicts: rpmdrake < 3.26-1
Conflicts: mandrake_doc-drakxtools-en < 9.2, mandrake_doc-drakxtools-es < 9.2, mandrake_doc-drakxtools-fr < 9.2
Conflicts: bootloader-utils < 1.8-4mdk, bootsplash < 2.1.7-1mdk
Conflicts: drakx-kbd-mouse-x11 < 0.19
Conflicts: initscripts < 8.33-4mdk
Requires: ldetect-lst >= 0.1.272
BuildRequires: gettext, ldetect-devel >= 0.9.0, ncurses-devel, perl-devel >= 1:5.8.0-20mdk, perl-MDK-Common-devel >= 1.1.8-3mdk
BuildRequires: parted-devel
BuildRequires: drakx-installer-binaries intltool
BuildRoot: %_tmppath/%name-buildroot
Provides: draksec
Obsoletes: draksec
%define _requires_exceptions perl(Net::FTP)\\|perl(Time::localtime)\\|perl(URPM)\\|perl(Xconfig.*)

%package curses
Summary: The drakxtools (diskdrake, ...)
Group: System/Configuration/Other
Requires: perl-base >= 2:5.8.6-1mdk, urpmi >= 4.8.23, usermode-consoleonly >= 1.44-4mdk
Requires: perl-Locale-gettext >= 1.05-4mdv2007
Requires: module-init-tools
Requires: %{name}-backend = %version-%release
Requires: drakx-net-text
Obsoletes: diskdrake kbdconfig mouseconfig setuptool drakfloppy
Obsoletes: drakxtools-newt
Provides: diskdrake, kbdconfig mouseconfig setuptool, drakfloppy = %version-%release
Provides: drakxtools-newt = %version-%release
%define _requires_exceptions perl(Gtk2::WebKit)\\|perl(Xconfig::various)

%package backend
Summary: Drakxtools libraries and background tools 
Group: System/Configuration/Other
Requires: dmidecode
Requires: perl-File-FnMatch
# for fileshareset and filesharelist (#17123)
Requires: perl-suid
# for common::wrap_command_for_root()
Requires: perl-String-ShellQuote
# "post" here means %triggerpostun:
Requires(post): perl-MDK-Common >= 1.2.13
Conflicts: drakxtools-newt < 10-51mdk
Conflicts: drakx-net < 0.28
Conflicts: e2fsprogs < 1.41.1-2mnb

%package http
Summary: The drakxtools via http
Group: System/Configuration/Other
Requires: %{name}-curses = %version-%release, perl(Net::SSLeay) >= 1.22-1mdk, perl-Authen-PAM >= 0.14-1mdk, perl-CGI >= 2.91-1mdk
Requires(pre): rpm-helper
Requires(post): rpm-helper

%package -n drakx-finish-install
Summary: First boot configuration
Group: System/Configuration/Other
Requires: %{name} = %version-%release
Requires: drakx-installer-matchbox

%package -n harddrake
Summary: Main Hardware Configuration/Information Tool
Group: System/Configuration/Hardware
Requires: %{name}-curses = %version-%release
Obsoletes: kudzu, kudzu-devel, libdetect0, libdetect0-devel, libdetect-lst, libdetect-lst-devel, detect, detect-lst
Provides: kudzu = %version, kudzu-devel = %version, libdetect0, libdetect0-devel, libdetect-lst, libdetect-lst-devel, detect, detect-lst
Requires(pre): rpm-helper
Requires(post): rpm-helper
Requires: libdrakx-net drakx-kbd-mouse-x11 drak3d
Requires: meta-task

%package -n harddrake-ui
Summary: Main Hardware Configuration/Information Tool
Group: System/Configuration/Hardware
Requires: %name = %version-%release
Requires: sane-backends
Requires: libdrakx-net drakx-kbd-mouse-x11 drak3d

%description
Contains many Mandriva Linux applications simplifying users and
administrators life on a Mandriva Linux machine. Nearly all of
them work both under XFree (graphical environment) and in console
(text environment), allowing easy distant work.

- drakbug: interactive bug report tool
- drakbug_report: help find bugs in DrakX
- drakclock: date & time configurator
- drakfloppy: boot disk creator
- drakfont: import fonts in the system
- draklog: show extracted information from the system logs
- drakperm: msec GUI (permissions configurator)
- draksec: security options managment / msec frontend

%description backend
See package %name

%description curses
Contains many Mandriva Linux applications simplifying users and
administrators life on a Mandriva Linux machine. Nearly all of
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

%description http
This package lets you configure your computer through your Web browser:
it provides an HTTP interface to the Mandriva tools found in the drakxtools
package.

%description -n drakx-finish-install
For OEM-like duplications, it allows at first boot:
- network configuration
- creating users
- setting root password
- choosing authentication


%description -n harddrake
The harddrake service is a hardware probing tool run at system boot
time to determine what hardware has been added or removed from the
system.
It then offer to run needed config tool to update the OS
configuration.


%description -n harddrake-ui
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
rm -rf $RPM_BUILD_ROOT

%make -C perl-install PREFIX=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/{X11/xinit.d,X11/wmsession.d,sysconfig/harddrake2}
touch $RPM_BUILD_ROOT/etc/sysconfig/harddrake2/previous_hw

dirs1="usr/lib/libDrakX usr/share/libDrakX"
(cd $RPM_BUILD_ROOT ; find $dirs1 usr/bin usr/sbin ! -type d -printf "/%%p\n")|egrep -v 'bin/.*harddrake' > %{name}.list
(cd $RPM_BUILD_ROOT ; find $dirs1 -type d -printf "%%%%dir /%%p\n") >> %{name}.list

perl -ni -e '/dbus_object\.pm|Xdrakres|clock|display_help|display_release_notes.pl|drak(bug|clock|dvb|floppy|font|hosts|log|perm|sec|splash)|gtk|icons|logdrake|pixmaps|\.png$/ ? print STDERR $_ : print' %{name}.list 2> %{name}-gtk.list
perl -ni -e '/http/ ? print STDERR $_ : print' %{name}.list 2> %{name}-http.list
perl -ni -e 'm!lib/libDrakX|bootloader-config|fileshare|lsnetdrake|drakupdate_fstab|rpcinfo|serial_probe! && !/curses/i ? print STDERR $_ : print' %{name}.list 2> %{name}-backend.list
perl -ni -e '/finish-install/ ? print STDERR $_ : print' %{name}.list 2> finish-install.list

#mdk menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/autostart

cat > $RPM_BUILD_ROOT%_sysconfdir/X11/xinit.d/harddrake2 <<EOF
#!/bin/sh
exec /usr/share/harddrake/service_harddrake X11
EOF

cat > $RPM_BUILD_ROOT%_sysconfdir/sysconfig/harddrake2/kernel <<EOF
KERNEL=2.6
EOF

mv $RPM_BUILD_ROOT%_sbindir/service_harddrake_confirm $RPM_BUILD_ROOT%_datadir/harddrake/confirm

chmod +x $RPM_BUILD_ROOT{%_datadir/harddrake/{conf*,service_harddrake},%_sysconfdir/X11/xinit.d/harddrake2}
# temporary fix until we reenable this feature
rm -f $RPM_BUILD_ROOT%_sysconfdir/X11/xinit.d/harddrake2

perl -I perl-install -mharddrake::data -e 'print "DETECT_$_->{class}=yes\n" foreach @harddrake::data::tree' |sort > $RPM_BUILD_ROOT%_sysconfdir/sysconfig/harddrake2/service.conf
echo -e "AUTORECONFIGURE_RIGHT_XORG_DRIVER=yes\n" >> $RPM_BUILD_ROOT%_sysconfdir/sysconfig/harddrake2/service.conf

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
        ln -sf %{_sysconfdir}/pam.d/mandriva-console-auth %{buildroot}%{_sysconfdir}/pam.d/$pak
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
        ln -sf %{_sysconfdir}/pam.d/mandriva-simple-auth %{buildroot}%{_sysconfdir}/pam.d/$pak
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
        ln -sf %{_sysconfdir}/pam.d/mandriva-simple-auth %{buildroot}%{_sysconfdir}/pam.d/$pak
done

%find_lang libDrakX
%find_lang libDrakX-standalone
cat libDrakX.lang libDrakX-standalone.lang >> %name.list

%check
cd perl-install
%make check

%clean
rm -rf $RPM_BUILD_ROOT

%post
%make_session
[[ ! -e %_sbindir/kbdconfig ]] && %__ln_s -f keyboarddrake %_sbindir/kbdconfig
[[ ! -e %_sbindir/mouseconfig ]] && %__ln_s -f mousedrake %_sbindir/mouseconfig
:

%postun
%make_session
for i in %_sbindir/kbdconfig %_sbindir/mouseconfig %_bindir/printtool;do
    [[ -L $i ]] && %__rm -f $i
done
:

%post http
%_post_service drakxtools_http

%preun http
%_preun_service drakxtools_http

%if %mdkversion < 200900
%post curses
%update_menus
%endif

%if %mdkversion < 200900
%postun curses
%clean_menus
%endif

%if %mdkversion < 200900
%post -n harddrake-ui
%update_menus
%endif

%if %mdkversion < 200900
%postun -n harddrake-ui
%clean_menus
%endif

%postun -n harddrake
file /etc/sysconfig/harddrake2/previous_hw | fgrep -q perl && %_datadir/harddrake/convert || :

%triggerpostun backend -- drakxtools-backend < 11.44
echo "Migrating /etc/fstab and bootloader configuration to use UUIDs. Previous files are saved with extension .before-migrate-to-uuids"
%_sbindir/bootloader-config --action migrate-to-uuids ||:

%triggerpostun backend -- drakxtools-backend < 11.52
echo "Updating /etc/modprobe.preload.d/floppy"
perl -I/usr/lib/libDrakX -Mharddrake::autoconf -e 'harddrake::autoconf::floppy()' ||:

%triggerpostun -n harddrake -- harddrake < 11.62-2
rm -f /etc/rc.d/*/{K,S}??harddrake

%files backend -f %{name}-backend.list
%defattr(-,root,root)
%config(noreplace) /etc/security/fileshare.conf
%attr(4755,root,root) %_sbindir/fileshareset

%files curses -f %name.list
%defattr(-,root,root)
%{_datadir}/applications/localedrake*.desktop
%doc perl-install/diskdrake/diskdrake.html
%_iconsdir/localedrake.png
%_iconsdir/large/localedrake.png
%_iconsdir/mini/localedrake.png
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
%defattr(-,root,root)
%{_bindir}/drakclock
%{_bindir}/drakfont
%config(noreplace) %{_sysconfdir}/security/console.apps/drakclock
%config(noreplace) %{_sysconfdir}/security/console.apps/drakfont
%config(noreplace) %{_sysconfdir}/pam.d/drakclock
%config(noreplace) %{_sysconfdir}/pam.d/drakfont

%files -n harddrake
%defattr(-,root,root)
%dir /etc/sysconfig/harddrake2/
%config(noreplace) /etc/sysconfig/harddrake2/previous_hw
%config(noreplace) /etc/sysconfig/harddrake2/service.conf
%config(noreplace) %_sysconfdir/sysconfig/harddrake2/kernel
%dir %_datadir/harddrake/
%_datadir/harddrake/*
%_sysconfdir/X11/xsetup.d/??notify-x11-free-driver-switch.xsetup
#%_sysconfdir/X11/xinit.d/harddrake2

%files -n harddrake-ui
%defattr(-,root,root)
%dir /etc/sysconfig/harddrake2/
%_sbindir/harddrake2
%_datadir/pixmaps/harddrake2
%{_datadir}/applications/harddrake.desktop
%_iconsdir/large/harddrake.png
%_iconsdir/mini/harddrake.png
%_iconsdir/harddrake.png

%files -n drakx-finish-install
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/sysconfig/finish-install
%_sysconfdir/X11/xsetup.d/??finish-install.xsetup
%_sbindir/finish-install

%files http -f %{name}-http.list
%defattr(-,root,root)
%dir %_sysconfdir/drakxtools_http
%config(noreplace) %_sysconfdir/pam.d/miniserv
%_sysconfdir/init.d/drakxtools_http
%config(noreplace) %_sysconfdir/drakxtools_http/conf
%config(noreplace) %_sysconfdir/drakxtools_http/authorised_progs
%config(noreplace) %_sysconfdir/logrotate.d/drakxtools-http


