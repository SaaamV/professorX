from toolbox import Toolbox 
import sys
from PyQt6 import QtWidgets, uic

from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("ProfessorX")

        self.t1 = 1
        self.spinBox.setMinimum(1)
        self.spinBox.valueChanged.connect(self.valuechange)
        # spinBox for time period for which each cue is displayed


        self.t2 = 0
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.valueChanged.connect(self.valuechange)
        # spinBox for buffer time period between two cues.

        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.the_button_was_clicked)



    def the_button_was_clicked(self):
        obj = Toolbox()
        obj.stimuli(self.t1*1000,self.t2*1000)
        

    def valuechange(self):
        self.t1 = self.spinBox.value()
        self.t2 = self.spinBox_2.value()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()