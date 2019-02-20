from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CardsWidget(QFrame):

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.initUi()

    def initUi(self):
        self.setFixedHeight(280)
        self.setObjectName("Outer")
        self.setStyleSheet("""
            QFrame {background-color: whitesmoke;}
            QFrame#Outer {border: 2px solid lightgray; border-radius: 8px;}
        """)
        # rgba(64, 64, 64, 1)

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
