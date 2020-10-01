from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject
import matplotlib.pyplot as plt
import UI, Model
import sys, os

class LogPrinter(object):
    def __init__(self):
        self.buffer = ''
        sys.stdout = self

    def write(self, message):
        self.buffer += message

    def saveLog(self, path):
        with open(path, 'w') as fp:
            fp.write(self.buffer)

class SignalPacket(QObject):
    processBarSig = pyqtSignal(str, int)
    taskDoneSig = pyqtSignal(bool)
    dataParseSig = pyqtSignal(str, list, object)
    analysisSig = pyqtSignal(str, str, list)
    updateDbSig = pyqtSignal()

class Dispatcher(object):

    def __init__(self):
        self.ui = UI.Ui_Higgs()
        self.sigs = SignalPacket()
        self.parsedDataFrame = []
        self.db = ''
        self.report = ''

    def loadWidgetsOn(self, win):
        self.ui.setupUi(win)
        self.connectDatabase()
        self.parentWin = win

        # configurate signals
        # @ main button
        self.ui.openDataButton.clicked.connect(self.setDataPathByButton)
        self.ui.parseDataButton.clicked.connect(self.parseDataFile)
        self.ui.analyzeButton.clicked.connect(self.analyzeDataFrame)
        self.ui.captureLogButton.clicked.connect(self.saveLog)
        self.ui.openButtonForDB.clicked.connect(self.setDatabasePathByButton)
        self.ui.updateButtonForDB.clicked.connect(self.updateDatabase)
        self.ui.checkGeneButton.clicked.connect(self.checkGene)
        self.ui.genReportButton.clicked.connect(self.generateReport)
        # @ plot chromosome button
        self.ui.plotChr_1.clicked.connect(lambda: self.plotChrFigure(['1']))
        self.ui.plotChr_2.clicked.connect(lambda: self.plotChrFigure(['2']))
        self.ui.plotChr_3.clicked.connect(lambda: self.plotChrFigure(['3']))
        self.ui.plotChr_4.clicked.connect(lambda: self.plotChrFigure(['4']))
        self.ui.plotChr_5.clicked.connect(lambda: self.plotChrFigure(['5']))
        self.ui.plotChr_6.clicked.connect(lambda: self.plotChrFigure(['6']))
        self.ui.plotChr_7.clicked.connect(lambda: self.plotChrFigure(['7']))
        self.ui.plotChr_8.clicked.connect(lambda: self.plotChrFigure(['8']))
        self.ui.plotChr_9.clicked.connect(lambda: self.plotChrFigure(['9']))
        self.ui.plotChr_10.clicked.connect(lambda: self.plotChrFigure(['10']))
        self.ui.plotChr_11.clicked.connect(lambda: self.plotChrFigure(['11']))
        self.ui.plotChr_12.clicked.connect(lambda: self.plotChrFigure(['12']))
        self.ui.plotChr_13.clicked.connect(lambda: self.plotChrFigure(['13']))
        self.ui.plotChr_14.clicked.connect(lambda: self.plotChrFigure(['14']))
        self.ui.plotChr_15.clicked.connect(lambda: self.plotChrFigure(['15']))
        self.ui.plotChr_16.clicked.connect(lambda: self.plotChrFigure(['16']))
        self.ui.plotChr_17.clicked.connect(lambda: self.plotChrFigure(['17']))
        self.ui.plotChr_18.clicked.connect(lambda: self.plotChrFigure(['18']))
        self.ui.plotChr_19.clicked.connect(lambda: self.plotChrFigure(['19']))
        self.ui.plotChr_20.clicked.connect(lambda: self.plotChrFigure(['20']))
        self.ui.plotChr_21.clicked.connect(lambda: self.plotChrFigure(['21']))
        self.ui.plotChr_22.clicked.connect(lambda: self.plotChrFigure(['22']))
        self.ui.plotChr_X.clicked.connect(lambda: self.plotChrFigure(['X']))
        var = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X']
        self.ui.plotChr_all.clicked.connect(lambda: self.plotChrFigure(var))
        # @ user-defined signals
        self.sigs.processBarSig.connect(self.processBarShow)
        self.sigs.taskDoneSig.connect(self.setTaskEnabled)
        self.sigs.dataParseSig.connect(self.showParsedResult)
        self.sigs.analysisSig.connect(self.showAnalysis)
        self.sigs.updateDbSig.connect(self.connectDatabase)

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
        self.widgetList.append(self.ui.openButtonForDB)

    def setLogger(self, logger):
        self.logger = logger

    def saveLog(self):
        filePath, fileType = QFileDialog.getSaveFileName(self.parentWin, 'Save as', 'higgs_log', 
                                                        'Log(*.log)')
        self.logger.saveLog(filePath)

    def setTaskEnabled(self, flag):
        for item in self.widgetList:
            item.setEnabled(flag)

    def connectDatabase(self):
        try:
            fp = open('db', encoding='UTF-8')
        except FileNotFoundError:
            info = 'There is no database!!!\nPlease update the database~'
            self.ui.databaseInfo.setText(info)
            return
        else:
            self.db = eval(fp.read())
            info = 'The current database:'
            info += '\nGenerated by file: ' + self.db['file']
            info += '\nUpdated on date: ' + self.db['date']
            self.ui.databaseInfo.setText(info)
            self.ui.gene.clear()
            self.ui.gene.addItems(list(self.db.keys())[2:])

    def showParsedResult(self, path, candidate, dataFrame):
        self.ui.parsedFileLabel.setText(path)
        self.ui.candidate.clear()
        self.ui.candidate.addItems(candidate)
        self.parsedDataFrame = dataFrame
        keepColumns = ['Gene1']
        for item in candidate:
            keepColumns.append(item + '_Scale')
        self.dataIndexSetChr = dataFrame.set_index('Chr')
        self.dataIndexSetChr = self.dataIndexSetChr[keepColumns]


    def plotChrFigure(self, chromosome):
        if type(self.parsedDataFrame) == list:
            QMessageBox.information(self.parentWin, "Information", "Please parse the data")
            return

        checkedId = self.ui.candidate.currentText() + '_Scale'
        idList = list(self.dataIndexSetChr.columns)
        idList.remove('Gene1')
        idList.remove(checkedId)
        idList.append(checkedId)

        for chr in chromosome:
            data = self.dataIndexSetChr.loc[chr]
            x = list(data['Gene1'])
            yList = []
            for item in idList:
                yList.append(list(data[item]))

            plt.figure()
            plt.xticks([])
            for y in yList:
                plt.plot(x, y)
            plt.legend(tuple(idList))

        plt.show()

    def showAnalysis(self, checkedId, summary, resultList):
        self.ui.showResultLabel.setText(summary)
        self.report = [checkedId, summary, resultList]

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

    def setDatabasePathByButton(self):
        filePath, fileType = QFileDialog.getOpenFileName(self.parentWin, 'Select Data File', '', 
                                                        'Spreadsheet(*.xlsx *.csv)')
        self.ui.inputDatabaseFile.setText(filePath)

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
            Model.ParseDataThread(path, self.sigs.taskDoneSig, self.sigs.dataParseSig).start()
            Model.TaskTimerThread('parsing', path, self.sigs.processBarSig, self.widgetList).start()

    def updateDatabase(self):
        path = self.ui.inputDatabaseFile.text()

        if not path:
            QMessageBox.information(self.parentWin, "Information", "Please fill the file path")
        elif not os.path.isfile(path):
            QMessageBox.information(self.parentWin, "Information", "The file does not exist")
        elif path[-4:] !='.csv' and path[-5:] != '.xlsx':
            QMessageBox.information(self.parentWin, "Information", "It is not supported file type")
        else:
            # trigger thread
            Model.UpdateDatabaseThread(path, self.sigs.taskDoneSig, self.sigs.updateDbSig).start()
            Model.TaskTimerThread('updating', 3, self.sigs.processBarSig, self.widgetList).start()
        
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

    def checkGene(self):
        checkedGene = self.ui.gene.currentText()
        self.ui.textBrowser.setText(self.db[checkedGene])

    def generateReport(self):
        if not self.report:
            QMessageBox.information(self.parentWin, "Information", "Please analyze the data")
        else:
            filePath, fileType = QFileDialog.getSaveFileName(self.parentWin, 'Save as', self.report[0], 
                                                        'Report(*.txt)')
            if not filePath:
                return
            Model.GenerateReportThread(filePath, self.report, self.db, self.parsedDataFrame).start()

#---------------------------------
# Main Entry
#---------------------------------
if __name__ == '__main__':
    # generate error dump
    fp = open('dump.log', 'w')
    sys.stderr = fp
    # instantiate dispatcher and logger
    dp = Dispatcher()
    log = LogPrinter()
    dp.setLogger(log)
    # run app
    app = QApplication(sys.argv)
    win = QMainWindow()
    dp.loadWidgetsOn(win)
    win.show()
    sys.exit(app.exec_())