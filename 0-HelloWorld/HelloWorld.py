# -*- coding: utf-8 -*-

"""
/***************************************************************************
                             A QGIS plugin Hello World

                             -------------------
        begin                : 2020-05-31
        copyright            : (C) 2020 by Zhefeng Jin
        email                : wugis1219@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5.QtGui import (QIcon)
from PyQt5.QtWidgets import (QAction, QMessageBox)

from .MyDialog import MyDialog

class HelloWorld:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self._iface = iface
        self.map_canvas = iface.mapCanvas()

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

    # noinspection PyAttributeOutsideInit
    # noinspection PyPep8Naming
    def initGui(self):
        icon_path = os.path.join(self.plugin_dir, "icons", "icon.png")
        self._action_test_message_box = QAction(QIcon(icon_path), 'Test QMessageBox', self._iface.mainWindow())
        self._action_test_dialog = QAction(QIcon(icon_path), 'Test QDialog', self._iface.mainWindow())

        self._toolbar = self._iface.addToolBar(u'HelloWorld')

        self._toolbar.addAction(self._action_test_message_box)
        self._toolbar.addAction(self._action_test_dialog)

        # connecting
        self._action_test_message_box.triggered.connect(self.on_action_test_message_box)
        self._action_test_dialog.triggered.connect(self.on_action_qdialog)

    def on_action_test_message_box(self):
        QMessageBox.information(self._iface.mainWindow(), 'Info', 'Hello World!')

    def on_action_qdialog(self):
        dialog = MyDialog(self)

        dialog.exec()

    def unload(self):
        del self._toolbar


if __name__ == '__main__':
    pass
