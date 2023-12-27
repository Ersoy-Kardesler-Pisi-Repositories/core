#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    python3modules.compile()


def install():
    python3modules.install()
    
    pisitools.insinto("/usr/share/vim/vimfiles", "data/syntax-highlighting/vim/*")
    # pisitools.insinto("/usr/share/emacs/site-lisp", "data/syntax-highlighting/emacs/*")
    pisitools.insinto("/usr/share/zsh/site-functions", "data/shell-completions/zsh/*")
    pisitools.insinto("/usr/share/bash-completion/completions", "data/shell-completions/bash/*")
    pisitools.remove("/usr/share/vim/vimfiles/README")
    
    pisitools.dodoc("COPYING", "README*")
