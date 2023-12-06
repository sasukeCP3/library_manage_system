from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import db


class BookStorageViewer(QWidget):

    def __init__(self):
        super(BookStorageViewer, self).__init__()

        self.setupUi()

    def setupUi(self):
        # 查询模型
        self.queryModel = None
        # 数据表
        self.tableView = None
        # 当前页
        self.CurrentPage = 0
        # 总页数
        self.TotalPage = 0
        # 总记录数
        self.TotalRecord = 0
        # 每页数据数
        self.Page_Record_Num = 15

        self.resize(1200, 500)
        font = QtGui.QFont()
        font.setPointSize(15)

        self.DownLayout = QtWidgets.QVBoxLayout(self)
        self.DownLayout.setObjectName("DownLayout")

        self.SearchLayout = QtWidgets.QHBoxLayout()
        self.SearchLayout.setObjectName("SearchLayout")

        self.SearchLabel = QtWidgets.QLabel()
        self.SearchLabel.setFont(font)
        self.SearchLabel.setObjectName("SearchLabel")
        self.SearchLayout.addWidget(self.SearchLabel)

        self.SearchEdit = QtWidgets.QLineEdit()
        self.SearchEdit.setFont(font)
        self.SearchEdit.setObjectName("SearchEdit")
        self.SearchLayout.addWidget(self.SearchEdit)

        self.SearchButton = QtWidgets.QPushButton()
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")
        self.SearchLayout.addWidget(self.SearchButton)
        
        self.BookType_Box = QtWidgets.QComboBox()
        self.BookType_Box.setFont(font)
        self.BookType_Box.setObjectName("BookType_Box")
        self.BookType_Box.addItem("")
        self.BookType_Box.addItem("")
        self.BookType_Box.addItem("")
        self.BookType_Box.addItem("")
        self.SearchLayout.addWidget(self.BookType_Box)
        self.DownLayout.addLayout(self.SearchLayout)

        self.BookTable = QtWidgets.QTableWidget()
        self.BookTable.setObjectName("BookTable")

        # 不可编辑
        self.BookTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.BookTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.BookTable.setColumnCount(8)
        self.BookTable.setRowCount(self.Page_Record_Num)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setVerticalHeaderItem(7, item)

        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(7, item)
        self.DownLayout.addWidget(self.BookTable)

        self.PageWidget = QtWidgets.QWidget()
        self.PageWidget.setObjectName("widget")

        self.PageLayout = QtWidgets.QHBoxLayout(self.PageWidget)
        self.PageLayout.setObjectName("PageLayout")

        self.PageNow = QtWidgets.QLabel(self.PageWidget)
        self.PageNow.setMaximumSize(QtCore.QSize(6, 32))
        self.PageNow.setObjectName("PageNow")
        self.PageLayout.addWidget(self.PageNow)

        self.PageTotal = QtWidgets.QLabel(self.PageWidget)
        self.PageTotal.setObjectName("PageTotal")
        self.PageLayout.addWidget(self.PageTotal)

        self.PreButton = QtWidgets.QPushButton(self.PageWidget)
        self.PreButton.setMaximumSize(QtCore.QSize(64, 32))
        self.PreButton.setObjectName("PreButton")
        self.PageLayout.addWidget(self.PreButton)

        self.BackButton = QtWidgets.QPushButton(self.PageWidget)
        self.BackButton.setMaximumSize(QtCore.QSize(64, 32))
        self.BackButton.setObjectName("BackButton")
        self.PageLayout.addWidget(self.BackButton)

        self.DownLayout.addWidget(self.PageWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.SearchButtonClicked()

        self.BookTable.setRowCount(self.Page_Record_Num)

        self.SearchButton.clicked.connect(self.SearchButtonClicked)
        self.PreButton.clicked.connect(self.PrevButtonClicked)
        self.BackButton.clicked.connect(self.BackButtonClicked)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.SearchLabel.setText(_translate("BookStorageViewer", "查询条件: "))
        self.SearchButton.setText(_translate("BookStorageViewer", "查询"))
        self.BookType_Box.setItemText(0, _translate("BookStorageViewer", "按书名查询"))
        self.BookType_Box.setItemText(1, _translate("BookStorageViewer", "按书号查询"))
        self.BookType_Box.setItemText(2, _translate("BookStorageViewer", "按作者查询"))
        self.BookType_Box.setItemText(3, _translate("BookStorageViewer", "按分类查询"))

        for row in range(8):
            item = self.BookTable.verticalHeaderItem(row)
            item.setText(_translate("BookStorageViewer", str(row)))

        item = self.BookTable.horizontalHeaderItem(0)
        item.setText(_translate("BookStorageViewer", "书名"))
        item = self.BookTable.horizontalHeaderItem(1)
        item.setText(_translate("BookStorageViewer", "书号"))
        item = self.BookTable.horizontalHeaderItem(2)
        item.setText(_translate("BookStorageViewer", "作者"))
        item = self.BookTable.horizontalHeaderItem(3)
        item.setText(_translate("BookStorageViewer", "分类"))
        item = self.BookTable.horizontalHeaderItem(4)
        item.setText(_translate("BookStorageViewer", "出版社"))
        item = self.BookTable.horizontalHeaderItem(5)
        item.setText(_translate("BookStorageViewer", "出版时间"))
        item = self.BookTable.horizontalHeaderItem(6)
        item.setText(_translate("BookStorageViewer", "库存"))
        item = self.BookTable.horizontalHeaderItem(7)
        item.setText(_translate("BookStorageViewer", "剩余可借"))
        self.PreButton.setText(_translate("BookStorageViewer", "前一页"))
        self.BackButton.setText(_translate("BookStorageViewer", "后一页"))

    def setButtonStatus(self):
        if (self.CurrentPage == self.TotalPage):
            self.PreButton.setEnabled(True)
            self.BackButton.setEnabled(False)
        if (self.CurrentPage == 1):
            self.BackButton.setEnabled(True)
            self.PreButton.setEnabled(False)
        if (self.CurrentPage < self.TotalPage and self.CurrentPage > 1):
            self.PreButton.setEnabled(True)
            self.BackButton.setEnabled(True)

    # 得到记录数
    def getTotalRecordCount(self):
        self.query = db.query("SELECT * FROM Book")
        self.TotalRecord = len(self.query)
        return

    # 得到总页数
    def getPageCount(self):
        self.query = db.query("SELECT * FROM Book")
        self.TotalRecord = len(self.query)
        self.TotalPage = int((self.TotalRecord + self.Page_Record_Num - 1) / self.Page_Record_Num)
        return

    # 分页记录查询
    def Record_Query(self, Record_Limit):

        QueryCondition = ""

        TypeChoice = self.BookType_Box.currentText()
        if (TypeChoice == "按书名查询"):
            TypeChoice = 'BookName'
        elif (TypeChoice == "按书号查询"):
            TypeChoice = 'BookId'
        elif (TypeChoice == "按作者查询"):
            TypeChoice = 'Auth'
        else:
            TypeChoice = 'Category'

        # 没输入查询条件
        if (self.SearchEdit.text() == ""):
            QueryCondition = (
                    "select * from Book ORDER BY %s  limit %d,%d " % (TypeChoice, Record_Limit, self.Page_Record_Num))
            self.query = db.query(QueryCondition)
            self.setButtonStatus()
            self.updateUI()
            return

        # 模糊查询
        temp = self.SearchEdit.text()
        s = '%%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%%"
        QueryCondition = ("SELECT * FROM Book WHERE {} LIKE '{}' ORDER BY {} ".format(
            TypeChoice, s, TypeChoice))
        self.query = db.query(QueryCondition)
        self.TotalRecord = len(self.query)
        self.updateUI()
        self.SearchEdit.setText('') 

        # 查询没查到
        if (self.TotalRecord == 0):
            print(QMessageBox.information(self, "警告", "图书馆未收录此书", QMessageBox.Yes, QMessageBox.Yes))
            QueryCondition = (
                    "select * from Book ORDER BY %s  limit %d,%d " % (TypeChoice, Record_Limit, self.Page_Record_Num))
            self.query = db.query(QueryCondition)
            self.setButtonStatus()
            self.updateUI()
            self.SearchEdit.setText('') 
            return

        self.TotalPage = int((self.TotalRecord + self.Page_Record_Num - 1) / self.Page_Record_Num)
        self.PageTotal.setText("/ " + str(int(self.TotalPage)) + "页")
        QueryCondition = ("SELECT * FROM Book WHERE %s LIKE '%s' ORDER BY %s LIMIT %d,%d " % (
            TypeChoice, s, TypeChoice, Record_Limit, self.Page_Record_Num))
        
        self.query = db.query(QueryCondition)
        self.setButtonStatus()
        self.updateUI()
        return

    # 点击查询
    def SearchButtonClicked(self):
        self.CurrentPage = 1
        self.PageNow.setText(str(self.CurrentPage))
        self.getPageCount()
        self.PageTotal.setText("/ " + str(int(self.TotalPage)) + "页")
        Record_Limit = (self.CurrentPage - 1) * self.Page_Record_Num
        self.Record_Query(Record_Limit)
        return

    # 向前翻页
    def PrevButtonClicked(self):
        self.CurrentPage -= 1
        if (self.CurrentPage <= 1):
            self.CurrentPage = 1
        self.PageNow.setText(str(self.CurrentPage))
        Record_Limit = (self.CurrentPage - 1) * self.Page_Record_Num
        self.Record_Query(Record_Limit)
        return

    # 向后翻页
    def BackButtonClicked(self):
        self.CurrentPage += 1
        if (self.CurrentPage >= int(self.TotalPage)):
            self.CurrentPage = int(self.TotalPage)
        self.PageNow.setText(str(self.CurrentPage))
        Record_Limit = (self.CurrentPage - 1) * self.Page_Record_Num
        self.Record_Query(Record_Limit)
        return

    def updateUI(self, *__args):
        for i in range(15):
            for j in range(9):
                if i < len(self.query):
                    ite1 = QTableWidgetItem(str(self.query[i][j]))
                else:
                    ite1 = QTableWidgetItem(None)
                self.BookTable.setItem(i, j, ite1)
        return


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainMindow = BookStorageViewer()
    mainMindow.show()
    sys.exit(app.exec_())
    # pass