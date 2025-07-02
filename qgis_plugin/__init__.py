"""
This file initializes the QGIS plugin package.
"""

def classFactory(iface):
    from .main import MyPlugin
    return MyPlugin(iface)