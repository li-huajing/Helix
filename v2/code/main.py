from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject
import UI, Model
import sys, os


class SignalPacket(QObject):
    processBarSig = pyqtSignal(str, int)
    TaskDoneSig = pyqtSignal(bool)
    dataFrameSig = pyqtSignal(str, list, object)

class Dispatcher(object):

    def __init__(self):
        self.ui = UI.Ui_Higgs()
        self.sigs = SignalPacket()
        self.parsedDataFrame = []

    def loadWidgetsOn(self, win):
        self.ui.setupUi(win)
        self.parentWin = win

        # configurate signals
        self.ui.openDataButton.clicked.connect(self.setDataPathByButton)
        self.ui.parseDataButton.clicked.connect(self.parseDataFile)
        #self.ui.captureLogButton.clicked.connect()
        #self.ui.openButtonForDB.clicked.connect()
        #self.ui.updateButtonForDB.clicked.connect()
        #self.ui.checkGeneButton.clicked.connect()
        #self.ui.analyzeButton.clicked.connect()
        #self.ui.checkChrButton.clicked.connect()
        #self.ui.genReportButton.clicked.connect()
        self.sigs.processBarSig.connect(self.processBarShow)
        self.sigs.TaskDoneSig.connect(self.setTaskEnabled)
        self.sigs.dataFrameSig.connect(self.showParsedResult)

        # when the thread is triggered, the following widgets can't be clicked
        # meantime the list is a flag to check whether the task done or not
        self.widgetList = []
        self.widgetList.append(self.ui.openDataButton)
        self.widgetList.append(self.ui.parseDataButton)
        self.widgetList.append(self.ui.analyzeButton)
        self.widgetList.append(self.ui.inputFilePath)
        self.widgetList.append(self.ui.checkChrButton)
        self.widgetList.append(self.ui.genReportButton)
        self.widgetList.append(self.ui.updateButtonForDB)
        self.widgetList.append(self.ui.candidate)

    def setTaskEnabled(self, flag):
        for item in self.widgetList:
            item.setEnabled(flag)

    def showParsedResult(self, path, candidate, dataFrame):
        self.ui.parsedFileLabel.setText(path)
        self.ui.candidate.clear()
        self.ui.candidate.addItems(candidate)
        self.parsedDataFrame = dataFrame

    def processBarShow(self, taskName, value):
        if taskName == 'parsing':
            self.ui.parsingBar.setValue(value)
        elif taskName == 'analyzing':
            self.ui.analyzingBar.setValue(value)
        elif taskName == 'updating':
            self.ui.updatingBar.setValue(value)

    def setDataPathByButton(self):
        filePath, fileType = QFileDialog.getOpenFileName(self.parentWin, 'Select Data File', '', 
                                                        'Spreadsheet(*.xlsx *.csv)')
        self.ui.inputFilePath.setText(filePath)

    def parseDataFile(self):
        path = self.ui.inputFilePath.text()

        if not path:
            QMessageBox.information(self.parentWin, "Information", "Please fill the file path")
        elif not os.path.isfile(path):
            QMessageBox.information(self.parentWin, "Information", "The file does not exist")
        elif path[-4:] !='.csv' and path[-5:] != '.xlsx':
            QMessageBox.information(self.parentWin, "Information", "It is not supported file type")
        else:
            self.parsedDataFrame = []
            self.ui.parsedFileLabel.setText('None')
            # trigger thread
            Model.ParseDataThread(path, self.sigs.TaskDoneSig, self.sigs.dataFrameSig).start()
            Model.TaskTimerThread('parsing', path, self.sigs.processBarSig, self.widgetList).start()
        



#---------------------------------
# Main Entry
#---------------------------------
if __name__ == '__main__':
    # instantiate dispatcher
    dp = Dispatcher()
    # run app
    app = QApplication(sys.argv)
    win = QMainWindow()
    dp.loadWidgetsOn(win)
    win.show()
    sys.exit(app.exec_())