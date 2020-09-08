from PyQt5.QtWidgets import QApplication, QMainWindow
import UI, sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    UI.Ui_Higgs().setupUi(win)
    win.show()
    sys.exit(app.exec_())