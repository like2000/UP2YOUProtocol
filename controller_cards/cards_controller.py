from PyQt5.QtWidgets import *

from controller_cards.cards_model import CardsModel


class CardsController(QTabWidget):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.list_view = QListView()
        self.list_view.setSpacing(20)  # 40)
        self.list_view.setModel(CardsModel(self.list_view))
        # self.list_view.setItemDelegate(CardsDelegate(self.list_view))
        # model = self.list_view.model()
        # for i in range(10):
        #     model.insertRows(i, 1, QtCore.QModelIndex())

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.list_view)