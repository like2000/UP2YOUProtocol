import typing

import pandas as pd
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from controller_cards.cards_widget import CardsWidget


class CardsModel(QAbstractListModel):

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.items_list = []

        try:
            self.data_table = pd.read_csv("res/store.csv")
        except IOError:
            self.data_table = pd.DataFrame(columns=["Index"])
            self.data_table.to_csv("res/store.csv")

        for i in range(2):
            self.items_list.append(CardsWidget())

    def setData(self, index: QModelIndex, value: typing.Any, role: int = ...) -> bool:
        return super().setData(index, value, role)

    @pyqtSlot()
    def insertRow(self, row: int, parent=QModelIndex(), card_type: str = "default") -> bool:
        self.beginInsertRows(parent, row - 1, row)
        self.items_list.append(CardsWidget(card_type))
        self.endInsertRows()

        return True

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:

        parent = self.parent()
        cw = self.items_list[index.row()]
        if not parent.indexWidget(index):
            parent.setIndexWidget(index, cw)

        if (role == Qt.FontRole):
            font = QFont("Nimbus Sans", 11, QFont.Bold)
            return font
        elif (role == Qt.SizeHintRole):
            size = QSize(cw.width() - 40, cw.height())
            return size
        elif role == Qt.DisplayRole:
            i = index.row()
            # r, g, b, a = self.color_scheme[i]
            # cw.setStyleSheet(f"""
            #             QFrame {{background-color: rgba({r}, {g}, {b}, {a});}}
            #             QFrame#Outer {{border: 2px solid lightgray; border-radius: 8px;}}
            #         """)
            # cw.textArea.setHtml(self.datatable.to_html())
            # return f'{self.items_list[i]}'
        elif (role == Qt.ForegroundRole and index.column() == 0):
            return QColor("orange")
        elif (role == Qt.ForegroundRole and index.column() == 1):
            return QColor("limegreen")
        else:
            return QVariant()

        # if role == Qt.DisplayRole:
        #     return self.items_list[index.row()]
        # elif role==Qt.SizeHintRole:
        #     return QSize(10, 100)
        # else:
        #     return QVariant()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.items_list)
