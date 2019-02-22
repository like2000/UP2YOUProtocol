from PyQt5 import QtCore
from PyQt5 import QtWidgets


class U2YMainWindow(QtWidgets.QMainWindow):

    def __init__(self, geometry, parent=None):
        super().__init__(parent=parent)

        self.initUi(geometry)

    def initUi(self, geometry):
        self.setWindowTitle("Up2You Protokoll")
        self.setGeometry(*geometry)
        with open("res/application_stylesheet.qss", "r") as fh:
            self.setStyleSheet(fh.read())

        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.setCentralWidget(splitter)

        self.leftTabWidget = QtWidgets.QTabWidget()
        splitter.addWidget(self.leftTabWidget)

        self.rightTabWidget = QtWidgets.QTabWidget()
        splitter.addWidget(self.rightTabWidget)

        self.show()
