import threading

class ParseDataThread(threading.Thread):

    def __init__(self, widgetList):
        threading.Thread.__init__(self)
        
        for item in widgetList:
            item.setEnabled(False)
        self.widgetList = widgetList

    def run(self):
        # for test
        import time
        time.sleep(3)
        # work done
        for item in self.widgetList:
            item.setEnabled(True)

