
from PyQt5.QtWidgets import *

app = QApplication([])

window = QMainWindow()
window.setGeometry(400, 250, 500, 500)

textbox = QLineEdit(window)
textbox.setGeometry(150, 250, 150, 20)

button = QPushButton("Convert", window)
button.setGeometry(310, 250, 70, 20)

window.show()

app.exec()
