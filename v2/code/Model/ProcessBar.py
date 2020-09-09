import threading, time

class ProcessBarThread(threading.Thread):

    def __init__(self, showBar, estimatedTime, signal):
        threading.Thread.__init__(self)

        showBar.setValue(0)
        self.showBar = showBar
        self.totalTime = estimatedTime
        self.signal = signal

    def run(self):
        step = self.totalTime / 100
        for i in range(100):
            self.showBar.setValue(i)
            time.sleep(step)
            if self.signal.isEnabled():
                break
        while(not self.signal.isEnabled()):
            time.sleep(step)
        self.showBar.setValue(100)
            
            