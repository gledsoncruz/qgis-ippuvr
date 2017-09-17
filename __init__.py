# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IPPUVR
                                 A QGIS plugin
 Plugin com várias funcionalidades para arender a Prefeitura Municipal de Volta Redonda
                             -------------------
        begin                : 2017-09-17
        copyright            : (C) 2017 by Gledson Cruz / IPPUVR
        email                : gledson.cruz@gmail.com
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
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load IPPUVR class from file IPPUVR.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cadastro import IPPUVR
    return IPPUVR(iface)
