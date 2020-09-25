import threading, time
import pandas as pd
import xml.etree.ElementTree as et

class UpdateDatabaseThread(threading.Thread):

    def __init__(self, path, isTaskDoneSig):
        threading.Thread.__init__(self)
        isTaskDoneSig.emit(False)
        
        self.isTaskDoneSig = isTaskDoneSig
        self.path = path

    def run(self):
        if self.path[-4:] == '.csv':
            data = pd.read_csv(self.path, low_memory=False)
        elif self.path[-5:] == '.xlsx':
            data = pd.read_excel(self.path)
        
        root = et.Element('data')
        root.attrib.update({'file': self.path})
        root.attrib.update({'date': time.ctime()})
        for index, item in data.iterrows():
            child = et.Element('gene')
            child.attrib.update({'name': item['GeneName']})
            child.attrib.update({'chnName': str(item['ChName'])})
            child.attrib.update({'inheritance': str(item['Inheritance'])})

            description = '\n'
            description += '[ChDescription]' + str(item['ChDescription']) + '\n'
            description += '[Description]' + str(item['Description']) + '\n'
            description += '[ChDescriptionJJ]' + str(item['ChDescriptionJJ']) + '\n'
            child.text = description

            root.append(child)

        et.ElementTree(root).write("GeneDatabase.xml", "UTF-8")

        # work done
        self.isTaskDoneSig.emit(True)
