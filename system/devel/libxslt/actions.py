#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


Libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"
bindir = "/usr/bin32" if get.buildTYPE() == "emul32" else "/usr/bin"

def setup():
    shelltools.export("PYTHON", "/usr/bin/python3")
    python = "--without-python" if get.buildTYPE() == "emul32" else "--with-python=/usr/bin/python3 "
    # don't remove --with-debugger as it is needed for reverse dependencies
    autotools.configure("%s \
                         --with-crypto \
                         --bindir=%s \
                         --with-debugger \
                         --disable-static \
                         --includedir=/usr/include \
                         --disable-silent-rules \
                        " % (python, bindir))

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        return

    pisitools.dodoc("AUTHORS", "Copyright", "FEATURES", "NEWS", "README*", "TODO")
