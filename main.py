import sys

from PyQt5 import QtWidgets

from controller_cards.cards_controller import CardsController
from windows.u2y_main_window import U2YMainWindow


class MainWindow(U2YMainWindow):

    def __init__(self):
        super().__init__(geometry=(100, 100, 1000, 900))

        card_width = 700
        self.centralWidget().setSizes((self.geometry().width() - card_width, card_width))

        cards_controller = CardsController(self)
        self.rightTabWidget.setLayout(QtWidgets.QVBoxLayout())
        self.rightTabWidget.layout().addWidget(cards_controller)

        self.leftTabWidget.setLayout(QtWidgets.QVBoxLayout())

        btn_add_1 = QtWidgets.QPushButton("Add card 1")
        btn_add_1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        btn_add_1.clicked.connect(
            lambda x: cards_controller.list_view.model().insertRow(cards_controller.list_view.model().rowCount(), card_type="arms"))
        self.leftTabWidget.layout().addWidget(btn_add_1)

        btn_add_2 = QtWidgets.QPushButton("Add card 2")
        btn_add_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        btn_add_2.clicked.connect(
            lambda x: cards_controller.list_view.model().insertRow(cards_controller.list_view.model().rowCount(), card_type="back"))
        self.leftTabWidget.layout().addWidget(btn_add_2)

        btn_save = QtWidgets.QPushButton("Save card")
        btn_save.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.leftTabWidget.layout().addWidget(btn_save)

        btn_del = QtWidgets.QPushButton("Remove card")
        btn_del.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.leftTabWidget.layout().addWidget(btn_del)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
