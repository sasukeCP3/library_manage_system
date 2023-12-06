from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import db


class Booking_Book(QDialog):
    booking_book_success_signal = pyqtSignal()

    def __init__(self, sId, parent=None):
        super(Booking_Book, self).__init__(parent)
        self.studentId = sId
        self.setupUi()

    def setupUi(self):
        self.resize(300, 400)

        titlefont = QtGui.QFont()
        titlefont.setPointSize(20)

        font = QtGui.QFont()
        font.setPointSize(14)

        # 底层
        self.DownLayout = QtWidgets.QFormLayout(self)
        self.DownLayout.setObjectName("DownLayout")

        # 借书标识
        self.TitleLabel = QtWidgets.QLabel(self)
        self.TitleLabel.setFont(titlefont)
        self.TitleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TitleLabel.setObjectName("TitleLabel")
        self.DownLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.TitleLabel)
        # 借阅ID
        self.Booking_Student = QtWidgets.QLabel(self)
        self.Booking_Student.setFont(font)
        self.Booking_Student.setObjectName("Booking_Student")
        self.DownLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Booking_Student)
        self.Booking_Student_Id = QtWidgets.QLabel(self)
        self.Booking_Student_Id.setFont(font)
        self.Booking_Student_Id.setObjectName("Booking_Student_Id")
        self.DownLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Booking_Student_Id)
        # 书名
        self.BookName = QtWidgets.QLabel(self)
        self.BookName.setFont(font)
        self.BookName.setObjectName("BookName")
        self.DownLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BookName)
        # 书名输入框
        self.BookName_Edit = QtWidgets.QLineEdit(self)
        self.BookName_Edit.setEnabled(False)
        self.BookName_Edit.setFont(font)
        self.BookName_Edit.setObjectName("BookName_Edit")
        self.DownLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.BookName_Edit)
        # 书号
        self.BookId = QtWidgets.QLabel(self)
        self.BookId.setFont(font)
        self.BookId.setObjectName("BookId")
        self.DownLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.BookId)
        # 书号输入框
        self.BookId_Edit = QtWidgets.QLineEdit(self)
        self.BookId_Edit.setFont(font)
        self.BookId_Edit.setObjectName("BookId_Edit")
        self.DownLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.BookId_Edit)
        # 作者姓名
        self.AuthName = QtWidgets.QLabel(self)
        self.AuthName.setFont(font)
        self.AuthName.setObjectName("AuthName")
        self.DownLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.AuthName)
        # 作者姓名输入框
        self.AuthName_Edit = QtWidgets.QLineEdit(self)
        self.AuthName_Edit.setEnabled(False)
        self.AuthName_Edit.setFont(font)
        self.AuthName_Edit.setObjectName("AuthName_Edit")
        self.DownLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.AuthName_Edit)
        # 书类
        self.BookCategory = QtWidgets.QLabel(self)
        self.BookCategory.setFont(font)
        self.BookCategory.setObjectName("BookCategory")
        self.DownLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.BookCategory)
        # 书类输入框
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
        # 出版社
        self.Publisher_Label = QtWidgets.QLabel(self)
        self.Publisher_Label.setFont(font)
        self.Publisher_Label.setObjectName("Publisher_Label")
        self.DownLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Publisher_Label)
        # 出版社输入框
        self.Publisher_Edit = QtWidgets.QLineEdit(self)
        self.Publisher_Edit.setEnabled(False)
        self.Publisher_Edit.setFont(font)
        self.Publisher_Edit.setObjectName("Publisher_Edit")
        self.DownLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Publisher_Edit)
        # 出版日期
        self.PublishDate = QtWidgets.QLabel(self)
        self.PublishDate.setFont(font)
        self.PublishDate.setObjectName("PublishDate")
        self.DownLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.PublishDate)
        # 出版日期输入框
        self.PublishDate_Edit = QtWidgets.QDateEdit(self)
        self.PublishDate_Edit.setEnabled(False)
        self.PublishDate_Edit.setFont(font)
        self.PublishDate_Edit.setObjectName("PublishDate_Edit")
        self.DownLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.PublishDate_Edit)
        # 预约按钮
        self.BookingBookButton = QtWidgets.QPushButton(self)
        self.BookingBookButton.setMaximumSize(QtCore.QSize(140, 32))
        self.BookingBookButton.setFont(font)
        self.BookingBookButton.setObjectName("BookingBookButton")
        self.DownLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.BookingBookButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.BookingBookButton.clicked.connect(self.BookingButtonClicked)
        self.BookId_Edit.textChanged.connect(self.BookIdEditChanged)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.TitleLabel.setText(_translate("Borrow_Book", "预约书籍"))
        self.Booking_Student.setText(_translate("Borrow_Book", "借 阅 ID:"))
        self.Booking_Student_Id.setText(_translate("Borrow_Book", self.studentId))
        self.BookName.setText(_translate("Borrow_Book", "书    名:"))
        self.BookId.setText(_translate("Borrow_Book", "书    号:"))
        self.AuthName.setText(_translate("Borrow_Book", "作    者:"))
        self.BookCategory.setText(_translate("Borrow_Book", "分    类:"))
        self.BookCategory_Box.setItemText(0, _translate("Borrow_Book", "哲学"))
        self.BookCategory_Box.setItemText(1, _translate("Borrow_Book", "社会科学"))
        self.BookCategory_Box.setItemText(2, _translate("Borrow_Book", "政治"))
        self.BookCategory_Box.setItemText(3, _translate("Borrow_Book", "法律"))
        self.BookCategory_Box.setItemText(4, _translate("Borrow_Book", "军事"))
        self.BookCategory_Box.setItemText(5, _translate("Borrow_Book", "经济"))
        self.BookCategory_Box.setItemText(6, _translate("Borrow_Book", "文化"))
        self.BookCategory_Box.setItemText(7, _translate("Borrow_Book", "教育"))
        self.BookCategory_Box.setItemText(8, _translate("Borrow_Book", "体育"))
        self.BookCategory_Box.setItemText(9, _translate("Borrow_Book", "语言文字"))
        self.BookCategory_Box.setItemText(10, _translate("Borrow_Book", "艺术"))
        self.BookCategory_Box.setItemText(11, _translate("Borrow_Book", "历史"))
        self.BookCategory_Box.setItemText(12, _translate("Borrow_Book", "地理"))
        self.BookCategory_Box.setItemText(13, _translate("Borrow_Book", "天文学"))
        self.BookCategory_Box.setItemText(14, _translate("Borrow_Book", "生物学"))
        self.BookCategory_Box.setItemText(15, _translate("Borrow_Book", "医学卫生"))
        self.BookCategory_Box.setItemText(16, _translate("Borrow_Book", "农业"))
        self.Publisher_Label.setText(_translate("Borrow_Book", "出 版 社:"))
        self.PublishDate.setText(_translate("Borrow_Book", "出版日期:"))
        self.BookingBookButton.setText(_translate("Borrow_Book", "确认预约"))

    def BookingButtonClicked(self):
        BookId = self.BookId_Edit.text()

        if (BookId == ""):
            print(QMessageBox.warning(self, "警告", "你所预约的书不存在，请查看输入", QMessageBox.Yes, QMessageBox.Yes))
            return
        
        sql = "SELECT * FROM Book WHERE BookId='%s'" % BookId
        query = db.query(sql)
        if (query == ()):
            print(QMessageBox.warning(self, "警告", "你所预约的书不存在，请查看输入", QMessageBox.Yes, QMessageBox.Yes))
            return
        
        #可以直接借阅
        sql = "SELECT * FROM Book WHERE BookId='%s'" % BookId
        query = db.query(sql)
        query = query[0]
        if (query[7] != 0):
            print(QMessageBox.warning(self, "警告", "你所需要的书不用预约，请查看输入", QMessageBox.Yes, QMessageBox.Yes))
            return
        print(QMessageBox.information(self, "提示", "预约成功!", QMessageBox.Yes, QMessageBox.Yes))

        # 更新Book表
        sql = "UPDATE Book SET NumBookinged=NumBookinged+1 WHERE BookId='%s'" % BookId
        db.exec_(sql)
        # 寻找预约排队人数
        sql = "SELECT BookingState FROM User_Book WHERE BookId='%s'" % BookId
        query = db.query(sql)
        bookingstates =[]
        for temp in query:
            bookingstate = temp[0]
            bookingstates.append(bookingstate)
        # 插入User_Book表
        sql = "INSERT INTO User_Book VALUES ('%s','%s',NULL,NULL,0,'%d')" % (self.studentId,
                                                                             BookId,max(bookingstates)+1)
        db.exec_( sql)
        self.booking_book_success_signal.emit()
        self.close()
        return

    def BookIdEditChanged(self):
        bookId = self.BookId_Edit.text()
        if (bookId == ""):
            self.BookName_Edit.clear()
            self.Publisher_Edit.clear()
            self.AuthName_Edit.clear()
            self.PublishDate_Edit.clear()

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
    mainMindow = Booking_Book("1234578")
    mainMindow.show()
    sys.exit(app.exec_())
    # pass