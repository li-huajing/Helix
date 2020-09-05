import tkinter as tk

class CreateOn(object):

    def __init__(self, menuBar):

        fileMenu = tk.Menu(menuBar, tearoff = 0)
        menuBar.add_cascade(label = 'File', menu = fileMenu)