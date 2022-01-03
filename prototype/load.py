from toolbox import Toolbox
from feature import Feature
from plot import PlotEEG, PlotFFT 
import sys
import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QObject, QThread, pyqtSignal

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
        # pushbutton to update channel selection

        self.pushButton_8.setCheckable(True)
        self.btn_ctr = 2
        self.pushButton_8.clicked.connect(self.select_all_channels)
        # pushbutton to select all channels

        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(self.save_to_csv)

        self.pushButton_3.setCheckable(True)
        self.pushButton_3.clicked.connect(self.plot_raw)
        self.plot_eeg = PlotEEG(self.channels)

        self.pushButton_4.setCheckable(True)
        self.pushButton_4.clicked.connect(self.plot_fourier)
        self.plot_fft = PlotFFT(self.channels)




    def the_button_was_clicked(self):
        obj = Toolbox()
        # total_time = (self.t1 + self.t2)*self.t3
        obj.random_gen(self.t3)
        self.record_EEG()
        obj.stimuli(self.t1*1000,self.t2)
        

    def valuechange(self):
        self.t1 = self.spinBox.value()
        self.t2 = self.spinBox_2.value()
        self.t3 = self.spinBox_3.value()

    def the_end(self):
        sys.exit("Recording Stopped")

    def select_all_channels(self):
        if self.btn_ctr % 2 == 0:
            self.AF3.setChecked(True)
            self.F7.setChecked(True)
            self.F3.setChecked(True)
            self.FC5.setChecked(True)
            self.T7.setChecked(True)
            self.P7.setChecked(True)
            self.O1.setChecked(True)
            self.O2.setChecked(True)
            self.P8.setChecked(True)
            self.T8.setChecked(True)
            self.FC6.setChecked(True)
            self.F4.setChecked(True)
            self.F8.setChecked(True)
            self.AF4.setChecked(True)
        else:
            self.AF3.setChecked(False)
            self.F7.setChecked(False)
            self.F3.setChecked(False)
            self.FC5.setChecked(False)
            self.T7.setChecked(False)
            self.P7.setChecked(False)
            self.O1.setChecked(False)
            self.O2.setChecked(False)
            self.P8.setChecked(False)
            self.T8.setChecked(False)
            self.FC6.setChecked(False)
            self.F4.setChecked(False)
            self.F8.setChecked(False)
            self.AF4.setChecked(False)
            
        self.btn_ctr = self.btn_ctr + 1

    def the_chosen_ones(self):
        self.mask = [self.AF3.isChecked(),self.F7.isChecked(),self.F3.isChecked(),self.FC5.isChecked(),self.T7.isChecked(),self.P7.isChecked(),self.O1.isChecked(),self.O2.isChecked(),self.P8.isChecked(),self.T8.isChecked(),self.FC6.isChecked(),self.F4.isChecked(),self.F8.isChecked(),self.AF4.isChecked()]
        # print(self.mask)
        self.channels = [x for x, y in zip(self.checklist, self.mask) if y == True]
        # print(self.channels)
        self.plot_eeg = PlotEEG(self.channels)
        self.plot_fft = PlotFFT(self.channels)
    
    def save_to_csv(self):
        feat = Feature(self.channels, self.t3)
        if self.checkBox.isChecked():
            feat.relative_psd()
        # if self.checkBox_2.isChecked():
            # feat.psd()
        if self.checkBox_3.isChecked() :
            feat.wavelet()
    
    def plot_raw(self):
        self.plot_eeg.show()

    def plot_fourier(self):
        self.plot_fft.show()
    

        

    
    def record_EEG(self):
        self.thread = QThread()
        self.worker = Worker()

        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.start)
        self.worker.finished.connect(self.thread.quit)

        # display fixation cross till it actually start recording

        # self.worker.finished.connect(self.worker.deleteLater)
        
        # self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()



# worker thread to record EEG using Cortex API
class Worker(QObject):
    finished = pyqtSignal()

    def start(self):
        os.system("python C:/Users/KHALS/OneDrive/Desktop/professorX/record.py")
        self.finished.emit()
        # trial, find alternative way to emit if this does not work.

            
        






app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()