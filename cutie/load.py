import sys
import os
from PyQt6 import QtWidgets, uic

from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("ProfessorX")

        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.the_button_was_clicked)



    def the_button_was_clicked(self):
        os.system("python C:/Users/KHALS/OneDrive/Desktop/professorX/toolbox/stimuli.py")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()