from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from random import randint, choice
import tkinter as tk

root = tk.Tk()
X = root.winfo_screenwidth()
Y = root.winfo_screenheight()
list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', '=', '@', '$', '&', '*', '1', '2', '3', '4', '5']
new_text = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
trigger_to_change_letter = -1


class Skills(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ResTimer = QTimer()
        self.TPtimer = QTimer()
        self.TextTimer = QTimer()
        self.Trigger_timer = QTimer()
        self.Trigger_timer.timeout.connect(self.text_rewrighter)
        self.Trigger_timer.start(100)

    def size_change(self):
        k = randint(30, 800)
        self.resize(k, k)
        self.heatpoints.move(k - 20, 0)
        self.text.move(k // 2, k // 2)

    def Resize(self, time):
        self.ResTimer.timeout.connect(self.size_change)
        self.ResTimer.start(time)

    def coordinate_changer(self):
        New_x = randint(0, X - 500)
        New_y = randint(0, Y - 500)
        self.move(New_x, New_y)

    def Teleport(self, time):
        self.TPtimer.timeout.connect(self.coordinate_changer)
        self.TPtimer.start(time)


    def text_rewrighter(self):
        global new_text, trigger_to_change_letter
        if trigger_to_change_letter != 3:
            trigger_to_change_letter += 1
        else:
            trigger_to_change_letter = 0
        if trigger_to_change_letter == 0:
            new_text[0] = choice(list_of_letters)
            new_text[4] = choice(list_of_letters)
        if trigger_to_change_letter == 1:
            new_text[1] = choice(list_of_letters)
            new_text[5] = choice(list_of_letters)
        if trigger_to_change_letter == 2:
            new_text[2] = choice(list_of_letters)
            new_text[6] = choice(list_of_letters)
        if trigger_to_change_letter == 3:
            new_text[3] = choice(list_of_letters)
            new_text[7] = choice(list_of_letters)

    def Text_changer(self):
        self.TextTimer.timeout.connect(lambda: self.text.setText(''.join(new_text)))
        self.TextTimer.start(100)
