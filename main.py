
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

app = QApplication([])

window = QMainWindow()
window.setGeometry(400, 250, 500, 500)

textbox = QLineEdit(window)
textbox.setGeometry(150, 250, 150, 20)

button = QPushButton("Convert", window)
button.setGeometry(310, 250, 70, 20)


def morse_code(entered_text):
    res = ''
    for i in entered_text:
        res += morse_code_dict[i.upper()]
        res += ' '
    return res


def convert_button():
    res = morse_code(textbox.text())
    print(res)


button.clicked.connect(convert_button)

window.show()

app.exec()
