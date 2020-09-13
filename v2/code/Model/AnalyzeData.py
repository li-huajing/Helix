import threading

class AnalyzeDataThread(threading.Thread):

    def __init__(self, param, isTaskDoneSig, resultSig):
        threading.Thread.__init__(self)
        isTaskDoneSig.emit(False)

        self.isTaskDoneSig = isTaskDoneSig
        self.resultSig = resultSig
        self.param = param

    def run(self):
        print(self.param)
        # work done
        self.resultSig.emit()
        self.isTaskDoneSig.emit(True)