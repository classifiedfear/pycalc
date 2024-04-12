from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QGridLayout, QPushButton

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class PyCalcWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('PyCalc')
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()

        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        buttonLayout = QGridLayout()
        keyBoard = [
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', '('],
            ['1', '2', '3', '-', ')'],
            ['0', '00', '.', '+', '=']
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonLayout.addWidget(self.buttonMap[key], row, col)
        self.generalLayout.addLayout(buttonLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    @property
    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')