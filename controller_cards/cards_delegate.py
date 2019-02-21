from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from controller_cards.cards_widget import CardsWidget


class CardsDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    # def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
    #     return CardsWidget(parent)

    def updateEditorGeometry(self, editor: QWidget, option: 'QStyleOptionViewItem', index: QModelIndex) -> None:
        editor.setGeometry(option.rect)

    def sizeHint(self, option: 'QStyleOptionViewItem', index: QModelIndex) -> QSize:
        return CardsWidget().sizeHint()

    def paint(self, painter: QPainter, option: 'QStyleOptionViewItem', index: QModelIndex) -> None:
        cw = CardsWidget()

        # cw = QFrame()
        # cw.setObjectName("Outer")
        # cw.setStyleSheet("""
        #     QFrame {background-color: whitesmoke;}
        #     QFrame#Outer {border: 2px solid lightgray; border-radius: 8px;}
        # """)
        #
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(2, 2)
        effect.setBlurRadius(15)
        effect.setColor(QColor("black"))
        # cw.setGraphicsEffect(effect)
        #
        # textArea = QTextEdit()
        # textArea.setStyleSheet("""
        #     background-color: transparent;
        # """)
        # cw.setLayout(QVBoxLayout())
        # cw.layout().addWidget(textArea)

        cw.setGeometry(option.rect)

        painter.save()
        painter.translate(option.rect.topLeft())
        cw.render(painter, QPoint(), QRegion(), QWidget.DrawChildren)
        # effect.draw(painter, QPoint(), QRegion(), QWidget.DrawChildren)
        painter.drawLine(0, 0, 300, 0)
        painter.restore()

    # QPushButton
    # button(index.data().toString());
    # button.setGeometry(option.rect);
    # painter->save();
    # painter->translate(option.rect.topLeft());
    # button.render(painter);
    # painter->restore();
