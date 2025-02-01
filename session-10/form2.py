import sys
from PyQt5.QtWidgets import *


# Main Window
class TableList(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTableWidget'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show window

    # Create table
    def createTable(self):
        self.tableWidget = QTableWidget()

        file1 = open("/Users/alireza/Desktop/pyadv-02/session-10/data.txt")
        data_list = file1.read().splitlines()
        self.tableWidget.setRowCount(len(data_list))

        # Column count
        self.tableWidget.setColumnCount(8)

        for i, data in enumerate(data_list):
            items = data.split(",")
            for j, yechizi in enumerate(items):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(yechizi))
                # Table will fit the screen horizontally
                self.tableWidget.horizontalHeader().setStretchLastSection(True)
                self.tableWidget.horizontalHeader().setSectionResizeMode(
                    QHeaderView.Stretch)

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
'''