from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
import sip
from BookStorageViewer import BookStorageViewer
from Borrow_Book import Borrow_Book
from Return_Book import Return_Book
from BookingBook import Booking_Book
from BorrowStatusViewer import BorrowStatusViewer


class StudentHome(QWidget):

    def __init__(self, studentId):
        super().__init__()
        self.sID = studentId
        self.setupUi()

    def setupUi(self ):
        self.resize(1400, 700)
        #设置字体。
        font = QtGui.QFont()
        font.setPointSize(16)
        
        # 底层
        self.DownLayout = QtWidgets.QHBoxLayout(self)
        self.DownLayout.setObjectName("DownLayout")
        
        # 按钮层
        self.ButtonLayout = QtWidgets.QVBoxLayout()
        self.ButtonLayout.setObjectName("ButtonLayout")
        # 借书
        self.BorrowButton = QtWidgets.QPushButton(self)
        self.BorrowButton.setMaximumSize(QtCore.QSize(100, 50))
        self.BorrowButton.setFont(font)
        self.BorrowButton.setObjectName("BorrowButton")
        self.ButtonLayout.addWidget(self.BorrowButton)
        # 还书
        self.ReturnButton = QtWidgets.QPushButton(self)
        self.ReturnButton.setMaximumSize(QtCore.QSize(100, 50))
        self.ReturnButton.setFont(font)
        self.ReturnButton.setObjectName("ReturnButton")
        self.ButtonLayout.addWidget(self.ReturnButton)
        # 预约
        self.BookingButton = QtWidgets.QPushButton(self)
        self.BookingButton.setMaximumSize(QtCore.QSize(100, 50))
        self.BookingButton.setFont(font)
        self.BookingButton.setObjectName("BookingButton")
        self.ButtonLayout.addWidget(self.BookingButton)
        # 借阅状态
        self.BookStatusButton = QtWidgets.QPushButton(self)
        self.BookStatusButton.setMaximumSize(QtCore.QSize(100, 50))
        self.BookStatusButton.setFont(font)
        self.BookStatusButton.setObjectName("BookStatusButton")
        self.ButtonLayout.addWidget(self.BookStatusButton)
        # 所有书籍
        self.AllBookButton = QtWidgets.QPushButton(self)
        self.AllBookButton.setMaximumSize(QtCore.QSize(100, 50))
        self.AllBookButton.setFont(font)
        self.AllBookButton.setObjectName("AllBookButton")
        self.ButtonLayout.addWidget(self.AllBookButton)
        # 书库 & 学生借书状态
        self.StorageView = BookStorageViewer()
        self.borrowStatusView = BorrowStatusViewer(self.sID)
        self.AllBookButton.setEnabled(False)
        self.DownLayout.addLayout(self.ButtonLayout)
        self.DownLayout.addWidget(self.StorageView)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.BorrowButton.clicked.connect(self.BorrowButtonClicked)
        self.ReturnButton.clicked.connect(self.ReturnButtonClicked)
        self.BookingButton.clicked.connect(self.BookingButtonClicked)
        self.BookStatusButton.clicked.connect(self.BookStatusButtonClicked)
        self.AllBookButton.clicked.connect(self.AllBookButtonClicked)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("StudentHome", "学生页面"))
        self.BorrowButton.setText(_translate("StudentHome", "借阅"))
        self.ReturnButton.setText(_translate("StudentHome", "归还"))
        self.BookingButton.setText(_translate("StudentHome", "预约"))
        self.BookStatusButton.setText(_translate("StudentHome", "借阅状态"))
        self.AllBookButton.setText(_translate("StudentHome", "所有书籍"))

    def BorrowButtonClicked(self):
        BorrowDialog = Borrow_Book(self.sID, self)
        BorrowDialog.borrow_book_success_signal.connect(self.borrowStatusView.BorrowedQuery)
        BorrowDialog.borrow_book_success_signal.connect(self.StorageView.SearchButtonClicked)
        BorrowDialog.show()
        BorrowDialog.exec_()
        return
    
    def ReturnButtonClicked(self):
        ReturnDialog = Return_Book(self.sID, self)
        ReturnDialog.return_book_success_signal.connect(self.borrowStatusView.ReturnedQuery)
        ReturnDialog.return_book_success_signal.connect(self.borrowStatusView.BorrowedQuery)
        ReturnDialog.return_book_success_signal.connect(self.StorageView.SearchButtonClicked)
        ReturnDialog.show()
        ReturnDialog.exec_()
    
    def BookingButtonClicked(self):
        BookingDialog = Booking_Book(self.sID, self)
        BookingDialog.booking_book_success_signal.connect(self.borrowStatusView.BookingedQuery)
        BookingDialog.booking_book_success_signal.connect(self.StorageView.SearchButtonClicked)
        BookingDialog.show()
        BookingDialog.exec_()
        return

    def BookStatusButtonClicked(self):
        self.DownLayout.removeWidget(self.StorageView)
        sip.delete(self.StorageView)
        self.StorageView = BookStorageViewer()
        self.borrowStatusView = BorrowStatusViewer(self.sID)
        self.DownLayout.addWidget(self.borrowStatusView)
        self.AllBookButton.setEnabled(True)
        self.BookStatusButton.setEnabled(False)
        return

    def AllBookButtonClicked(self):
        self.DownLayout.removeWidget(self.borrowStatusView)
        sip.delete(self.borrowStatusView)
        self.borrowStatusView = BorrowStatusViewer(self.sID)
        self.StorageView = BookStorageViewer()
        self.DownLayout.addWidget(self.StorageView)
        self.AllBookButton.setEnabled(False)
        self.BookStatusButton.setEnabled(True)
        return


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    mainMindow = StudentHome("999")
    mainMindow.show()
    sys.exit(app.exec_())
    # pass