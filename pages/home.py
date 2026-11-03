from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
from datetime import date
import storage

class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        self.message = QLabel("Havent checked in.\nCheck in today!")
        self.message.setAlignment(Qt.AlignCenter)

        self.checkin_button = QPushButton("Check in")

        layout = QVBoxLayout(self)
        layout.addWidget(self.message)
        layout.addWidget(self.checkin_button)
        self.refresh()

    def refresh(self):
        today = date.today().isoformat()
        checkin = storage.get_by_date(today)

        if checkin is None:
            self.message.setText("Havent checked in.\nCheck in today!")
            self.checkin_button.show()
        else:
            self.message.setText(f"Today's mood : {checkin['mood']}")
            self.checkin_button.hide()
