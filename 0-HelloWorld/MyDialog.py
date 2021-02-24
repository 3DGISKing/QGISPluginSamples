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
from qgis.PyQt.uic import loadUiType
from qgis.PyQt.QtWidgets import QDialog


FORM_CLASS, _ = loadUiType(os.path.join(os.path.dirname(__file__), 'MyDialog.ui'))


class MyDialog(QDialog, FORM_CLASS):
    def __init__(self, plugin):
        super(QDialog, self).__init__(None)
        self.setupUi(self)