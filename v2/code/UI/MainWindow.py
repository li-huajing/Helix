# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Higgs(object):
    def setupUi(self, Higgs):
        Higgs.setObjectName("Higgs")
        Higgs.setWindowModality(QtCore.Qt.NonModal)
        Higgs.setEnabled(True)
        Higgs.resize(960, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Higgs.sizePolicy().hasHeightForWidth())
        Higgs.setSizePolicy(sizePolicy)
        Higgs.setMinimumSize(QtCore.QSize(0, 0))
        Higgs.setMaximumSize(QtCore.QSize(960, 600))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        Higgs.setFont(font)
        Higgs.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Higgs.setWindowOpacity(1.0)
        Higgs.setAutoFillBackground(False)
        self.aboutInfoFrame = QtWidgets.QFrame(Higgs)
        self.aboutInfoFrame.setGeometry(QtCore.QRect(190, 0, 771, 601))
        self.aboutInfoFrame.setAutoFillBackground(False)
        self.aboutInfoFrame.setStyleSheet("background-color: rgb(219, 255, 225);")
        self.aboutInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.aboutInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aboutInfoFrame.setObjectName("aboutInfoFrame")
        self.captureLogButton = QtWidgets.QPushButton(self.aboutInfoFrame)
        self.captureLogButton.setGeometry(QtCore.QRect(620, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.captureLogButton.setFont(font)
        self.captureLogButton.setStyleSheet("QPushButton{background-color: rgb(85, 255, 255);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(165, 255, 255);}")
        self.captureLogButton.setObjectName("captureLogButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.aboutInfoFrame)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 50, 581, 41))
        self.textBrowser_2.setStyleSheet("background-color: rgb(96, 205, 255);\n"
"border:none;\n"
"border-radius:4px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.databaseFuncFrame = QtWidgets.QFrame(Higgs)
        self.databaseFuncFrame.setGeometry(QtCore.QRect(190, 0, 771, 601))
        self.databaseFuncFrame.setAutoFillBackground(False)
        self.databaseFuncFrame.setStyleSheet("background-color: rgb(222, 247, 255);")
        self.databaseFuncFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.databaseFuncFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.databaseFuncFrame.setObjectName("databaseFuncFrame")
        self.databaseInfo = QtWidgets.QLabel(self.databaseFuncFrame)
        self.databaseInfo.setGeometry(QtCore.QRect(30, 30, 711, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.databaseInfo.setFont(font)
        self.databaseInfo.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.databaseInfo.setObjectName("databaseInfo")
        self.inputDatabaseFile = QLineEdit_ext(self.databaseFuncFrame)
        self.inputDatabaseFile.setGeometry(QtCore.QRect(30, 180, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.inputDatabaseFile.setFont(font)
        self.inputDatabaseFile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.inputDatabaseFile.setObjectName("inputDatabaseFile")
        self.openButtonForDB = QtWidgets.QPushButton(self.databaseFuncFrame)
        self.openButtonForDB.setGeometry(QtCore.QRect(600, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openButtonForDB.setFont(font)
        self.openButtonForDB.setStyleSheet("QPushButton{background-color: rgb(85, 255, 255);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(165, 255, 255);}")
        self.openButtonForDB.setObjectName("openButtonForDB")
        self.updateButtonForDB = QtWidgets.QPushButton(self.databaseFuncFrame)
        self.updateButtonForDB.setGeometry(QtCore.QRect(670, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.updateButtonForDB.setFont(font)
        self.updateButtonForDB.setStyleSheet("QPushButton{background-color: rgb(85, 255, 255);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(165, 255, 255);}")
        self.updateButtonForDB.setObjectName("updateButtonForDB")
        self.updatingBar = QtWidgets.QProgressBar(self.databaseFuncFrame)
        self.updatingBar.setGeometry(QtCore.QRect(30, 230, 701, 16))
        self.updatingBar.setProperty("value", 0)
        self.updatingBar.setObjectName("updatingBar")
        self.line_3 = QtWidgets.QFrame(self.databaseFuncFrame)
        self.line_3.setGeometry(QtCore.QRect(0, 260, 771, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gene = QtWidgets.QComboBox(self.databaseFuncFrame)
        self.gene.setGeometry(QtCore.QRect(100, 290, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.gene.setFont(font)
        self.gene.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"QComboBox::down-arrow{border:none;}")
        self.gene.setObjectName("gene")
        self.label_7 = QtWidgets.QLabel(self.databaseFuncFrame)
        self.label_7.setGeometry(QtCore.QRect(30, 290, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.checkGeneButton = QtWidgets.QPushButton(self.databaseFuncFrame)
        self.checkGeneButton.setGeometry(QtCore.QRect(270, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkGeneButton.setFont(font)
        self.checkGeneButton.setStyleSheet("QPushButton{background-color: rgb(85, 255, 255);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(165, 255, 255);}")
        self.checkGeneButton.setObjectName("checkGeneButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.databaseFuncFrame)
        self.textBrowser.setGeometry(QtCore.QRect(30, 340, 701, 231))
        self.textBrowser.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.analysisFuncFrame = QtWidgets.QFrame(Higgs)
        self.analysisFuncFrame.setGeometry(QtCore.QRect(190, 0, 771, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysisFuncFrame.sizePolicy().hasHeightForWidth())
        self.analysisFuncFrame.setSizePolicy(sizePolicy)
        self.analysisFuncFrame.setAutoFillBackground(False)
        self.analysisFuncFrame.setStyleSheet("background-color: rgb(243, 255, 210);")
        self.analysisFuncFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analysisFuncFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analysisFuncFrame.setObjectName("analysisFuncFrame")
        self.parseFrame = QtWidgets.QFrame(self.analysisFuncFrame)
        self.parseFrame.setGeometry(QtCore.QRect(0, 0, 771, 121))
        self.parseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.parseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.parseFrame.setObjectName("parseFrame")
        self.parsingBar = QtWidgets.QProgressBar(self.parseFrame)
        self.parsingBar.setGeometry(QtCore.QRect(20, 80, 721, 16))
        self.parsingBar.setProperty("value", 0)
        self.parsingBar.setObjectName("parsingBar")
        self.inputFilePath = QLineEdit_ext(self.parseFrame)
        self.inputFilePath.setGeometry(QtCore.QRect(20, 30, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.inputFilePath.setFont(font)
        self.inputFilePath.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.inputFilePath.setObjectName("inputFilePath")
        self.line = QtWidgets.QFrame(self.parseFrame)
        self.line.setGeometry(QtCore.QRect(0, 100, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.openDataButton = QtWidgets.QPushButton(self.parseFrame)
        self.openDataButton.setGeometry(QtCore.QRect(610, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openDataButton.setFont(font)
        self.openDataButton.setStyleSheet("QPushButton{background-color: rgb(85, 255, 255);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(165, 255, 255);}")
        self.openDataButton.setObjectName("openDataButton")
        self.parseDataButton = QtWidgets.QPushButton(self.parseFrame)
        self.parseDataButton.setGeometry(QtCore.QRect(680, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parseDataButton.setFont(font)
        self.parseDataButton.setStyleSheet("QPushButton{background-color: rgb(85, 255, 255);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(165, 255, 255);}")
        self.parseDataButton.setObjectName("parseDataButton")
        self.analysisFrame = QtWidgets.QFrame(self.analysisFuncFrame)
        self.analysisFrame.setGeometry(QtCore.QRect(0, 120, 771, 221))
        self.analysisFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analysisFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analysisFrame.setObjectName("analysisFrame")
        self.label = QtWidgets.QLabel(self.analysisFrame)
        self.label.setGeometry(QtCore.QRect(40, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.candidate = QtWidgets.QComboBox(self.analysisFrame)
        self.candidate.setGeometry(QtCore.QRect(130, 120, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.candidate.setFont(font)
        self.candidate.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"QComboBox::down-arrow{border:none;}")
        self.candidate.setObjectName("candidate")
        self.checkDad = QtWidgets.QCheckBox(self.analysisFrame)
        self.checkDad.setGeometry(QtCore.QRect(350, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(14)
        self.checkDad.setFont(font)
        self.checkDad.setObjectName("checkDad")
        self.checkMom = QtWidgets.QCheckBox(self.analysisFrame)
        self.checkMom.setGeometry(QtCore.QRect(480, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(14)
        self.checkMom.setFont(font)
        self.checkMom.setObjectName("checkMom")
        self.analyzeButton = QtWidgets.QPushButton(self.analysisFrame)
        self.analyzeButton.setGeometry(QtCore.QRect(610, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.analyzeButton.setFont(font)
        self.analyzeButton.setStyleSheet("QPushButton{background-color: rgb(218, 255, 111);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(99, 215, 43);}\n"
"")
        self.analyzeButton.setObjectName("analyzeButton")
        self.minScale = QtWidgets.QDoubleSpinBox(self.analysisFrame)
        self.minScale.setGeometry(QtCore.QRect(470, 60, 81, 31))
        self.minScale.setStyleSheet("background-color: rgb(255, 253, 246);\n"
"QDoubleSpinBox::up-button{border:none;};\n"
"QDoubleSpinBox::down-button{border:none;};")
        self.minScale.setSingleStep(0.01)
        self.minScale.setObjectName("minScale")
        self.label_2 = QtWidgets.QLabel(self.analysisFrame)
        self.label_2.setGeometry(QtCore.QRect(390, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(74, 149, 223);\n"
"border:1px solid rgb(0, 0, 0);\n"
"background-color: rgb(181, 255, 172);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.analysisFrame)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(74, 149, 223);\n"
"border:1px solid rgb(0, 0, 0);\n"
"background-color: rgb(232, 235, 197);\n"
"")
        self.label_5.setObjectName("label_5")
        self.maxScale = QtWidgets.QDoubleSpinBox(self.analysisFrame)
        self.maxScale.setGeometry(QtCore.QRect(630, 60, 81, 31))
        self.maxScale.setStyleSheet("background-color: rgb(255, 253, 246);\n"
"QDoubleSpinBox::up-button{border:none;};\n"
"QDoubleSpinBox::down-button{border:none;};")
        self.maxScale.setSingleStep(0.01)
        self.maxScale.setObjectName("maxScale")
        self.label_3 = QtWidgets.QLabel(self.analysisFrame)
        self.label_3.setGeometry(QtCore.QRect(550, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(74, 149, 223);\n"
"border:1px solid rgb(0, 0, 0);\n"
"background-color: rgb(181, 255, 172);\n"
"")
        self.label_3.setObjectName("label_3")
        self.minHori = QtWidgets.QDoubleSpinBox(self.analysisFrame)
        self.minHori.setGeometry(QtCore.QRect(290, 60, 101, 31))
        self.minHori.setStyleSheet("background-color: rgb(255, 253, 246);\n"
"QDoubleSpinBox::up-button{border:none;};\n"
"QDoubleSpinBox::down-button{border:none;};")
        self.minHori.setWrapping(False)
        self.minHori.setFrame(True)
        self.minHori.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.minHori.setAccelerated(False)
        self.minHori.setKeyboardTracking(True)
        self.minHori.setProperty("showGroupSeparator", False)
        self.minHori.setMaximum(99999.99)
        self.minHori.setObjectName("minHori")
        self.label_4 = QtWidgets.QLabel(self.analysisFrame)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(74, 149, 223);\n"
"border:1px solid rgb(0, 0, 0);\n"
"background-color: rgb(181, 255, 172);\n"
"")
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(self.analysisFrame)
        self.line_2.setGeometry(QtCore.QRect(0, 200, 771, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.analyzingBar = QtWidgets.QProgressBar(self.analysisFrame)
        self.analyzingBar.setGeometry(QtCore.QRect(40, 180, 681, 16))
        self.analyzingBar.setProperty("value", 0)
        self.analyzingBar.setObjectName("analyzingBar")
        self.parsedFileLabel = QtWidgets.QLabel(self.analysisFrame)
        self.parsedFileLabel.setGeometry(QtCore.QRect(160, 30, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.parsedFileLabel.setFont(font)
        self.parsedFileLabel.setStyleSheet("color: rgb(74, 149, 223);\n"
"border:1px solid rgb(0, 0, 0);\n"
"background-color: rgb(179, 255, 128);\n"
"")
        self.parsedFileLabel.setObjectName("parsedFileLabel")
        self.label_6 = QtWidgets.QLabel(self.analysisFrame)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(74, 149, 223);\n"
"border:1px solid rgb(0, 0, 0);\n"
"background-color: rgb(232, 235, 197);\n"
"")
        self.label_6.setObjectName("label_6")
        self.showFrame = QtWidgets.QFrame(self.analysisFuncFrame)
        self.showFrame.setGeometry(QtCore.QRect(0, 340, 771, 261))
        self.showFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.showFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.showFrame.setObjectName("showFrame")
        self.checkChrButton = QtWidgets.QPushButton(self.showFrame)
        self.checkChrButton.setGeometry(QtCore.QRect(670, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkChrButton.setFont(font)
        self.checkChrButton.setStyleSheet("QPushButton{background-color: rgb(255, 255, 150);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(255, 215, 140);}\n"
"")
        self.checkChrButton.setObjectName("checkChrButton")
        self.genReportButton = QtWidgets.QPushButton(self.showFrame)
        self.genReportButton.setGeometry(QtCore.QRect(670, 200, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.genReportButton.setFont(font)
        self.genReportButton.setStyleSheet("QPushButton{background-color: rgb(255, 255, 150);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(255, 215, 140);}\n"
"")
        self.genReportButton.setObjectName("genReportButton")
        self.showTextBrowser = QtWidgets.QTextBrowser(self.showFrame)
        self.showTextBrowser.setGeometry(QtCore.QRect(20, 20, 631, 221))
        self.showTextBrowser.setObjectName("showTextBrowser")
        self.analysisFrame.raise_()
        self.parseFrame.raise_()
        self.showFrame.raise_()
        self.showChrFrame = QtWidgets.QFrame(Higgs)
        self.showChrFrame.setGeometry(QtCore.QRect(0, 0, 961, 601))
        self.showChrFrame.setStyleSheet("background-color: rgb(243, 255, 210);")
        self.showChrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.showChrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.showChrFrame.setObjectName("showChrFrame")
        self.returnButton = QtWidgets.QPushButton(self.showChrFrame)
        self.returnButton.setGeometry(QtCore.QRect(890, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.returnButton.setFont(font)
        self.returnButton.setStyleSheet("QPushButton{background-color: rgb(255, 0, 50);border:1px;border-radius:10px;}\n"
"QPushButton:hover{background-color: rgb(255, 150, 100);}\n"
"")
        self.returnButton.setObjectName("returnButton")
        self.tabWidget = QtWidgets.QTabWidget(self.showChrFrame)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 871, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.tabWidget.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tabWidget.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tabWidget.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.tabWidget.addTab(self.tab_17, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.tabWidget.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.tabWidget.addTab(self.tab_19, "")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.tabWidget.addTab(self.tab_20, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.tabWidget.addTab(self.tab_21, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.tabWidget.addTab(self.tab_22, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.tabWidget.addTab(self.tab_23, "")
        self.leftToolFrame = QtWidgets.QFrame(Higgs)
        self.leftToolFrame.setGeometry(QtCore.QRect(0, 0, 191, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftToolFrame.sizePolicy().hasHeightForWidth())
        self.leftToolFrame.setSizePolicy(sizePolicy)
        self.leftToolFrame.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leftToolFrame.setAutoFillBackground(False)
        self.leftToolFrame.setStyleSheet("background-color: rgb(255, 254, 246);")
        self.leftToolFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftToolFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftToolFrame.setObjectName("leftToolFrame")
        self.analyzerButton = QtWidgets.QPushButton(self.leftToolFrame)
        self.analyzerButton.setGeometry(QtCore.QRect(0, 170, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(16)
        self.analyzerButton.setFont(font)
        self.analyzerButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.analyzerButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.analyzerButton.setAutoFillBackground(False)
        self.analyzerButton.setStyleSheet("QPushButton{background-color: rgb(243, 255, 210);border:none;}\n"
"QPushButton:hover{background-color: rgb(243, 255, 150);}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/analysis.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analyzerButton.setIcon(icon)
        self.analyzerButton.setIconSize(QtCore.QSize(45, 45))
        self.analyzerButton.setAutoDefault(False)
        self.analyzerButton.setDefault(False)
        self.analyzerButton.setFlat(False)
        self.analyzerButton.setObjectName("analyzerButton")
        self.logo = QtWidgets.QLabel(self.leftToolFrame)
        self.logo.setGeometry(QtCore.QRect(0, 0, 191, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.PlainText)
        self.logo.setPixmap(QtGui.QPixmap(":/resource/logo.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.databaseButton = QtWidgets.QPushButton(self.leftToolFrame)
        self.databaseButton.setGeometry(QtCore.QRect(0, 240, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(16)
        self.databaseButton.setFont(font)
        self.databaseButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.databaseButton.setAutoFillBackground(False)
        self.databaseButton.setStyleSheet("QPushButton{background-color: rgb(222, 247, 255);border:none;}\n"
"QPushButton:hover{background-color: rgb(162, 247, 255);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resource/database.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.databaseButton.setIcon(icon1)
        self.databaseButton.setIconSize(QtCore.QSize(45, 45))
        self.databaseButton.setAutoDefault(False)
        self.databaseButton.setDefault(False)
        self.databaseButton.setFlat(False)
        self.databaseButton.setObjectName("databaseButton")
        self.infoButton = QtWidgets.QPushButton(self.leftToolFrame)
        self.infoButton.setGeometry(QtCore.QRect(0, 310, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(16)
        self.infoButton.setFont(font)
        self.infoButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.infoButton.setAutoFillBackground(False)
        self.infoButton.setStyleSheet("QPushButton{background-color: rgb(219, 255, 225);border:none;}\n"
"QPushButton:hover{background-color: rgb(169, 255, 225);}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resource/info.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoButton.setIcon(icon2)
        self.infoButton.setIconSize(QtCore.QSize(45, 45))
        self.infoButton.setAutoDefault(False)
        self.infoButton.setDefault(False)
        self.infoButton.setFlat(False)
        self.infoButton.setObjectName("infoButton")
        self.showChrFrame.raise_()
        self.aboutInfoFrame.raise_()
        self.leftToolFrame.raise_()
        self.databaseFuncFrame.raise_()
        self.analysisFuncFrame.raise_()

        self.retranslateUi(Higgs)
        self.tabWidget.setCurrentIndex(0)
        self.analyzerButton.clicked.connect(self.analysisFuncFrame.raise_)
        self.databaseButton.clicked.connect(self.databaseFuncFrame.raise_)
        self.infoButton.clicked.connect(self.aboutInfoFrame.raise_)
        self.returnButton.clicked.connect(self.analysisFuncFrame.raise_)
        self.checkChrButton.clicked.connect(self.showChrFrame.raise_)
        self.returnButton.clicked.connect(self.leftToolFrame.raise_)
        QtCore.QMetaObject.connectSlotsByName(Higgs)

    def retranslateUi(self, Higgs):
        _translate = QtCore.QCoreApplication.translate
        Higgs.setWindowTitle(_translate("Higgs", "Higgs"))
        self.captureLogButton.setText(_translate("Higgs", "Capture Log"))
        self.textBrowser_2.setHtml(_translate("Higgs", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Please share the log to huajing.li@foxmail.com</span></p></body></html>"))
        self.databaseInfo.setText(_translate("Higgs", "There is no database!!!\n"
"Please update the database~"))
        self.openButtonForDB.setText(_translate("Higgs", "Open"))
        self.updateButtonForDB.setText(_translate("Higgs", "Update"))
        self.label_7.setText(_translate("Higgs", "Gene"))
        self.checkGeneButton.setText(_translate("Higgs", "Check"))
        self.openDataButton.setText(_translate("Higgs", "Open"))
        self.parseDataButton.setText(_translate("Higgs", "Parse"))
        self.label.setText(_translate("Higgs", "Candidate"))
        self.checkDad.setText(_translate("Higgs", "Father"))
        self.checkMom.setText(_translate("Higgs", "Mother"))
        self.analyzeButton.setText(_translate("Higgs", "Analyze"))
        self.label_2.setText(_translate("Higgs", "Min Scale"))
        self.label_5.setText(_translate("Higgs", "[Parameter]"))
        self.label_3.setText(_translate("Higgs", "Max Scale"))
        self.label_4.setText(_translate("Higgs", "Min Hori Average"))
        self.parsedFileLabel.setText(_translate("Higgs", "None"))
        self.label_6.setText(_translate("Higgs", "[Parsed File]"))
        self.checkChrButton.setText(_translate("Higgs", "Check"))
        self.genReportButton.setText(_translate("Higgs", "Generate"))
        self.returnButton.setText(_translate("Higgs", "Return"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Higgs", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Higgs", "2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Higgs", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Higgs", "4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Higgs", "5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Higgs", "6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Higgs", "7"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Higgs", "8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Higgs", "9"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("Higgs", "10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("Higgs", "11"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("Higgs", "12"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("Higgs", "13"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), _translate("Higgs", "14"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), _translate("Higgs", "15"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), _translate("Higgs", "16"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_17), _translate("Higgs", "17"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_18), _translate("Higgs", "18"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_19), _translate("Higgs", "19"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_20), _translate("Higgs", "20"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_21), _translate("Higgs", "21"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_22), _translate("Higgs", "22"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_23), _translate("Higgs", "XY"))
        self.analyzerButton.setText(_translate("Higgs", "Analyzer"))
        self.databaseButton.setText(_translate("Higgs", "Database"))
        self.infoButton.setText(_translate("Higgs", "About"))
from . import resources_rc

class QLineEdit_ext(QtWidgets.QLineEdit):
    # override
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/uri-list'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().text()
        path = path.split('\n')[0]
        path = path[8:]
        self.setText(path)
