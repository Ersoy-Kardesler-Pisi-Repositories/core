#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    # shelltools.system("sed -i 's|get_option('datadir') + '/pkgconfig|get_option('libdir') + '/pkgconfig|g' meson.build")
    mesontools.configure("-Dlegacy=true")

def build():
    mesontools.build()
    
def install():
    mesontools.install()
    
    pisitools.dodoc("README*", "COPYING*", "AUTHORS")
    
    pisitools.remove("/usr/include/X11/extensions/apple*")
    pisitools.remove("/usr/include/X11/extensions/windows*")
    pisitools.remove("/usr/share/doc/xorg-proto/COPYING-windowswmproto")
    pisitools.remove("/usr/share/doc/xorg-proto/COPYING-applewmproto")
    pisitools.remove("/usr/lib/pkgconfig/applewmproto.pc")
    pisitools.remove("/usr/lib/pkgconfig/windowswmproto.pc")
    
    #libX11
    pisitools.remove("/usr/include/X11/extensions/vldXvMC.h")
    pisitools.remove("/usr/include/X11/extensions/XKBgeom.h")
