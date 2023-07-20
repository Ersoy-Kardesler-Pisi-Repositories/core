#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-rpath")
    #shelltools.system("sed -i '/pragma weak pthread_create/d' tests/glthread/thread.h")

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.install()
    
    pisitools.dosym("libunistring.so.2.2.0", "/usr/lib/libunistring.so.0")
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "COPYING.LIB", "HACKING", "NEWS", "README",  "THANKS")
