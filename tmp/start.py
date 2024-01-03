from Enemy import *
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
enemy = Basic_enemy()
enemy.show()
app.exec()
