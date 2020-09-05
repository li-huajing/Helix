import sys
sys.path.append('..')

import View
from . import Dispatcher


class Application(object):

    def __init__(self):
        self.dispatcher = Dispatcher.Dispatcher()
        self.viewer = View.MainWindow(self.dispatcher)

    def run(self):
        self.dispatcher.configLogger(self.viewer)
        self.viewer.startShow()