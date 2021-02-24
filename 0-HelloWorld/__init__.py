# -*- coding: utf-8 -*-


# noinspection PyPep8Naming
def classFactory(iface):
    """
    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #

    from .HelloWorld import HelloWorld

    return HelloWorld(iface)
