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

        self.frame = QtWidgets.QFrame()
        splitter.addWidget(self.frame)

        self.list_view = QtWidgets.QListView()
        splitter.addWidget(self.list_view)

        self.show()
