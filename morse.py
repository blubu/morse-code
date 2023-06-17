
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from convert import Converter


# main window class
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setGeometry(500, 250, 600, 550)
        self.setFixedSize(600, 500)
        self.setStyleSheet("QMainWindow {background-color: black;}")

        self.icon = QIcon('./images/morse_icon.png')
        self.setWindowIcon(self.icon)
        self.setWindowTitle('  Morse Code Convertor')

        self.dropdown = QComboBox(self)
        self.textbox = QLineEdit(self)
        self.button = QPushButton("Convert", self)
        self.label = QLabel('', self)
        self.copy_button = QPushButton(f"Copy", self)
        self.widgets()

        # button clicked events
        self.button.clicked.connect(self.convert_button)
        self.copy_button.clicked.connect(self.copy)

    def widgets(self):
        # dropdown menu
        self.dropdown.setGeometry(175, 75, 250, 30)
        self.dropdown.addItem('--- Text to Morse ---')
        self.dropdown.addItem('--- Morse to Text ---')

        # input box
        self.textbox.setPlaceholderText("Enter text to be converted")
        self.textbox.setGeometry(175, 110, 250, 30)
        self.textbox.setStyleSheet("border-radius: 3px;font-family: Courier New;")

        # convert button
        self.button.setGeometry(350, 145, 75, 30)
        self.button.setStyleSheet("QPushButton {font-weight: bold;background-color:orange;border-radius: 5px;}"
                                  "QPushButton:hover {background-color: black;color: orange;"
                                  "border-radius: 5px;border-style: solid;"
                                  "border-width: 1px;border-color: orange}")

        # output label
        self.label.setGeometry(75, 220, 450, 25)
        self.label.setFixedWidth(450)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("font-weight: bold;"
                                 "color: white;")

        # copy to clipboard button
        self.copy_button.setGeometry(272, 400, 56, 35)
        self.copy_button.setToolTip("Copy result to clipboard")
        self.copy_button.setStyleSheet("QPushButton {font-weight: bold;background-color:orange;border-radius: 5px;}"
                                       "QPushButton:hover {background-color: black;color: orange;"
                                       "border-radius: 5px;border-style: solid;"
                                       "border-width: 1px;border-color: orange}")
        self.copy_button.hide()

    # convert button function
    def convert_button(self):
        if self.dropdown.currentIndex() == 0:
            res = Converter.morse_code(self.textbox.text())
        else:
            res = Converter.text_code(self.textbox.text())

        if res == '':
            self.label.setText('No Input Found...')
            self.copy_button.hide()
        elif res == 'Invalid Input !!':
            self.label.setText(res)
            self.copy_button.hide()
        else:
            self.label.setText(res)
            self.label.setFixedHeight(self.label.sizeHint().height())
            self.copy_button.show()

    # copy button function
    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.label.text())

    # keypress function
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.app.quit()
        if event.key() == Qt.Key_Right or event.key() == Qt.Key_Left:
            if self.dropdown.currentIndex() == 0:
                self.dropdown.setCurrentIndex(1)
            else:
                self.dropdown.setCurrentIndex(0)

