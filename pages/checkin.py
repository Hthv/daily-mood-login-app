from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QStackedWidget
)
from PySide6.QtCore import Qt

class CheckinPage(QWidget):
    def __init__(self):
        super().__init__()

        self.steps = QStackedWidget()
        self.steps.addWidget(self.build_mood_step())
        self.steps.addWidget(self.build_description_step())
        self.steps.addWidget(self.build_photo_step())

        self.back_button = QPushButton("Back")
        self.next_button = QPushButton("Next")
        self.back_button.clicked.connect(self.go_back)
        self.next_button.clicked.connect(self.go_next)

        buttons = QHBoxLayout()
        buttons.addWidget(self.back_button)
        buttons.addWidget(self.next_button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.steps)
        layout.addLayout(buttons)
        self.update_buttons()

    def build_mood_step(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("Step 1 : How do you feel today?"))
        return page

    def build_description_step(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("Step 2 : Describe your day."))
        return page
    
    def build_photo_step(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("Step 3 : Take a photo! "))
        return page
    
    def go_next(self):
        current = self.steps.currentIndex()
        if current < 2:
            self.steps.setCurrentIndex(current + 1)
        self.update_buttons()

    def go_back(self):
        current = self.steps.currentIndex()
        if current == 0:
            self.steps.setCurrentIndex(current - 1)
        self.update_buttons()

    def update_buttons(self):
        current = self.steps.currentIndex()
        self.back_button.setEnabled(current > 0)
        if (current == 2):
            self.next_button.setText("Save")
        else:
            self.next_button.setText("Next")