#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("env NOCONFIGURE=1 ./autogen.sh")
    
    autotools.configure("--enable-rust \
                         --enable-trivial-httpd-cmdline \
                         --with-openssl \
                         --disable-static \
                         --without-dracut \
                         --without-mkinitcpio")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.removeDir("/etc/grub.d")

    pisitools.dodoc("TODO", "README*")
