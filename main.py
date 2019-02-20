import sys

from PyQt5 import QtWidgets

from cards_list.cards_model import CardsModel
from windows.u2y_main_window import U2YMainWindow


class MainWindow(U2YMainWindow):

    def __init__(self):
        super().__init__(geometry=(200, 200, 1200, 800))

        self.centralWidget().setSizes((300, 600))

        self.list_view.setModel(CardsModel(self.list_view))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
