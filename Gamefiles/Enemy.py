from PyQt5.QtWidgets import QMainWindow, QLabel
from random import randint, choice
import tkinter as tk
from PyQt5 import uic

import Abbilities

root = tk.Tk()
X = root.winfo_screenwidth()
Y = root.winfo_screenheight()
trigger_to_die = 0


class Basic_enemy(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vrag_smile_face.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('Обычный враг')
        self.count = 1
        self.heatpoints.setText(str(self.count))
        self.difficult = 1

    def closeEvent(self, event):
        global trigger_to_die
        if self.count == 1:
            trigger_to_die -= 1
            event.accept()
        else:
            self.count -= 1
            self.heatpoints.setText(str(self.count))
            event.ignore()


class Big_Enemy(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vrag_reklama_avaiseils.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('Большой враг')
        self.count = 3
        self.heatpoints.setText(str(str(self.count)))
        self.difficult = 1

    def closeEvent(self, event):
        global trigger_to_die
        if self.count == 1:
            trigger_to_die -= 1
            event.accept()
        else:
            self.count -= 1
            self.heatpoints.setText(str(self.count))
            event.ignore()


class Giant_Enemy(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vrag_reklama_Luba.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('Огромный враг')
        self.count = 7
        self.heatpoints.setText(str(str(self.count)))
        self.difficult = 3

    def closeEvent(self, event):
        global trigger_to_die
        if self.count == 1:
            trigger_to_die -= 1
            event.accept()
        else:
            self.count -= 1
            self.heatpoints.setText(str(self.count))
            event.ignore()


class Teleporter(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vrag_emotionless.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('Пикселеходец')
        self.count = 2
        self.heatpoints.setText(str(self.count))
        self.difficult = 2
        self.Teleport(800)

    def closeEvent(self, event):
        global trigger_to_die
        if self.count == 1:
            trigger_to_die -= 1
            event.accept()
        else:
            self.count -= 1
            self.heatpoints.setText(str(self.count))
            event.ignore()


class Resizer(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('Размероменятель')
        self.count = 3
        self.heatpoints = QLabel(self)
        self.heatpoints.setText(str(self.count))
        self.design = QLabel(self)
        self.text = QLabel(self)
        self.text.move(250, 250)
        self.heatpoints.move(480, 0)
        self.difficult = 2
        self.Resize(600)
        self.Text_changer()

    def closeEvent(self, event):
        global trigger_to_die
        if self.count == 1:
            trigger_to_die -= 1
            event.accept()
        else:
            self.count -= 1
            self.heatpoints.setText(str(self.count))
            event.ignore()


class Duplicator(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vrag_angry.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('Синяя птичка из Angry birds')
        self.count = 3
        self.heatpoints.setText(str(self.count))
        self.difficult = 3

    def closeEvent(self, event):
        global dupl1
        global dupl2
        dupl1 = Duplicated1()
        dupl1.show()
        dupl2 = Duplicated2()
        dupl2.show()


class Duplicated1(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vrag_angry.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('Синяя птичка из Angry birds')
        self.count = 2
        self.heatpoints.setText(str(self.count))
        self.difficult = 0

    def closeEvent(self, event):
        global dupl3
        global dupl4
        dupl3 = Duplicated3()
        dupl3.show()
        dupl4 = Duplicated3()
        dupl4.show()


class Duplicated2(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vrag_angry.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('Синяя птичка из Angry birds')
        self.count = 2
        self.heatpoints.setText(str(self.count))
        self.difficult = 0

    def closeEvent(self, event):
        global dupl5
        global dupl6
        dupl5 = Duplicated3()
        dupl5.show()
        dupl6 = Duplicated3()
        dupl6.show()


class Duplicated3(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vrag_angry.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('Синяя птичка из Angry birds')
        self.count = 1
        self.heatpoints.setText(str(self.count))
        self.difficult = 0

    def closeEvent(self, event):
        global trigger_to_die
        trigger_to_die -= 1


class Boss(Abbilities.Skills, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vrag_demon_boss.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(randint(0, X - 500), randint(30, Y - 500), 500, 500)
        self.setWindowTitle('БОСС!!!')
        self.count = 5
        self.enemies_lvl2 = (Teleporter, Resizer, Giant_Enemy)
        self.heatpoints.setText(str(self.count))
        self.difficult = 4

    def closeEvent(self, event):
        global trigger_to_die, first_enemy, second_enemy
        if self.count == 1 and trigger_to_die == 0:
            event.accept()
        else:
            if trigger_to_die == 0:
                self.count -= 1
                trigger_to_die = 5
                first_chosen = choice(self.enemies_lvl2)
                first_enemy = first_chosen()
                first_enemy.show()
                second_enemy = Duplicator()
                second_enemy.show()
                self.heatpoints.setText(str(self.count))
                event.ignore()
            else:
                event.ignore()
