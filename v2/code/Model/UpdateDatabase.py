import threading, time
import pandas as pd

class UpdateDatabaseThread(threading.Thread):

    def __init__(self, path, isTaskDoneSig, updateDbSig):
        threading.Thread.__init__(self)
        isTaskDoneSig.emit(False)
        
        self.isTaskDoneSig = isTaskDoneSig
        self.updateDbSig = updateDbSig
        self.path = path

    def run(self):
        if self.path[-4:] == '.csv':
            data = pd.read_csv(self.path, low_memory=False)
        elif self.path[-5:] == '.xlsx':
            data = pd.read_excel(self.path)
        data = data.set_index('GeneName')

        db = {}
        db.update({'file': self.path.split('/')[-1]})
        db.update({'date': time.ctime()})
        for gene, item in data.iterrows():
            description = 'chnName: %s  inheritance: %s' % (str(item['ChName']), str(item['Inheritance']))

            if pd.isnull(item['ChDescription']):
                description += '[ChDescription]' + 'None' + '\n'
            else:
                description += '[ChDescription]' + str(item['ChDescription']) + '\n'

            if pd.isnull(item['Description']):
                description += '[Description]' + 'None' + '\n'
            else:
                description += '[Description]' + str(item['Description']) + '\n'

            db.update({gene: description})

        with open('db', 'w', encoding='utf-8') as fp:
            fp.write(str(db))
        # work done
        self.updateDbSig.emit()
        self.isTaskDoneSig.emit(True)