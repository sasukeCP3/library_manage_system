from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import db


class BookStatusAdmin(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("借阅状态")
        self.setupUi()

    def setupUi(self):
        self.resize(850, 500)
        font = QtGui.QFont()
        font.setPointSize(16)

        self.DownLayout = QtWidgets.QVBoxLayout(self)
        self.DownLayout.setObjectName("DownLayout")
        
        self.BookStatus_Title_Label = QtWidgets.QLabel(self)
        self.BookStatus_Title_Label.setFont(font)
        self.BookStatus_Title_Label.setObjectName("BookStatus_Title_Label")
        self.BookStatusTable = QtWidgets.QTableWidget(self)
        self.BookStatusTable.setObjectName("BookStatusTable")
        # 不可编辑
        self.BookStatusTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.BookStatusTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.BookStatusTable.setColumnCount(5)
        self.BookStatusQuery()
        self.BookStatusTable.setRowCount(self.BookStatusRow)
        self.BookStatusUI()
        item = QtWidgets.QTableWidgetItem()
        self.BookStatusTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookStatusTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookStatusTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookStatusTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookStatusTable.setHorizontalHeaderItem(4, item)

        self.DownLayout.addWidget(self.BookStatus_Title_Label)
        self.DownLayout.addWidget(self.BookStatusTable)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate

        self.BookStatus_Title_Label.setText(_translate("BookStatusAdmin", "借阅状态:"))
        item = self.BookStatusTable.horizontalHeaderItem(0)
        item.setText(_translate("BookStatusAdmin", "学生ID"))
        item = self.BookStatusTable.horizontalHeaderItem(1)
        item.setText(_translate("BookStatusAdmin", "书号"))
        item = self.BookStatusTable.horizontalHeaderItem(2)
        item.setText(_translate("BookStatusAdmin", "借出时间"))
        item = self.BookStatusTable.horizontalHeaderItem(3)
        item.setText(_translate("BookStatusAdmin", "归还时间"))
        item = self.BookStatusTable.horizontalHeaderItem(4)
        item.setText(_translate("BookStatusAdmin", "预约排队状态"))

    def BookStatusQuery(self):
        sql = "SELECT StudentId,BookId,BorrowTime,ReturnTime,BookingState FROM User_Book"
        self.query = db.query(sql)
        self.BookStatusRow = len(self.query)
        return

    def BookStatusUI(self):
        for i in range(len(self.query)):
            for j in range(5):
                ite1 = QTableWidgetItem(str(self.query[i][j]))
                self.BookStatusTable.setItem(i, j, ite1)
        return


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainMindow = BookStatusAdmin()
    mainMindow.show()
    sys.exit(app.exec_())
    # pass