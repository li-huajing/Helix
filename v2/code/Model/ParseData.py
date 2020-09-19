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
            data = pd.read_csv(self.path, index_col=0, low_memory=False)
        elif self.path[-5:] == '.xlsx':
            data = pd.read_excel(self.path, index_col=0)
        
        '''
        filter useless data
        '''
        # 1) delete the 'CDS' column value is NUll row data
        data = data.drop(data[pd.isnull(data.CDS)].index)
        # 2) delete the 'Gene1' column value is NUll row data
        data = data.drop(data[pd.isnull(data.Gene1)].index)
        # 3) delete the needless column data
        labels = []
        for item in data.keys():
            if item[0:5] == 'Blank':
                labels.append(item)
            if item[-11:] == '_TargetGene':
                labels.append(item)
            if item[-8:] == '_Predict':
                labels.append(item)
            if item[-13:] == '_ZygoticState':
                labels.append(item)
        data = data.drop(columns=labels)

        '''
        get the candidate id
        '''
        candidate = []
        for item in data.keys():
            if item[-6:] == '_Scale':
                candidate.append(item.split('_')[0])

        # work done
        self.dataFrameSig.emit(self.path, candidate, data)
        self.isTaskDoneSig.emit(True)
