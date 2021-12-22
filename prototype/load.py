from toolbox import Toolbox
from feature import Feature 
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

        self.t3 = 5
        self.spinBox_3.setRange(5, 200)
        self.spinBox_3.valueChanged.connect(self.valuechange)
        self.spinBox_3.setSingleStep(5)
        # spinbox for number of trials

        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        # start recording pushbutton

        self.pushButton_6.setCheckable(True)
        self.pushButton_6.clicked.connect(self.the_end)
        # stop recording pushbutton

        self.checklist = ['EEG.AF3','EEG.F7','EEG.F3','EEG.FC5','EEG.T7','EEG.P7','EEG.O1','EEG.O2','EEG.P8','EEG.T8','EEG.FC6','EEG.F4','EEG.F8','EEG.AF4']
        self.mask = []
        self.channels = []

        self.pushButton_7.setCheckable(True)
        self.pushButton_7.clicked.connect(self.the_chosen_ones)




    def the_button_was_clicked(self):
        obj = Toolbox()
        # total_time = (self.t1 + self.t2)*self.t3
        obj.random_gen(self.t3)
        obj.stimuli(self.t1*1000,self.t2)
        

    def valuechange(self):
        self.t1 = self.spinBox.value()
        self.t2 = self.spinBox_2.value()
        self.t3 = self.spinBox_3.value()

    def the_end(self):
        sys.exit("Recording Stopped")

    def the_chosen_ones(self):
        self.mask = [self.AF3.isChecked(),self.F7.isChecked(),self.F3.isChecked(),self.FC5.isChecked(),self.T7.isChecked(),self.P7.isChecked(),self.O1.isChecked(),self.O2.isChecked(),self.P8.isChecked(),self.T8.isChecked(),self.FC6.isChecked(),self.F4.isChecked(),self.F8.isChecked(),self.AF4.isChecked()]
        # print(self.mask)
        self.channels = [x for x, y in zip(self.checklist, self.mask) if y == True]
        print(self.channels)





app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()