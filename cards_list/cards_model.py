import typing

import pandas as pd
from PyQt5.QtCore import *


class CardsModel(QAbstractListModel):

    def __init__(self, parent: typing.Optional[QObject] = ...) -> None:
        super().__init__(parent)

        self.items_list = []
        self.data_table = pd.DataFrame()

    def setData(self, index: QModelIndex, value: typing.Any, role: int = ...) -> bool:
        return super().setData(index, value, role)

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        return super().data(index, role)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.items_list)
