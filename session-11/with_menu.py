from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
class MainWindow(QtWidgets.QMainWindow):
    def info(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("/Users/alireza/Desktop/pyadv-02/session-11/with_menu.ui", self) 
        self.actionAbout.triggered.connect(self.info)

if __name__=="__main__":
        app = QtWidgets.QApplication([])
        w = MainWindow()
        w.show()
        app.exec()
