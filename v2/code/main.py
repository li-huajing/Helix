from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import UI
import sys, os


class Dispatcher(object):

    def __init__(self):
        self.ui = UI.Ui_Higgs()

    def loadWidgetOn(self, win):
        self.ui.setupUi(win)
        self.parentWin = win

        # configurate signals
        self.ui.openDataButton.clicked.connect(self.setDataPathByButton)
        #self.ui.captureLogButton.clicked.connect()
        #self.ui.openButtonForDB.clicked.connect()
        #self.ui.updateButtonForDB.clicked.connect()
        #self.ui.checkGeneButton.clicked.connect()
        #self.ui.parseDataButton.clicked.connect()
        #self.ui.analyzeButton.clicked.connect()
        #self.ui.checkChrButton.clicked.connect()
        #self.ui.genReportButton.clicked.connect()

    def setDataPathByButton(self):
        filePath, fileType = QFileDialog.getOpenFileName(self.parentWin, 'Select Data File', '', 
                                                        'Spreadsheet(*.xls *.xlsx *.csv)')
        self.ui.inputFilePath.setText(filePath)



#---------------------------------
# Main Entry
#---------------------------------
if __name__ == '__main__':
    # instantiiate dispatcher
    dp = Dispatcher()
    # run app
    app = QApplication(sys.argv)
    win = QMainWindow()
    dp.loadWidgetOn(win)
    win.show()
    sys.exit(app.exec_())