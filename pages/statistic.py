from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

class StatisticPage(QWidget):
    def __init__(self):
        super().__init__()

        title = QLabel("Statistics Page")
        title.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(title)