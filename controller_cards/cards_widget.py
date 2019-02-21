from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CardsWidget(QFrame):

    def __init__(self, card_type="default", parent=None) -> None:
        super().__init__(parent=parent)

        self.initUi(card_type)

    def initUi(self, card_type):
        self.setFixedHeight(280)
        if card_type == "default":
            self.setObjectName("Default")
        elif card_type == "arms":
            self.setObjectName("Arms")
        elif card_type == "back":
            self.setObjectName("Back")
        self.setStyleSheet("""
            QFrame#Default {background-color: whitesmoke;
                border: 2px solid rgba(160, 160, 160, 1); border-radius: 8px;}
            QFrame#Arms {background-color: lavender;
                border: 2px solid rgba(160, 160, 160, 1); border-radius: 8px;}
            QFrame#Back {background-color: darkseagreen;
                border: 2px solid rgba(160, 160, 160, 1); border-radius: 8px;}
        """)

        effect = QGraphicsDropShadowEffect()
        effect.setOffset(2, 2)
        effect.setBlurRadius(15)
        effect.setColor(QColor("black"))
        self.setGraphicsEffect(effect)

        self.textArea = QTextEdit()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.textArea)
        self.textArea.setStyleSheet("""
            background-color: transparent;
        """)
