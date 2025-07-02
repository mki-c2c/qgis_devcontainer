"""
/qgis_plugin/qgis_plugin/main.py
"""

from qgis.core import QgsProcessingAlgorithm, QgsProcessingParameterNumber
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtWidgets import QAction, QDialog
from .forms.Ui_Dialog import Ui_Dialog

class MyPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.dialog = None

    def initGui(self):
        self.action = QAction(QCoreApplication.translate("MyPlugin", "My Plugin"), self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu(QCoreApplication.translate("MyPlugin", "My Plugin"), self.action)

    def unload(self):
        self.iface.removePluginMenu(QCoreApplication.translate("MyPlugin", "My Plugin"), self.action)

    def run(self):
        try:
            import debugpy
            debugpy.listen(("0.0.0.0", 5679))
        except:
            pass
        if not self.dialog:
            self.dialog = QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.dialog)
            self.ui.connectButtons()
        self.dialog.show()