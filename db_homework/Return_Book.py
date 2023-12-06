from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import db


class Return_Book(QDialog):
    return_book_success_signal = pyqtSignal()

    def __init__(self, sId, parent=None):
        super(Return_Book, self).__init__(parent)
        self.StudentId = sId
        self.setupUi()

    def setupUi(self):
        self.resize(300, 400)

        titlefont = QtGui.QFont()
        titlefont.setPointSize(20)

        font = QtGui.QFont()
        font.setPointSize(14)

        self.DownLayout = QtWidgets.QFormLayout(self)
        self.DownLayout.setObjectName("DownLayout")

        self.TitleLabel = QtWidgets.QLabel(self)
        self.TitleLabel.setFont(titlefont)
        self.TitleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TitleLabel.setObjectName("TitleLabel")
        self.DownLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.TitleLabel)

        self.Return_Student = QtWidgets.QLabel(self)
        self.Return_Student.setFont(font)
        self.Return_Student.setObjectName("Return_Student")
        self.DownLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Return_Student)
        self.Return_Student_Id = QtWidgets.QLabel(self)
        self.Return_Student_Id.setFont(font)
        self.Return_Student_Id.setObjectName("Return_Student_Id")
        self.DownLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Return_Student_Id)

        self.BookName = QtWidgets.QLabel(self)
        self.BookName.setFont(font)
        self.BookName.setObjectName("BookName")
        self.DownLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BookName)

        self.BookName_Edit = QtWidgets.QLineEdit(self)
        self.BookName_Edit.setEnabled(False)
        self.BookName_Edit.setFont(font)
        self.BookName_Edit.setObjectName("BookName_Edit")
        self.DownLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.BookName_Edit)

        self.BookId = QtWidgets.QLabel(self)
        self.BookId.setFont(font)
        self.BookId.setObjectName("BookId")
        self.DownLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.BookId)

        self.BookId_Edit = QtWidgets.QLineEdit(self)
        self.BookId_Edit.setFont(font)
        self.BookId_Edit.setObjectName("BookId_Edit")
        self.DownLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.BookId_Edit)

        self.AuthName = QtWidgets.QLabel(self)
        self.AuthName.setFont(font)
        self.AuthName.setObjectName("AuthName")
        self.DownLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.AuthName)

        self.AuthName_Edit = QtWidgets.QLineEdit(self)
        self.AuthName_Edit.setEnabled(False)
        self.AuthName_Edit.setFont(font)
        self.AuthName_Edit.setObjectName("AuthName_Edit")
        self.DownLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.AuthName_Edit)

        self.BookCategory = QtWidgets.QLabel(self)
        self.BookCategory.setFont(font)
        self.BookCategory.setObjectName("BookCategory")
        self.DownLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.BookCategory)

        self.BookCategory_Box = QtWidgets.QComboBox(self)
        self.BookCategory_Box.setEnabled(False)
        self.BookCategory_Box.setFont(font)
        self.BookCategory_Box.setObjectName("BookCategory_Box")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.BookCategory_Box.addItem("")
        self.DownLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.BookCategory_Box)

        self.Publisher_Label = QtWidgets.QLabel(self)
        self.Publisher_Label.setFont(font)
        self.Publisher_Label.setObjectName("Publisher_Label")
        self.DownLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Publisher_Label)

        self.Publisher_Edit = QtWidgets.QLineEdit(self)
        self.Publisher_Edit.setEnabled(False)
        self.Publisher_Edit.setFont(font)
        self.Publisher_Edit.setObjectName("Publisher_Edit")
        self.DownLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Publisher_Edit)

        self.PublishDate = QtWidgets.QLabel(self)
        self.PublishDate.setFont(font)
        self.PublishDate.setObjectName("PublishDate")
        self.DownLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.PublishDate)

        self.PublishDate_Edit = QtWidgets.QDateEdit(self)
        self.PublishDate_Edit.setEnabled(False)
        self.PublishDate_Edit.setFont(font)
        self.PublishDate_Edit.setObjectName("PublishDate_Edit")
        self.DownLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.PublishDate_Edit)

        self.ReturnBookButton = QtWidgets.QPushButton(self)
        self.ReturnBookButton.setMaximumSize(QtCore.QSize(140, 32))
        self.ReturnBookButton.setFont(font)
        self.ReturnBookButton.setObjectName("ReturnBookButton")
        self.DownLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.ReturnBookButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.ReturnBookButton.clicked.connect(self.ReturnButtonClicked)
        self.BookId_Edit.textChanged.connect(self.BookIdEditChanged)

    def retranslateUi(self):

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Return_Book", "归还书籍"))
        self.TitleLabel.setText(_translate("Return_Book", "归还书籍"))
        self.Return_Student.setText(_translate("Return_Book", "归 还 ID:"))
        self.Return_Student_Id.setText(_translate("Return_Book", self.StudentId))
        self.BookName.setText(_translate("Return_Book", "书    名:"))
        self.BookId.setText(_translate("Return_Book", "书    号:"))
        self.AuthName.setText(_translate("Return_Book", "作    者:"))
        self.BookCategory.setText(_translate("Return_Book", "分    类:"))
        self.BookCategory_Box.setItemText(0, _translate("Return_Book", "哲学"))
        self.BookCategory_Box.setItemText(1, _translate("Return_Book", "社会科学"))
        self.BookCategory_Box.setItemText(2, _translate("Return_Book", "政治"))
        self.BookCategory_Box.setItemText(3, _translate("Return_Book", "法律"))
        self.BookCategory_Box.setItemText(4, _translate("Return_Book", "军事"))
        self.BookCategory_Box.setItemText(5, _translate("Return_Book", "经济"))
        self.BookCategory_Box.setItemText(6, _translate("Return_Book", "文化"))
        self.BookCategory_Box.setItemText(7, _translate("Return_Book", "教育"))
        self.BookCategory_Box.setItemText(8, _translate("Return_Book", "体育"))
        self.BookCategory_Box.setItemText(9, _translate("Return_Book", "语言文字"))
        self.BookCategory_Box.setItemText(10, _translate("Return_Book", "艺术"))
        self.BookCategory_Box.setItemText(11, _translate("Return_Book", "历史"))
        self.BookCategory_Box.setItemText(12, _translate("Return_Book", "地理"))
        self.BookCategory_Box.setItemText(13, _translate("Return_Book", "天文学"))
        self.BookCategory_Box.setItemText(14, _translate("Return_Book", "生物学"))
        self.BookCategory_Box.setItemText(15, _translate("Return_Book", "医学卫生"))
        self.BookCategory_Box.setItemText(16, _translate("Return_Book", "农业"))
        self.Publisher_Label.setText(_translate("Return_Book", "出 版 社:"))
        self.PublishDate.setText(_translate("Return_Book", "出版日期:"))
        self.ReturnBookButton.setText(_translate("Return_Book", "确认归还"))

    def ReturnButtonClicked(self):
        BookId = self.BookId_Edit.text()
        if (BookId == ""):
            print(QMessageBox.warning(self, "警告", "图书馆未收录此书", QMessageBox.Yes, QMessageBox.Yes))
            return
        sql = "SELECT * FROM User_Book WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            self.StudentId, BookId)
        query = db.query(sql)
        if (query == ()):
            print(QMessageBox.information(self, "警告", "您并未借阅此书", QMessageBox.Yes, QMessageBox.Yes))
            return
        # 更新Book表
        sql = "SELECT * FROM Book WHERE BookId='%s' AND NumBookinged != 0" % (
            BookId)
        query = db.exec_(sql)
        if (query == None):
            sql = "UPDATE Book SET NumCanBorrow=NumCanBorrow+1 WHERE BookId='%s'" % BookId
            db.exec_(sql)
            print(111)
        else:
            sql = "UPDATE Book SET NumBookinged=NumBookinged-1 WHERE BookId='%s'" % BookId
            db.exec_(sql)
            print(222)
        # 更新还书学生User_Book表
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "UPDATE User_Book SET ReturnTime='%s',BorrowState=0 WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            timenow, self.StudentId, BookId)
        db.exec_(sql)
        # 更新第一个预约学生User_Book表
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "SELECT * FROM User_Book WHERE BookId='%s' AND BookingState = 1 " % (BookId)
        query = db.query(sql)
        if (query != ()):
            sql = "UPDATE User_Book SET BorrowTime='%s',BorrowState = 1,BookingState = 0 WHERE BookId='%s' AND BookingState = 1 " % (
            timenow, BookId)
            db.exec_(sql)
        # 更新剩余预约学生User_Book表
        sql = "UPDATE User_Book SET BookingState = BookingState-1 WHERE BookId='%s' AND BookingState != 0" % (
            BookId)
        db.exec_(sql)
        print(QMessageBox.information(self, "提示", "归还成功!", QMessageBox.Yes, QMessageBox.Yes))
        self.return_book_success_signal.emit()
        self.close()
        return

    def BookIdEditChanged(self):
        bookId = self.BookId_Edit.text()
        if (bookId == "" or len(bookId) < 6):
            self.BookName_Edit.clear()
            self.Publisher_Edit.clear()
            self.AuthName_Edit.clear()
            self.PublishDate_Edit.clear()

        # 在User_Book表中找借阅记录，如果存在借阅，则更新form内容
        sql = "SELECT * FROM User_Book WHERE StudentId='%s' AND BookId='%s' AND BorrowState=1" % (
            self.StudentId, bookId)
        query = db.query(sql)
        if (query != ()):
            # 更新form内容
            sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
            query = db.query(sql)
            # 查询对应书号，如果存在就更新form
            if (query != ()):
                query = query[0]
                self.BookName_Edit.setText(query[0])
                self.AuthName_Edit.setText(query[2])
                self.BookCategory_Box.setCurrentText(query[3])
                self.Publisher_Edit.setText(query[4])
                self.PublishDate_Edit.setDate(query[5])
        return


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainMindow = Return_Book("12345678")
    mainMindow.show()
    sys.exit(app.exec_())
    # pass