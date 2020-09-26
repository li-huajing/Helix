import threading, time
import pandas as pd

class UpdateDatabaseThread(threading.Thread):

    def __init__(self, path, isTaskDoneSig, updateDbSig):
        threading.Thread.__init__(self)
        isTaskDoneSig.emit(False)
        
        self.isTaskDoneSig = isTaskDoneSig
        self.updateDbSig = updateDbSig
        self.path = path
        print('[Task] 解析传进来的基因描述文件以更新基因库，文件路径为：%s' % self.path)

    def run(self):
        if self.path[-4:] == '.csv':
            data = pd.read_csv(self.path, low_memory=False)
        elif self.path[-5:] == '.xlsx':
            data = pd.read_excel(self.path)
        data = data.set_index('GeneName')
        print('[run] 将电子表格中的数据转化为pandas的dataframe数据结构---已完成')

        db = {}
        db.update({'file': self.path.split('/')[-1]})
        db.update({'date': time.ctime()})
        for gene, item in data.iterrows():
            description = 'chnName: %s  inheritance: %s\n' % (str(item['ChName']), str(item['Inheritance']))

            if pd.isnull(item['ChDescription']):
                description += '[ChDescription]' + 'None' + '\n'
            else:
                description += '[ChDescription]' + str(item['ChDescription']) + '\n'

            if pd.isnull(item['Description']):
                description += '[Description]' + 'None' + '\n'
            else:
                description += '[Description]' + str(item['Description']) + '\n'

            db.update({gene: description})
        print('[run] 将带有基因描述信息的dataframe转化为字典---已完成')

        with open('db', 'w', encoding='utf-8') as fp:
            fp.write(str(db))
        print('[run] 将带有基因描述信息的字典保存为db文件---已完成')
        # work done
        self.updateDbSig.emit()
        self.isTaskDoneSig.emit(True)