from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject
import UI, Model
import sys, os


class SignalPacket(QObject):
    processBarSig = pyqtSignal(str, int)
    taskDoneSig = pyqtSignal(bool)
    dataFrameSig = pyqtSignal(str, list, object)
    analysisSig = pyqtSignal(str, list)

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
        self.ui.analyzeButton.clicked.connect(self.analyzeDataFrame)
        #self.ui.captureLogButton.clicked.connect()
        #self.ui.openButtonForDB.clicked.connect()
        #self.ui.updateButtonForDB.clicked.connect()
        #self.ui.checkGeneButton.clicked.connect()
        #self.ui.checkChrButton.clicked.connect()
        #self.ui.genReportButton.clicked.connect()
        self.sigs.processBarSig.connect(self.processBarShow)
        self.sigs.taskDoneSig.connect(self.setTaskEnabled)
        self.sigs.dataFrameSig.connect(self.showParsedResult)
        self.sigs.analysisSig.connect(self.showAnalysis)

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
        self.widgetList.append(self.ui.checkDad)
        self.widgetList.append(self.ui.checkMom)

    def setTaskEnabled(self, flag):
        for item in self.widgetList:
            item.setEnabled(flag)

    def showParsedResult(self, path, candidate, dataFrame):
        self.ui.parsedFileLabel.setText(path)
        self.ui.candidate.clear()
        self.ui.candidate.addItems(candidate)
        self.parsedDataFrame = dataFrame

    def showAnalysis(self, summary, resultList):
        self.ui.showResultLabel.setText(summary)


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
            Model.ParseDataThread(path, self.sigs.taskDoneSig, self.sigs.dataFrameSig).start()
            Model.TaskTimerThread('parsing', path, self.sigs.processBarSig, self.widgetList).start()
        
    def analyzeDataFrame(self):
        path = self.ui.parsedFileLabel.text()
        checkedId = self.ui.candidate.currentText()
        checkedDad = self.ui.checkDad.isChecked()
        checkedMom = self.ui.checkMom.isChecked()
        minScale = self.ui.minScale.text()
        maxScale = self.ui.maxScale.text()
        minHori = self.ui.minHori.text()
        data = self.parsedDataFrame

        param = [data, path, checkedId, checkedDad, checkedMom, minScale, maxScale, minHori]

        if type(data) == list:
            QMessageBox.information(self.parentWin, "Information", "Please parse the data")
        else:
            Model.AnalyzeDataThread(param, self.sigs.taskDoneSig, self.sigs.analysisSig).start()
            Model.TaskTimerThread('analyzing', 3, self.sigs.processBarSig, self.widgetList).start()


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