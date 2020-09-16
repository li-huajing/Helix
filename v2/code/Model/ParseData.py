import threading
import pandas as pd

class ParseDataThread(threading.Thread):

    def __init__(self, path, isTaskDoneSig, dataFrameSig):
        threading.Thread.__init__(self)
        isTaskDoneSig.emit(False)
        
        self.isTaskDoneSig = isTaskDoneSig
        self.dataFrameSig = dataFrameSig
        self.path = path

    def run(self):
        if self.path[-4:] == '.csv':
            data = pd.read_csv(self.path, low_memory=False)
        elif self.path[-5:] == '.xlsx':
            data = pd.read_excel(self.path)
        
        candidate = []
        for item in data.keys():
            if item[-6:] == '_Scale':
                candidate.append(item.split('_')[0])

        # work done
        self.dataFrameSig.emit(self.path, candidate, data)
        self.isTaskDoneSig.emit(True)
