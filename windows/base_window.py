from PyQt5 import QtCore
from PyQt5 import QtWidgets


class BaseWindow(QtWidgets.QMainWindow):

    def __init__(self, geometry, parent=None):
        super().__init__(parent=parent)

        self.initUi(geometry)

    def initUi(self, geometry):
        self.setWindowTitle("Base application")
        self.setGeometry(*geometry)
