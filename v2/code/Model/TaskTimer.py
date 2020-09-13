import threading, time, os

class TaskTimerThread(threading.Thread):

    def __init__(self, taskName, workload, barSignal, taskDoneFlag):
        threading.Thread.__init__(self)
        barSignal.emit(taskName, 0)

        # Task: parsing
        # etimate of time for parsing data file by pandas (estimatedTime)
        # test in I7-6500U@2.5GHz  file size: 26700382 byte
        # 1)excel file:  Average time: 37.3s
        # 2)csv file:  Average time: 0.9s
        if taskName == 'parsing':
            fsize = os.path.getsize(workload)
            if workload[-4:] == '.csv':
                estimatedTime = 0.9 / 26700382 * fsize
            elif workload[-5:] == '.xlsx':
                estimatedTime = 37.3 / 26700382 * fsize

        # Task: analyzing
        # etimate of time for analyzing data by pandas
        elif taskName == 'analyzing':
            estimatedTime = workload

        # Task: updating
        # etimate of time for updating database by pandas
        elif taskName == 'updating':
            pass

        self.taskName = taskName
        self.totalTime = estimatedTime
        self.barSignal = barSignal
        self.taskDoneFlag = taskDoneFlag[0]

    def run(self):
        step = self.totalTime / 100
        for i in range(100):
            time.sleep(step)
            self.barSignal.emit(self.taskName, i)
            if self.taskDoneFlag.isEnabled():
                break

        while(not self.taskDoneFlag.isEnabled()):
            time.sleep(step)
        self.barSignal.emit(self.taskName, 100)
            
            