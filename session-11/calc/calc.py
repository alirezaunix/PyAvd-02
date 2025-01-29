from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class MainWindow(QtWidgets.QMainWindow):	

    def insertDigit(self, n):
        txt = self.label_result.text()
        self.label_result.setText(txt+n)

    def equal(self):
        txt = self.label_result.text()
        self.label_result.setText(str(eval(txt)))
    
    def clear_label(self):
        self.label_result.setText("")
    
    def delete_label(self):
        txt = self.label_result.text()
        self.label_result.setText(txt[:-1])

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("/Users/alireza/Desktop/pyadv-02/session-11/calc/calc.ui", self) 
        file1=open("/Users/alireza/Desktop/pyadv-02/session-11/calc/style.qss")
        styleButton=file1.read()
        self.setStyleSheet(styleButton)
        file1.close()
        
        for v in range(10):
            getattr(self, f"btn_{v}").clicked.connect(lambda _, n=v: self.insertDigit(str(n)))
            
        operators={"div":"/",
                            "add":"+",
                            "mul":"*",
                            "minus":"-",
                            "dot":".",
                            "p_1":"(",
                            "p_2":")"}
        for v in operators:
            getattr(self, f"btn_{v}").clicked.connect(
                lambda _, n=operators[v]: self.insertDigit(n))
        self.btn_equal.clicked.connect(self.equal)
        self.btn_c.clicked.connect(self.clear_label)
        self.btn_d.clicked.connect(self.delete_label)


if __name__=="__main__":
    app = QtWidgets.QApplication([])
    w = MainWindow()
    w.show()
    app.exec()
