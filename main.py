
from PyQt5.QtWidgets import *
from morse import MainWindow

# main function
if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow(app)
    window.show()

    app.exec()
