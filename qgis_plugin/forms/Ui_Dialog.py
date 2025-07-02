from pkg_resources import resource_filename

from qgis.PyQt import QtWidgets, uic


FORM_CLASS, _ = uic.loadUiType("qgis_plugin/forms/dialog.ui")

class Ui_Dialog(QtWidgets.QDockWidget, FORM_CLASS):


    def __init__(self, parent=None):
        """Constructor."""
        super(Ui_Dialog, self).__init__(parent)
        # self.setupUi(self)

    def connectButtons(self):
        self.buttonOk.clicked.connect(self.ok)
        # raise Exception
        self.buttonCancel.clicked.connect(self.cancel)

    def ok(self):
        raise Exception

    def cancel(self):
        print('bla')
        self.close()
