from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import db


class Shortage_Count(QDialog):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("缺货统计")
        self.setupUi()

    def setupUi(self):
        self.resize(850, 500)
        font = QtGui.QFont()
        font.setPointSize(16)

        self.DownLayout = QtWidgets.QVBoxLayout(self)
        self.DownLayout.setObjectName("DownLayout")
        
        self.ShortageBook_Title_Label = QtWidgets.QLabel(self)
        self.ShortageBook_Title_Label.setFont(font)
        self.ShortageBook_Title_Label.setObjectName("ShortageBook_Title_Label")
        self.ShortageBookTable = QtWidgets.QTableWidget(self)
        self.ShortageBookTable.setObjectName("ShortageBookTable")
        # 不可编辑
        self.ShortageBookTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.ShortageBookTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ShortageBookTable.setColumnCount(7)
        self.ShortageBookQuery()
        self.ShortageBookTable.setRowCount(self.ShortageBookRow)
        self.ShortageBookUI()
        item = QtWidgets.QTableWidgetItem()
        self.ShortageBookTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ShortageBookTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ShortageBookTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ShortageBookTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ShortageBookTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ShortageBookTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ShortageBookTable.setHorizontalHeaderItem(6, item)

        self.DownLayout.addWidget(self.ShortageBook_Title_Label)
        self.DownLayout.addWidget(self.ShortageBookTable)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate

        self.ShortageBook_Title_Label.setText(_translate("ShortageBookAdmin", "缺货统计:"))
        item = self.ShortageBookTable.horizontalHeaderItem(0)
        item.setText(_translate("ShortageBookAdmin", "书名"))
        item = self.ShortageBookTable.horizontalHeaderItem(1)
        item.setText(_translate("ShortageBookAdmin", "书号"))
        item = self.ShortageBookTable.horizontalHeaderItem(2)
        item.setText(_translate("ShortageBookAdmin", "作者"))
        item = self.ShortageBookTable.horizontalHeaderItem(3)
        item.setText(_translate("ShortageBookAdmin", "分类"))
        item = self.ShortageBookTable.horizontalHeaderItem(4)
        item.setText(_translate("ShortageBookAdmin", "出版社"))
        item = self.ShortageBookTable.horizontalHeaderItem(5)
        item.setText(_translate("ShortageBookAdmin", "出版时间"))
        item = self.ShortageBookTable.horizontalHeaderItem(6)
        item.setText(_translate("ShortageBookAdmin", "图书馆剩余"))

    def ShortageBookQuery(self):
        sql = "SELECT BookName,BookId,Auth,Category,Publisher,PublishTime,NumCanBorrow FROM Book WHERE NumCanBorrow < 10 "
        self.query = db.query(sql)
        self.ShortageBookRow = len(self.query)
        return

    def ShortageBookUI(self):
        for i in range(len(self.query)):
            for j in range(7):
                ite1 = QTableWidgetItem(str(self.query[i][j]))
                self.ShortageBookTable.setItem(i, j, ite1)
        return


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainMindow = Shortage_Count()
    mainMindow.show()
    sys.exit(app.exec_())
    # pass