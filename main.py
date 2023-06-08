
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', '#': '-.-.---', '<': '-.-.-',
    '>': '.-.--', ' ': '/'
}

text_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
    '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/',
    '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-',
    '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '-.-.---': '#', '-.-.-': '<', '.-.--': '>', '/': ' '
}


app = QApplication([])

window = QMainWindow()
window.setGeometry(500, 250, 600, 550)
window.setFixedSize(600, 500)

dropdown = QComboBox(window)
dropdown.setGeometry(175, 75, 250, 30)
dropdown.addItem('-- Text to Morse --')
dropdown.addItem('-- Morse to Text --')

textbox = QLineEdit(window)
textbox.setPlaceholderText("Enter text to be converted")
textbox.setGeometry(175, 110, 250, 30)

button = QPushButton("Convert", window)
button.setGeometry(350, 145, 75, 30)

label = QLabel('', window)
label.setGeometry(150, 220, 300, 25)
label.setFixedWidth(300)
label.setAlignment(Qt.AlignCenter)
label.setWordWrap(True)

copy_button = QPushButton(f"Copy", window)
copy_button.setGeometry(250, 400, 50, 35)


def morse_code(entered_text):
    res = ''
    for i in entered_text:
        res += morse_code_dict[i.upper()]
        res += ' '
    return res


def text_code(entered_text):
    res = ''
    text = entered_text.split()
    for i in text:
        res += text_code_dict[i]
    return res


def convert_button():
    if dropdown.currentIndex() == 0:
        res = morse_code(textbox.text())
    else:
        res = text_code(textbox.text())
    label.setText(res)


def copy():
    clipboard = QApplication.clipboard()
    clipboard.setText(label.text())
    QMessageBox.information(window, 'copy', 'Text copied to clipboard.')

button.clicked.connect(convert_button)
copy_button.clicked.connect(copy)

window.show()

app.exec()
