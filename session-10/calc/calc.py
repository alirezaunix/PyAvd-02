from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class MainWindow(QtWidgets.QMainWindow):	
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("/Users/alireza/Desktop/pyadv-02/session-10/calc/calc.ui", self) 
        file1=open("/Users/alireza/Desktop/pyadv-02/session-10/calc/style.qss")
        styleButton=file1.read()
        self.setStyleSheet(styleButton)
        file1.close()
        self.btn_0.clicked.connect(MainWindow.close)  # type: ignore



if __name__=="__main__":
    app = QtWidgets.QApplication([])
    w = MainWindow()
    w.show()
    app.exec()
