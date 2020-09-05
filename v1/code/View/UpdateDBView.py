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
        processBar = ttk.Progressbar(self.frame, mode = "determinate", orient = "horizontal")
        geneList = ttk.Combobox(self.frame, value = ())
        showResult = tk.Label(self.frame, wraplength = 680, anchor = 'nw', justify = 'left') #Automatic line wrap
        signal = td.Event()
        signal.set()
        databaseDescription = tk.Label(self.frame)
        dispatcher.initializeDatabase(self.frame, databaseDescription, geneList)

        def setFilePath(path):
            filePath.set(path[0].decode())

        def openFile():
            if not signal.isSet():
                return
            fileTypeList = [('XLSX','.xlsx'), ('XLS','.xls')]
            filePath.set(tkf.askopenfilename(filetypes = fileTypeList))

        def updateDB():
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
                dispatcher.updateDatabase(path, signal, processBar, self.frame, databaseDescription, geneList)

        def showDetail():
            if not signal.isSet():
                return
            checkGene = geneList.get()
            if not checkGene:
                dispatcher.warning("There is no selected gene name.\n")
            else:
                dispatcher.checkDescriptionByGeneName(checkGene, showResult)

        #-----------------------------
        #  Layout
        #-----------------------------
        databaseDescription.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.35)
        processBar.place(relx = 0.01, rely = 0.38, relwidth = 0.98, relheight = 0.03)

        tk.Label(self.frame, text = 'File:').place(relx = 0.01, rely = 0.43, relwidth = 0.06, relheight = 0.06)
        pathInputObject = tk.Entry(self.frame, textvariable = filePath)
        pathInputObject.place(relx = 0.07, rely = 0.43, relwidth = 0.66, relheight = 0.06)
        # support drop files into entry
        wd.hook_dropfiles(pathInputObject.winfo_id(), func = setFilePath)
        tk.Button(self.frame, text = 'open', command = openFile).place(relx = 0.74, rely = 0.43, relwidth = 0.12, relheight = 0.06)
        tk.Button(self.frame, text = 'update', command = updateDB).place(relx = 0.87, rely = 0.43, relwidth = 0.12, relheight = 0.06)

        tk.Label(self.frame, text = 'Check Gene Description', anchor = 'w').place(relx = 0.01, rely = 0.50, relwidth = 0.98, relheight = 0.1)
        geneList.place(relx = 0.01, rely = 0.61, relwidth = 0.15, relheight = 0.06)
        tk.Button(self.frame, text = 'check', command = showDetail).place(relx = 0.18, rely = 0.61, relwidth = 0.12, relheight = 0.06)

        showResult.place(relx = 0.01, rely = 0.68, relwidth = 0.98, relheight = 0.31)