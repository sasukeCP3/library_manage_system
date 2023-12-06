from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Add_Book import Add_Book
from Delete_Book import Delete_Book
from BookStatusAdmin import BookStatusAdmin
from Shortage_Count import Shortage_Count
from BookStorageViewer import BookStorageViewer


from Stu_Manage import Stu_Manage

class AdminHome(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("AdminHome")
        self.resize(1240, 620)

        font = QtGui.QFont()
        font.setPointSize(16)

        self.DownLayout = QtWidgets.QHBoxLayout(self)
        self.DownLayout.setObjectName("DownLayout")

        self.ButtonLayout = QtWidgets.QVBoxLayout()
        self.ButtonLayout.setObjectName("ButtonLayout")

        self.AddBookButton = QtWidgets.QPushButton(self)
        self.AddBookButton.setEnabled(True)
        self.AddBookButton.setMaximumSize(QtCore.QSize(100, 42))
        self.AddBookButton.setFont(font)
        self.AddBookButton.setObjectName("AddBookButton")
        self.ButtonLayout.addWidget(self.AddBookButton)

        self.DeleteBookButton = QtWidgets.QPushButton(self)
        self.DeleteBookButton.setMaximumSize(QtCore.QSize(100, 42))
        self.DeleteBookButton.setFont(font)
        self.DeleteBookButton.setObjectName("DeleteBookButton")
        self.ButtonLayout.addWidget(self.DeleteBookButton)

        self.BookStatusButton = QtWidgets.QPushButton(self)
        self.BookStatusButton.setMaximumSize(QtCore.QSize(100, 42))
        self.BookStatusButton.setFont(font)
        self.BookStatusButton.setObjectName("BookStatusButton")
        self.ButtonLayout.addWidget(self.BookStatusButton)

        self.ShortageBookButton = QtWidgets.QPushButton(self)
        self.ShortageBookButton.setMaximumSize(QtCore.QSize(100, 42))
        self.ShortageBookButton.setFont(font)
        self.ShortageBookButton.setObjectName("ShortageBookButton")
        self.ButtonLayout.addWidget(self.ShortageBookButton)

        self.StuManageButton = QtWidgets.QPushButton(self)
        self.StuManageButton.setMaximumSize(QtCore.QSize(100, 42))
        self.StuManageButton.setFont(font)
        self.StuManageButton.setObjectName("StuManageButton")
        self.ButtonLayout.addWidget(self.StuManageButton)

        self.DownLayout.addLayout(self.ButtonLayout)
        self.storageView = BookStorageViewer()
        self.DownLayout.addWidget(self.storageView)

        self.AddBookButton.clicked.connect(self.AddBookButtonClicked)
        self.DeleteBookButton.clicked.connect(self.DeleteBookButtonClicked)
        self.BookStatusButton.clicked.connect(self.BookStatusButtonClicked)
        self.ShortageBookButton.clicked.connect(self.ShortageBookButtonClicked)
        self.StuManageButton.clicked.connect(self.StuManage)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AdminHome", "欢迎使用图书馆管理系统"))
        self.AddBookButton.setText(_translate("AdminHome", "添加书籍"))
        self.DeleteBookButton.setText(_translate("AdminHome", "删除书籍"))
        self.BookStatusButton.setText(_translate("AdminHome", "借阅状态"))
        self.ShortageBookButton.setText(_translate("AdminHome", "缺货统计"))
        self.StuManageButton.setText(_translate("AdminHome", "学生管理"))

    def AddBookButtonClicked(self):
        AddBook = Add_Book(self)
        AddBook.add_book_success_signal.connect(self.storageView.SearchButtonClicked)
        AddBook.show()
        AddBook.exec_()

    def DeleteBookButtonClicked(self):
        DeleteBook = Delete_Book(self)
        DeleteBook.delete_book_successful_signal.connect(self.storageView.SearchButtonClicked)
        DeleteBook.show()
        DeleteBook.exec_()

    def BookStatusButtonClicked(self):
        BookStatus = BookStatusAdmin(self)
        BookStatus.show()
        BookStatus.exec_()

    def ShortageBookButtonClicked(self):
        ShortageBook = Shortage_Count(self)
        ShortageBook.show()
        ShortageBook.exec_()

    def StuManage(self):
        StuManage = Stu_Manage(self)
        StuManage.show()
        StuManage.exec_()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainMindow = AdminHome()
    mainMindow.show()
    sys.exit(app.exec_())