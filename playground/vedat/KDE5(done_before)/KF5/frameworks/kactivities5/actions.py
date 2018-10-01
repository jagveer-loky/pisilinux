﻿#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("%s/build" %get.workDIR())

    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DKACTIVITIES_ENABLE_EXCEPTIONS=OFF \
                          -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt5/mkspecs/modules \
                          -DQT_PLUGIN_INSTALL_DIR=lib/qt5/plugins \
                          -DQML_INSTALL_DIR=lib/qt5/qml \
                          -DLIB_INSTALL_DIR=lib \
                          -DSYSCONF_INSTALL_DIR=/etc \
                          -DLOCALE_INSTALL_DIR=/usr/share/locale \
                          -DPYTHON_EXECUTABLE=/usr/bin/python3 \
                          -DBUILD_TESTING=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("README.md", "MAINTAINER", "TODO")