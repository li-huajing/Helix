import os, re

path = os.getcwd() + "\..\..\code\\UI\MainWindow.py"
print('gen file path:' + path)

# correct code to fix build error
fileText = ''
with open(path, 'r') as fp:
    for line in fp.readlines():
        ''' #1 '''
        if re.match('.*clicked\.connect.*', line):
            print('origin:\n' + line)
            line = re.sub('raise', 'raise_', line)
            print('modified:\n' + line)
        ''' #2 '''
        if re.match('^import', line):
            print('origin:\n' + line)
            line = 'from . ' + line
            print('modified:\n' + line)
        ''' #3 '''
        if re.match('.*QLineEdit.*', line):
            print('origin:\n' + line)
            line = re.sub('QtWidgets.QLineEdit', 'QLineEdit_ext', line)
            print('modified:\n' + line)
    
        fileText += line

# extend QLineEdit Widget
fileText += '''
class QLineEdit_ext(QtWidgets.QLineEdit):
    # override
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/uri-list'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().text()
        path = path.split('\\n')[0]
        path = path[8:]
        self.setText(path)
'''

# save code
fp = open(path, 'w')
fp.writelines(fileText)
fp.close()