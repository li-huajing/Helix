import tkinter as tk

class MainWindow(object):

    def __init__(self, dispatcher):
        self.mainWindowTitle = 'Higgs⭐⭐⭐'
        self.mainWindowSIze = '800x600'
        self.dispatcher = dispatcher

    def startShow(self):
        #-----------------------------
        #  window
        #-----------------------------
        window = tk.Tk()
        window.title(self.mainWindowTitle)
        window.geometry(self.mainWindowSIze)
        #-----------------------------
        #  Menu
        #-----------------------------
        from . import TopMenu
        menuBar = tk.Menu(window)
        TopMenu.CreateOn(menuBar)
        #-----------------------------
        #  Function Frame
        #-----------------------------
        from . import AnalysisView
        from . import UpdateDBView
        ''''''
        toolListFrame = tk.Frame(window)
        funcFrame = tk.Frame(window)
        toolList = []
        # function module
        #toolList.append(AnalysisView.CreateOn(funcFrame, self.dispatcher, "Gene\nAnalyzer", "silver"))
        toolList.append(AnalysisView.CreateOn(funcFrame, self.dispatcher, "Gene\nAnalyzer", "seashell"))
        toolList.append(UpdateDBView.CreateOn(funcFrame, self.dispatcher, "Update\nDatabase", "snow"))
        
        #-----------------------------
        #  Status Frame
        #-----------------------------
        statFrame = tk.Frame(window)
        self.logView = tk.Text(statFrame, bg = 'Honeydew')
        logView = self.logView
        logView.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        scroll = tk.Scrollbar()
        # associate scroll bar and text box
        scroll.config(command = logView.yview)
        logView.config(yscrollcommand = scroll.set)
        # tag config
        logView.tag_add('warning', tk.END)
        logView.tag_config('warning', background = 'Pink')
        logView.tag_add('error', tk.END)
        logView.tag_config('error', background = 'DeepPink')
        logView.tag_add('message', tk.END)
        logView.tag_config('message', background = 'SkyBlue')
        logView.tag_add('information', tk.END)
        logView.tag_config('information', background = 'Gainsboro')
        #-----------------------------
        #  Frame Layout
        #-----------------------------
        window.config(menu = menuBar)
        toolListFrame.place(relx = 0.005, rely = 0.005, relwidth = 0.09, relheight = 0.99)
        funcFrame.place(relx = 0.105, rely = 0.005, relwidth = 0.89, relheight = 0.69)
        statFrame.place(relx = 0.105, rely = 0.705, relwidth = 0.89, relheight = 0.29)
        # button layout on tool list frame
        def showFrame(frame):
            frame.tkraise()

        count = len(toolList)
        step = 1 / count
        for idx in range(count):
            obj = tk.Button(toolListFrame, 
                            text = toolList[idx].name,
                            bg = toolList[idx].color,
                            command = lambda arg=toolList[idx].frame: showFrame(arg))
            obj.place(relx = 0.005, relwidth = 0.9, rely = 0 + idx * step + step * 0.01, relheight = step * 0.95)
        #-----------------------------
        #  Run
        #-----------------------------
        window.mainloop()

    def printLog(self, string, tag = 'information'):
        self.logView.insert(tk.END, string, tag)
        self.logView.yview_moveto(1)