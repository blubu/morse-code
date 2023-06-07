
from PyQt5.QtWidgets import *

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
window.setGeometry(400, 250, 500, 500)

dropdown = QComboBox(window)
dropdown.setGeometry(150, 230, 100, 20)
dropdown.addItem('-- Text to Morse --')
dropdown.addItem('-- Morse to Text --')

textbox = QLineEdit(window)
textbox.setGeometry(150, 250, 150, 20)

button = QPushButton("Convert", window)
button.setGeometry(310, 250, 70, 20)

label = QLabel("", window)
label.setGeometry(250, 300, 100, 100)


def morse_code(entered_text):
    res = ''
    for i in entered_text:
        res += morse_code_dict[i.upper()]
        res += ' '
    return res


def text_code(entered_text):
    res = ''
    text = entered_text.split(' / ')
    for word in text:
        letter = word.split()
        for l in letter:
            res += text_code_dict[l]
        res += " "
    return res


def convert_button():
    if dropdown.currentIndex() == 0:
        res = morse_code(textbox.text())
    else:
        res = text_code(textbox.text())
    label.setText(res)


button.clicked.connect(convert_button)

window.show()

app.exec()
