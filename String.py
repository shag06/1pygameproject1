# -*- coding: utf-8 -*-
import sys
import random
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('random_string.ui', self)  # Загружаем дизайн
        self.get.clicked.connect(self.get_string)

    def get_string(self):
        if not lst:
            s = "Empty file!"
        else:
            s = "".join([elem + "\n" for elem in lst[1::2] + lst[::2]])
        try:
            self.result.setPlaceholderText(s)
        except Exception as ex:
            print(ex.__class__.__name__)


if __name__ == '__main__':
    name = "lines.txt"
    flag = True
    while flag:
        try:
            f = open(name, "r")
            flag = False
        except Exception:
            print(f"File {name} not found. Please, write new place")
            name = input()
    lst = [elem.rstrip() for elem in f.readlines()]
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())