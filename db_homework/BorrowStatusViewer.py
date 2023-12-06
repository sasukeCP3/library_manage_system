from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import db


class BorrowStatusViewer(QWidget):
    def __init__(self, sId):
        super(BorrowStatusViewer, self).__init__()
        self.StudentId = sId
        self.setupUi()

    def setupUi(self):
        self.resize(850, 500)
        font = QtGui.QFont()
        font.setPointSize(16)

        self.DownLayout = QtWidgets.QVBoxLayout(self)
        self.DownLayout.setObjectName("DownLayout")
        
        self.Borrowed_Title_Label = QtWidgets.QLabel(self)
        self.Borrowed_Title_Label.setFont(font)
        self.Borrowed_Title_Label.setObjectName("Borrowed_Title_Label")
        self.BorrowedTable = QtWidgets.QTableWidget(self)
        self.BorrowedTable.setObjectName("BorrowedTable")
        # 不可编辑
        self.BorrowedTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.BorrowedTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.BorrowedTable.setColumnCount(7)
        self.BorrowedQuery()
        self.BorrowedTable.setRowCount(self.borrowedRow)
        self.BorrowedUI()
        item = QtWidgets.QTableWidgetItem()
        self.BorrowedTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BorrowedTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BorrowedTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.BorrowedTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.BorrowedTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.BorrowedTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.BorrowedTable.setHorizontalHeaderItem(6, item)

        self.Returned_Title_Label = QtWidgets.QLabel(self)
        self.Returned_Title_Label.setFont(font)
        self.Returned_Title_Label.setObjectName("Returned_Title_Label")
        self.ReturnedTable = QtWidgets.QTableWidget(self)
        self.ReturnedTable.setObjectName("ReturnedTable")
        # 不可编辑
        self.ReturnedTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.ReturnedTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ReturnedTable.setColumnCount(8)
        self.ReturnedQuery()
        self.ReturnedTable.setRowCount(self.returnedRow)
        self.ReturnedUI()
        item = QtWidgets.QTableWidgetItem()
        self.ReturnedTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReturnedTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReturnedTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReturnedTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReturnedTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReturnedTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReturnedTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReturnedTable.setHorizontalHeaderItem(7, item)

        self.Bookinged_Title_Label = QtWidgets.QLabel(self)
        self.Bookinged_Title_Label.setFont(font)
        self.Bookinged_Title_Label.setObjectName("Bookinged_Title_Label")
        self.BookingedTable = QtWidgets.QTableWidget(self)
        self.BookingedTable.setObjectName("BookingedTable")
        # 不可编辑
        self.BookingedTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.BookingedTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.BookingedTable.setColumnCount(7)
        self.BookingedQuery()
        self.BookingedTable.setRowCount(self.BookingedRow)
        self.BookingedUI()
        item = QtWidgets.QTableWidgetItem()
        self.BookingedTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookingedTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookingedTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookingedTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookingedTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookingedTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookingedTable.setHorizontalHeaderItem(6, item)

        self.DownLayout.addWidget(self.Borrowed_Title_Label)
        self.DownLayout.addWidget(self.BorrowedTable)
        self.DownLayout.addWidget(self.Returned_Title_Label)
        self.DownLayout.addWidget(self.ReturnedTable)
        self.DownLayout.addWidget(self.Bookinged_Title_Label)
        self.DownLayout.addWidget(self.BookingedTable)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate

        self.Borrowed_Title_Label.setText(_translate("BorrowStatusViewer", "已借阅:"))
        item = self.BorrowedTable.horizontalHeaderItem(0)
        item.setText(_translate("BorrowStatusViewer", "书名"))
        item = self.BorrowedTable.horizontalHeaderItem(1)
        item.setText(_translate("BorrowStatusViewer", "书号"))
        item = self.BorrowedTable.horizontalHeaderItem(2)
        item.setText(_translate("BorrowStatusViewer", "作者"))
        item = self.BorrowedTable.horizontalHeaderItem(3)
        item.setText(_translate("BorrowStatusViewer", "分类"))
        item = self.BorrowedTable.horizontalHeaderItem(4)
        item.setText(_translate("BorrowStatusViewer", "出版社"))
        item = self.BorrowedTable.horizontalHeaderItem(5)
        item.setText(_translate("BorrowStatusViewer", "出版时间"))
        item = self.BorrowedTable.horizontalHeaderItem(6)
        item.setText(_translate("BorrowStatusViewer", "借出时间"))

        self.Returned_Title_Label.setText(_translate("BorrowStatusViewer", "已归还:"))
        item = self.ReturnedTable.horizontalHeaderItem(0)
        item.setText(_translate("BorrowStatusViewer", "书名"))
        item = self.ReturnedTable.horizontalHeaderItem(1)
        item.setText(_translate("BorrowStatusViewer", "书号"))
        item = self.ReturnedTable.horizontalHeaderItem(2)
        item.setText(_translate("BorrowStatusViewer", "作者"))
        item = self.ReturnedTable.horizontalHeaderItem(3)
        item.setText(_translate("BorrowStatusViewer", "分类"))
        item = self.ReturnedTable.horizontalHeaderItem(4)
        item.setText(_translate("BorrowStatusViewer", "出版社"))
        item = self.ReturnedTable.horizontalHeaderItem(5)
        item.setText(_translate("BorrowStatusViewer", "出版时间"))
        item = self.ReturnedTable.horizontalHeaderItem(6)
        item.setText(_translate("BorrowStatusViewer", "借出时间"))
        item = self.ReturnedTable.horizontalHeaderItem(7)
        item.setText(_translate("BorrowStatusViewer", "归还时间"))

        self.Bookinged_Title_Label.setText(_translate("BorrowStatusViewer", "已预约:"))
        item = self.BookingedTable.horizontalHeaderItem(0)
        item.setText(_translate("BorrowStatusViewer", "书名"))
        item = self.BookingedTable.horizontalHeaderItem(1)
        item.setText(_translate("BorrowStatusViewer", "书号"))
        item = self.BookingedTable.horizontalHeaderItem(2)
        item.setText(_translate("BorrowStatusViewer", "作者"))
        item = self.BookingedTable.horizontalHeaderItem(3)
        item.setText(_translate("BorrowStatusViewer", "分类"))
        item = self.BookingedTable.horizontalHeaderItem(4)
        item.setText(_translate("BorrowStatusViewer", "出版社"))
        item = self.BookingedTable.horizontalHeaderItem(5)
        item.setText(_translate("BorrowStatusViewer", "出版时间"))
        item = self.BookingedTable.horizontalHeaderItem(6)
        item.setText(_translate("BorrowStatusViewer", "预约排队"))

    def BorrowedQuery(self):
        sql = "SELECT Book.BookName,Book.BookId,Auth,Category,Publisher,PublishTime,BorrowTime  FROM Book,User_Book WHERE Book.BookId=User_Book.BookId AND User_Book.BorrowState=1 AND StudentId='%s'" % self.StudentId
        self.query = db.query(sql)
        self.borrowedRow = len(self.query)
        return

    def ReturnedQuery(self):
        sql = "SELECT Book.BookName,Book.BookId,Auth,Category,Publisher,PublishTime,BorrowTime,ReturnTime  FROM Book,User_Book WHERE Book.BookId=User_Book.BookId AND User_Book.BorrowState=0 AND StudentId='%s' AND User_Book.BookingState=0" % self.StudentId
        self.query = db.query(sql)
        self.returnedRow = len(self.query)
        return
    
    def BookingedQuery(self):
        sql = "SELECT Book.BookName,Book.BookId,Auth,Category,Publisher,PublishTime,BookingState  FROM Book,User_Book WHERE Book.BookId=User_Book.BookId AND User_Book.BookingState!='0' AND StudentId='%s'" % self.StudentId
        self.query = db.query(sql)
        self.BookingedRow = len(self.query)
        return

    def BorrowedUI(self):
        for i in range(len(self.query)):
            for j in range(7):
                ite1 = QTableWidgetItem(str(self.query[i][j]))
                self.BorrowedTable.setItem(i, j, ite1)
        return

    def ReturnedUI(self):
        for i in range(len(self.query)):
            for j in range(8):
                ite1 = QTableWidgetItem(str(self.query[i][j]))
                self.ReturnedTable.setItem(i, j, ite1)
        return
    
    def BookingedUI(self):
        for i in range(len(self.query)):
            for j in range(7):
                ite1 = QTableWidgetItem(str(self.query[i][j]))
                self.BookingedTable.setItem(i, j, ite1)
        return


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainMindow = BorrowStatusViewer("111")
    mainMindow.show()
    sys.exit(app.exec_())
    # pass