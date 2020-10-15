import threading
import pandas as pd

class ParseDataThread(threading.Thread):

    def __init__(self, path, isTaskDoneSig, dataParseSig):
        threading.Thread.__init__(self)
        isTaskDoneSig.emit(False)
        
        self.isTaskDoneSig = isTaskDoneSig
        self.dataParseSig = dataParseSig
        self.path = path
        print('[Task] 解析传进来的基因数据表格文件，文件路径为：%s' % self.path)

    def run(self):
        if self.path[-4:] == '.csv':
            data = pd.read_csv(self.path, index_col=0, low_memory=False)
        elif self.path[-5:] == '.xlsx':
            data = pd.read_excel(self.path, index_col=0)
        print('[run] 将电子表格中的数据转化为pandas的dataframe数据结构---已完成')
        
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
        print('[run] 过滤掉不需要的数据---已完成')

        '''
        get the candidate id
        '''
        candidate = []
        for item in data.keys():
            if item[-6:] == '_Scale':
                candidate.append(item.split('_')[0])
        filename = self.path.split('/')[-1]
        num = filename.split('-')[0]
        if num in candidate:
            candidate.remove(num)
            candidate.insert(0, num)

        print('[run] 解析出表格中可能的基因检测者的编号：%s' % str(candidate))
        # work done
        self.dataParseSig.emit(self.path, candidate, data)
        self.isTaskDoneSig.emit(True)
