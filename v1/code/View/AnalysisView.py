import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkf
import threading as td
import windnd as wd

class CreateOn(object):

    def __init__(self, funcFrame, dispatcher, name, color):
        
        self.name = name
        self.color = color
        self.frame = tk.Frame(funcFrame, bg = self.color)
        self.frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        #-----------------------------
        #  Parameter
        #-----------------------------
        filePath = tk.StringVar()
        minScale = tk.StringVar()
        minScale.set("0.7")
        maxScale = tk.StringVar()
        maxScale.set("1.3")
        minHoriAverage = tk.StringVar()
        minHoriAverage.set("4")
        signal = td.Event()
        signal.set()
        fa = tk.IntVar()
        mo = tk.IntVar()
        candidateList = ttk.Combobox(self.frame, value = ())
        candidateFa = tk.Checkbutton(self.frame, text = 'father', variable = fa)
        candidateMo = tk.Checkbutton(self.frame, text = 'mother', variable = mo)
        processBar = ttk.Progressbar(self.frame, mode = "determinate", orient = "horizontal")
        reportBoard = tk.Label(self.frame, bg = 'Ivory', anchor = 'nw', justify = 'left')

        def setFilePath(path):
            filePath.set(path[0].decode())

        def openFile():
            if not signal.isSet():
                return
            fileTypeList = [('XLSX','.xlsx'), ('XLS','.xls')]
            filePath.set(tkf.askopenfilename(filetypes = fileTypeList))

        def parseFile():
            if not signal.isSet():
                return
            path = filePath.get()
            if not path:
                dispatcher.warning("There is no selected file.Please input the file path!\n")
            elif path[-4:] != '.xls' and path[-5:] != '.xlsx':
                dispatcher.error("The file type is not supported!\n")
            else:
                signal.clear()
                processBar["value"] = 0
                reportBoard["text"] = ""
                dispatcher.information("Parsing the file:%s\n" % path)
                dispatcher.openDataFile(path, candidateList, signal, processBar, self.frame)

        def analyzeData():
            if not signal.isSet():
                return
            id = candidateList.get()
            min = minScale.get()
            max = maxScale.get()
            minHori = minHoriAverage.get()
            if not id:
                dispatcher.warning("Please select the candidate id\n")
            elif not min:
                dispatcher.warning("Please fill the min scale\n")
            elif not max:
                dispatcher.warning("Please fill the max scale\n")
            elif not minHori:
                dispatcher.warning("Please fill the hori average\n")
            else:
                try:
                    min = float(min)
                    max = float(max)
                    minHori = float(minHori)
                    flagFa = fa.get()
                    flagMo = mo.get()
                except ValueError:
                    dispatcher.error("Please check the minScale, maxScale or horiAverage value\n")
                    return

                dispatcher.information("Analyzing the Ge data of id:%s fa:%s mo:%s minScale:%s maxScale:%s minHoriAverage:%s\n"
                                         % (id, flagFa, flagMo, str(min), str(max), str(minHori)))
                signal.clear()
                processBar["value"] = 0
                reportBoard["text"] = ""
                dispatcher.analyzeData(id, max, min, minHori, reportBoard, signal, processBar, self.frame, flagFa, flagMo)

        def generateReport():
            if not signal.isSet():
                return
            if not reportBoard['text']:
                dispatcher.warning("There is no any report have been generated\n")
                return
            filePath = tkf.asksaveasfilename(filetypes = [('TXT', '.txt'), ('All Type', '.*')])
            fileHandle = open(filePath, 'w', encoding='utf-8')
            signal.clear()
            dispatcher.generateReport(fileHandle, signal, processBar, self.frame)

        #-----------------------------
        #  Layout
        #-----------------------------
        tk.Label(self.frame, text = 'File:').place(relx = 0.01, rely = 0.05, relwidth = 0.06, relheight = 0.06)
        pathInputObject = tk.Entry(self.frame, textvariable = filePath)
        pathInputObject.place(relx = 0.07, rely = 0.05, relwidth = 0.66, relheight = 0.06)
        # support drop files into entry
        wd.hook_dropfiles(pathInputObject.winfo_id(), func = setFilePath)
        tk.Button(self.frame, text = 'open', command = openFile).place(relx = 0.75, rely = 0.05, relwidth = 0.12, relheight = 0.06)
        tk.Button(self.frame, text = 'parse', command = parseFile).place(relx = 0.88, rely = 0.05, relwidth = 0.12, relheight = 0.06)

        tk.Label(self.frame, text = 'Candidate:').place(relx = 0.01, rely = 0.15, relwidth = 0.1, relheight = 0.06)
        candidateList.place(relx = 0.11, rely = 0.15, relwidth = 0.12, relheight = 0.06)
        candidateFa.place(relx = 0.23, rely = 0.15, relwidth = 0.08, relheight = 0.06)
        candidateMo.place(relx = 0.31, rely = 0.15, relwidth = 0.09, relheight = 0.06)
        tk.Label(self.frame, text = 'Min Scale:').place(relx = 0.41, rely = 0.15, relwidth = 0.1, relheight = 0.06)
        tk.Entry(self.frame, textvariable = minScale).place(relx = 0.51, rely = 0.15, relwidth = 0.05, relheight = 0.06)
        tk.Label(self.frame, text = 'Max Scale:').place(relx = 0.56, rely = 0.15, relwidth = 0.1, relheight = 0.06)
        tk.Entry(self.frame, textvariable = maxScale).place(relx = 0.66, rely = 0.15, relwidth = 0.05, relheight = 0.06)
        tk.Label(self.frame, text = 'Hori Average:').place(relx = 0.71, rely = 0.15, relwidth = 0.12, relheight = 0.06)
        tk.Entry(self.frame, textvariable = minHoriAverage).place(relx = 0.83, rely = 0.15, relwidth = 0.05, relheight = 0.06)
        tk.Button(self.frame, text = 'analyze', command = analyzeData).place(relx = 0.88, rely = 0.15, relwidth = 0.12, relheight = 0.06)

        processBar.place(relx = 0.01, rely = 0.22, relwidth = 0.98, relheight = 0.03)

        reportBoard.place(relx = 0.01, rely = 0.26, relwidth = 0.98, relheight = 0.73)
        tk.Button(self.frame, text = 'generate report', command = generateReport).place(relx = 0.84, rely = 0.93, relwidth = 0.15, relheight = 0.06)


        