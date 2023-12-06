from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import db


class Delete_Book(QDialog):
    delete_book_successful_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(Delete_Book, self).__init__(parent)
        self.setWindowTitle("删除书籍")
        self.setupUi()

    def setupUi(self, ):
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

        self.BookName = QtWidgets.QLabel(self)
        self.BookName.setFont(font)
        self.BookName.setObjectName("BookName")
        self.DownLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.BookName)

        self.BookName_Edit = QtWidgets.QLineEdit(self)
        self.BookName_Edit.setEnabled(False)
        self.BookName_Edit.setFont(font)
        self.BookName_Edit.setObjectName("BookName_Edit")
        self.DownLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.BookName_Edit)

        self.BookId = QtWidgets.QLabel(self)
        self.BookId.setFont(font)
        self.BookId.setObjectName("BookId")
        self.DownLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BookId)

        self.BookId_Edit = QtWidgets.QLineEdit(self)
        self.BookId_Edit.setFont(font)
        self.BookId_Edit.setObjectName("BookId_Edit")
        self.DownLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.BookId_Edit)

        self.AuthName = QtWidgets.QLabel(self)
        self.AuthName.setFont(font)
        self.AuthName.setObjectName("AuthName")
        self.DownLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.AuthName)

        self.AuthName_Edit = QtWidgets.QLineEdit(self)
        self.AuthName_Edit.setEnabled(False)
        self.AuthName_Edit.setFont(font)
        self.AuthName_Edit.setObjectName("AuthName_Edit")
        self.DownLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.AuthName_Edit)

        self.BookCategory = QtWidgets.QLabel(self)
        self.BookCategory.setFont(font)
        self.BookCategory.setObjectName("BookCategory")
        self.DownLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.BookCategory)

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
        self.DownLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.BookCategory_Box)

        self.Publisher_Label = QtWidgets.QLabel(self)
        self.Publisher_Label.setFont(font)
        self.Publisher_Label.setObjectName("Publisher_Label")
        self.DownLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Publisher_Label)

        self.Publisher_Edit = QtWidgets.QLineEdit(self)
        self.Publisher_Edit.setEnabled(False)
        self.Publisher_Edit.setFont(font)
        self.Publisher_Edit.setObjectName("Publisher_Edit")
        self.DownLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Publisher_Edit)

        self.PublishDate = QtWidgets.QLabel(self)
        self.PublishDate.setFont(font)
        self.PublishDate.setObjectName("PublishDate")
        self.DownLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.PublishDate)

        self.PublishDate_Edit = QtWidgets.QDateEdit(self)
        self.PublishDate_Edit.setEnabled(False)
        self.PublishDate_Edit.setFont(font)
        self.PublishDate_Edit.setObjectName("PublishDate_Edit")
        self.DownLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.PublishDate_Edit)

        self.DeleteNumLabel = QtWidgets.QLabel(self)
        self.DeleteNumLabel.setFont(font)
        self.DeleteNumLabel.setObjectName("DeleteNumLabel")
        self.DownLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.DeleteNumLabel)

        self.DeleteNumEdit = QtWidgets.QLineEdit(self)
        self.DeleteNumEdit.setFont(font)
        self.DeleteNumEdit.setObjectName("DeleteNumEdit")
        self.DownLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.DeleteNumEdit)

        self.DeleteBookButton = QtWidgets.QPushButton(self)
        self.DeleteBookButton.setMaximumSize(QtCore.QSize(140, 32))
        self.DeleteBookButton.setFont(font)
        self.DeleteBookButton.setObjectName("DeleteBookButton")
        self.DownLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.DeleteBookButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.DeleteBookButton.clicked.connect(self.DeleteBookButtonClicked)
        self.BookId_Edit.textChanged.connect(self.BookIdEditChanged)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.TitleLabel.setText(_translate("addBookDialog", "  删除书籍"))
        self.BookName.setText(_translate("addBookDialog", "书    名:"))
        self.BookId.setText(_translate("addBookDialog", "书    号:"))
        self.AuthName.setText(_translate("addBookDialog", "作    者:"))
        self.BookCategory.setText(_translate("addBookDialog", "分    类:"))
        self.BookCategory_Box.setItemText(0, _translate("addBookDialog", "哲学"))
        self.BookCategory_Box.setItemText(1, _translate("addBookDialog", "社会科学"))
        self.BookCategory_Box.setItemText(2, _translate("addBookDialog", "政治"))
        self.BookCategory_Box.setItemText(3, _translate("addBookDialog", "法律"))
        self.BookCategory_Box.setItemText(4, _translate("addBookDialog", "军事"))
        self.BookCategory_Box.setItemText(5, _translate("addBookDialog", "经济"))
        self.BookCategory_Box.setItemText(6, _translate("addBookDialog", "文化"))
        self.BookCategory_Box.setItemText(7, _translate("addBookDialog", "教育"))
        self.BookCategory_Box.setItemText(8, _translate("addBookDialog", "体育"))
        self.BookCategory_Box.setItemText(9, _translate("addBookDialog", "语言文字"))
        self.BookCategory_Box.setItemText(10, _translate("addBookDialog", "艺术"))
        self.BookCategory_Box.setItemText(11, _translate("addBookDialog", "历史"))
        self.BookCategory_Box.setItemText(12, _translate("addBookDialog", "地理"))
        self.BookCategory_Box.setItemText(13, _translate("addBookDialog", "天文学"))
        self.BookCategory_Box.setItemText(14, _translate("addBookDialog", "生物学"))
        self.BookCategory_Box.setItemText(15, _translate("addBookDialog", "医学卫生"))
        self.BookCategory_Box.setItemText(16, _translate("addBookDialog", "农业"))
        self.Publisher_Label.setText(_translate("addBookDialog", "出 版 社:"))
        self.PublishDate.setText(_translate("addBookDialog", "出版日期:"))
        self.DeleteNumLabel.setText(_translate("", "数    量:"))
        self.DeleteBookButton.setText(_translate("", "删除"))

    def BookIdEditChanged(self):
        bookId = self.BookId_Edit.text()
        if (bookId == "" or len(bookId) < 6):
            self.BookName_Edit.clear()
            self.Publisher_Edit.clear()
            self.AuthName_Edit.clear()
            self.DeleteNumEdit.clear()
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

    def DeleteBookButtonClicked(self):
        bookId = self.BookId_Edit.text()
        DeleteNum = 0
        if (self.DeleteNumEdit.text() == ""):
            print(QMessageBox.warning(self, "警告", "淘汰数目为空，操作失败！"), QMessageBox.Yes, QMessageBox.Yes)
            return
        DeleteNum = int(self.DeleteNumEdit.text())
        sql = "SELECT * FROM Book WHERE BookId='%s'" % (bookId)
        query = db.query(sql)
        if (query == ()):
            print(QMessageBox.warning(self, "警告", "该书不存在"), QMessageBox.Yes, QMessageBox.Yes)
            return
        if (query != ()):
            if (DeleteNum > query[0][7] or DeleteNum < 0):
                print(QMessageBox.warning(self, "警告", "最多可淘汰%d本" % (query[0][7]), QMessageBox.Yes, QMessageBox.Yes))
                return
        if (DeleteNum == query[0][6]):
            sql = "DELETE  FROM Book WHERE BookId='%s'" % (bookId)
        else:
            sql = "UPDATE BOOK SET NumStorage=NumStorage-%d,NumCanBorrow=NumCanBorrow-%d WHERE BookId='%s'" % (
                DeleteNum, DeleteNum, bookId)
        db.exec_(sql)

        print(QMessageBox.information(self, "提示", "删除成功!", QMessageBox.Yes, QMessageBox.Yes))
        self.delete_book_successful_signal.emit()
        self.close()
        return


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainMindow = Delete_Book()
    mainMindow.show()
    sys.exit(app.exec_())
