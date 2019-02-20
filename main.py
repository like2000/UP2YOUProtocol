import sys

from PyQt5 import QtWidgets

from cards_list.cards_delegate import CardsDelegate
from cards_list.cards_model import CardsModel
from windows.u2y_main_window import U2YMainWindow


class MainWindow(U2YMainWindow):

    def __init__(self):
        super().__init__(geometry=(100, 100, 1000, 900))

        card_width = 700
        self.centralWidget().setSizes((self.geometry().width()-card_width, card_width))

        self.list_view.setSpacing(20) # 40)
        self.list_view.setModel(CardsModel(self.list_view))
        # self.list_view.setItemDelegate(CardsDelegate(self.list_view))
        # model = self.list_view.model()
        # for i in range(10):
        #     model.insertRows(i, 1, QtCore.QModelIndex())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
