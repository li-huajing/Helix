import threading
import pandas as pd

class ParseDataThread(threading.Thread):

    def __init__(self, isTaskDoneSig):
        threading.Thread.__init__(self)
        isTaskDoneSig.emit(False)
        
        self.isTaskDoneSig = isTaskDoneSig

    def run(self):
        # for test
        '''
        if self.path[-4:] == '.csv':
            data = pd.read_csv(self.path)
        else:
            data = pd.read_excel(self.path)
        '''
        import time
        time.sleep(3)
        
        # work done
        self.isTaskDoneSig.emit(True)
