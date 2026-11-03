import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget, 
    QPushButton, QVBoxLayout, QHBoxLayout
)
from pages.home import HomePage
from pages.checkin import CheckinPage
from pages.statistic import StatisticPage


app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Daily Mood")
window.resize(640, 640)

home = HomePage()
checkin = CheckinPage()
statistic = StatisticPage()

stack = QStackedWidget()
stack.addWidget(home)
stack.addWidget(checkin)
stack.addWidget(statistic)

def go_home():
    home.refresh()
    stack.setCurrentWidget(home)

def go_checkin():
    stack.setCurrentWidget(checkin)

def go_statistic():
    stack.setCurrentWidget(statistic)

home_btn = QPushButton("Home")
checkin_btn = QPushButton("Check in")
statistic_btn = QPushButton("Statistics")

home_btn.clicked.connect(go_home)
checkin_btn.clicked.connect(go_checkin)
statistic_btn.clicked.connect(go_statistic)

home.checkin_button.clicked.connect(go_checkin)

nav = QHBoxLayout()
nav.addWidget(home_btn)
nav.addWidget(checkin_btn)
nav.addWidget(statistic_btn)

container = QWidget()
main_layout = QVBoxLayout(container)
main_layout.addWidget(stack)
main_layout.addLayout(nav)

window.setCentralWidget(container)
window.show()

sys.exit(app.exec())