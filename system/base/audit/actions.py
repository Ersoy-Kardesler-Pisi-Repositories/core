#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("PYTHON", "/usr/bin/python3")
    autotools.autoreconf("-vif")
    autotools.configure("--with-libcap-ng=yes \
                         --enable-gssapi-krb5=no \
                         --enable-systemd=no \
                         --disable-zos-remote \
                         --disable-static")

def build():
    autotools.make()

def check():
    autotools.make("-j1 check")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # remove RH specific bits
    pisitools.removeDir("/etc/sysconfig")
    pisitools.removeDir("/etc/rc.d")

    # Create data directories
    pisitools.dodir("/var/log/audit")
    pisitools.dodir("/var/spool/audit")

    # Disable zos-remote plugin to get rid of deps. like cyrus-sasl
    pisitools.remove("/usr/share/man/man8/audispd-zos-remote.8")
    pisitools.remove("/usr/share/man/man5/zos-remote.conf.5")
    
    pisitools.insinto("/etc/audit/rules.d", "rules/10-no-audit.rules", "audit.rules")
    
    for sbin in shelltools.ls("%s/usr/sbin" % get.installDIR()):
        pisitools.dosym("/usr/sbin/%s" % sbin, "/sbin/%s" % sbin)

    pisitools.dodoc("AUTHORS", "ChangeLog", "THANKS", "README", "COPYING")
