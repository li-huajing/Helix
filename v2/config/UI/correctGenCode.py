import os, re

path = os.getcwd() + "\..\..\code\\UI\MainWindow.py"
print('gen file path:' + path)

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
    
        fileText += line
    
fp = open(path, 'w')
fp.writelines(fileText)
fp.close()