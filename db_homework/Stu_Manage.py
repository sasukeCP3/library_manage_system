from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import time
import sip
import db


class Stu_Manage(QDialog):

    def __init__(self, parent=None):
        super(Stu_Manage, self).__init__(parent)
        self.resize(600, 600)

        self.setWindowTitle("管理用户")
        # 用户数
        self.userCount = 0
        self.oldDeleteId = ""
        self.oldDeleteName = ""
        self.deleteId = ""
        self.deleteName = ""
        self.setupUi()

    def setupUi(self):

        font = QtGui.QFont()
        font.setPointSize(16)

        self.getResult()
        self.DownLayout = QtWidgets.QFormLayout(self)
        self.DownLayout.setObjectName("DownLayout")
        # 删除
        self.Delete_Title_Label = QtWidgets.QLabel(self)
        self.Delete_Title_Label.setFont(font)
        self.Delete_Title_Label.setObjectName("Delete_Title_Label")
        self.DownLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Delete_Title_Label)

        self.TableWidget = QtWidgets.QTableWidget(self)
        self.TableWidget.setMinimumSize(QtCore.QSize(800, 160))
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setColumnCount(4)
        self.TableWidget.setRowCount(self.userCount)
        item = QtWidgets.QTableWidgetItem()
        item.setText("学号")
        self.TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("姓名")
        self.TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("密码")
        self.TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("电话")
        self.TableWidget.setHorizontalHeaderItem(3, item)
        self.DownLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.TableWidget)

        # 不可编辑
        self.TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 标题可拉伸
        self.TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 整行选中
        self.TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setRows()

        # 添加
        self.Add_Title_Label = QtWidgets.QLabel(self)
        self.Add_Title_Label.setFont(font)
        self.Add_Title_Label.setObjectName("Add_Title_Label")
        self.DownLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Add_Title_Label)

        self.Add_Edit_Widget = QtWidgets.QTableWidget(self)
        self.Add_Edit_Widget.setMinimumSize(QtCore.QSize(800, 90))
        self.Add_Edit_Widget.setObjectName("Add_Edit_Widget")
        self.Add_Edit_Widget.setColumnCount(4)
        self.Add_Edit_Widget.setRowCount(self.userCount)
        item = QtWidgets.QTableWidgetItem()
        item.setText("学号")
        self.Add_Edit_Widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("姓名")
        self.Add_Edit_Widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("密码")
        self.Add_Edit_Widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("电话")
        self.Add_Edit_Widget.setHorizontalHeaderItem(3, item)
        self.DownLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Add_Edit_Widget)
        # 标题可拉伸
        self.Add_Edit_Widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # 编辑
        self.Editing_Title_Label = QtWidgets.QLabel(self)
        self.Editing_Title_Label.setFont(font)
        self.Editing_Title_Label.setObjectName("Editing_Title_Label")
        self.DownLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Editing_Title_Label)

        self.Editing_Edit_Widget = QtWidgets.QTableWidget(self)
        self.Editing_Edit_Widget.setMinimumSize(QtCore.QSize(800, 160))
        self.Editing_Edit_Widget.setObjectName("Editing_Edit_Widget")
        self.Editing_Edit_Widget.setColumnCount(4)
        self.Editing_Edit_Widget.setRowCount(self.userCount)
        item = QtWidgets.QTableWidgetItem()
        item.setText("学号")
        self.Editing_Edit_Widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("姓名")
        self.Editing_Edit_Widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("密码")
        self.Editing_Edit_Widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("电话")
        self.Editing_Edit_Widget.setHorizontalHeaderItem(3, item)
        self.DownLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Editing_Edit_Widget)
        # 标题可拉伸
        self.Editing_Edit_Widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 按钮
        self.ButtonWidget = QtWidgets.QWidget(self)
        self.ButtonWidget.setMinimumSize(QtCore.QSize(0, 160))
        self.ButtonWidget.setObjectName("ButtonWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ButtonWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.ButtonLayout = QtWidgets.QHBoxLayout()
        self.ButtonLayout.setObjectName("ButtonLayout")

        self.Delete_Stu_Button = QtWidgets.QPushButton(self.ButtonWidget)
        self.Delete_Stu_Button.setMaximumSize(QtCore.QSize(180, 36))
        self.Delete_Stu_Button.setObjectName("Delete_Stu_Button")
        self.ButtonLayout.addWidget(self.Delete_Stu_Button)
        self.horizontalLayout.addLayout(self.ButtonLayout)

        self.Add_Stu_Button = QtWidgets.QPushButton(self.ButtonWidget)
        self.Add_Stu_Button.setMaximumSize(QtCore.QSize(180, 36))
        self.Add_Stu_Button.setObjectName("Add_Stu_Button")
        self.ButtonLayout.addWidget(self.Add_Stu_Button)

        self.Editing_Stu_Button = QtWidgets.QPushButton(self.ButtonWidget)
        self.Editing_Stu_Button.setMaximumSize(QtCore.QSize(180, 36))
        self.Editing_Stu_Button.setObjectName("Editing_Stu_Button")
        self.ButtonLayout.addWidget(self.Editing_Stu_Button)

        self.DownLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.ButtonWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # 设置信号
        self.Add_Stu_Button.clicked.connect(self.AddStu)
        self.Editing_Stu_Button.clicked.connect(self.EditStu)
        self.Delete_Stu_Button.clicked.connect(self.DeleteStu)
        self.TableWidget.itemClicked.connect(self.getStudentInfo)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("", "管理用户"))
        self.Delete_Title_Label.setText(_translate("", "删 除 用 户"))
        self.Add_Title_Label.setText(_translate("", "添 加 用 户"))
        self.Editing_Title_Label.setText(_translate("", "编 辑 用 户"))
        self.Add_Stu_Button.setText(_translate("", "添 加 用 户"))
        self.Editing_Stu_Button.setText(_translate("", "编 辑 用 户"))
        self.Delete_Stu_Button.setText(_translate("", "删 除 用 户"))

    def getResult(self):
        sql = "SELECT StudentId,Name,Password,tel FROM User WHERE IsAdmin=0"
        self.query = db.query(sql)
        if self.query != ():
            self.userCount = len(self.query)

    def setRows(self):
        font = QFont()
        font.setPixelSize(14)
        for i in range(self.userCount):

            StudentIdItem = QTableWidgetItem(self.query[i][0])
            StudentNameItem = QTableWidgetItem(self.query[i][1])
            StudentPasswordItem = QTableWidgetItem(self.query[i][2])
            StudentTelItem = QTableWidgetItem(self.query[i][3])

            StudentIdItem.setFont(font)
            StudentNameItem.setFont(font)
            StudentPasswordItem.setFont(font)
            StudentTelItem.setFont(font)

            self.TableWidget.setItem(i, 0, StudentIdItem)
            self.TableWidget.setItem(i, 1, StudentNameItem)
            self.TableWidget.setItem(i, 2, StudentPasswordItem)
            self.TableWidget.setItem(i, 3, StudentTelItem)
        return

    def getStudentInfo(self):
        row = self.TableWidget.currentIndex().row()
        self.TableWidget.verticalScrollBar().setSliderPosition(row)
        self.getResult()
        if (self.query != ()):
            i = row
        self.oldDeleteId = self.deleteId
        self.oldDeleteName = self.deleteName
        self.deleteId = self.query[i][0]
        self.deleteName = self.query[i][1]

    def AddStu(self):
        #获得表格输入
        if (self.Add_Edit_Widget.item(0,0) == None or self.Add_Edit_Widget.item(0,1) == None or self.Add_Edit_Widget.item(0,2) == None or self.Add_Edit_Widget.item(0,3) == None):
            print(QMessageBox.warning(self, "警告", "信息不完整,无法添加", QMessageBox.Yes, QMessageBox.Yes))
            return
        studentId = self.Add_Edit_Widget.item(0,0).text()
        studentName = self.Add_Edit_Widget.item(0,1).text()
        password = self.Add_Edit_Widget.item(0,2).text()
        tel = self.Add_Edit_Widget.item(0,3).text()
        if (studentId == "" or studentName == "" or password == "" or tel =='' ):
            print(QMessageBox.warning(self, "警告", "信息不完整", QMessageBox.Yes, QMessageBox.Yes))
            return
        sql = "SELECT * FROM User  WHERE StudentId='%s'" % studentId
        self.query = db.query(sql)
        if (self.query != ()):
            print(QMessageBox.warning(self, "警告", "学生ID重复", QMessageBox.Yes, QMessageBox.Yes))
            return
        # 从User表添加用户
        sql = "INSERT INTO USER VALUES ('%s','%s','%s',0,'%s')" % (studentId, studentName, password, tel)
        db.exec_(sql)
        print(QMessageBox.information(self, "提示", "添加用户成功", QMessageBox.Yes, QMessageBox.Yes))
        studentId = self.Add_Edit_Widget.item(0,0).setText('')
        studentName = self.Add_Edit_Widget.item(0,1).setText('')
        password = self.Add_Edit_Widget.item(0,2).setText('')
        tel = self.Add_Edit_Widget.item(0,3).setText('')
        self.updateUI()
        return

    def DeleteStu(self):
        if (self.deleteId == "" and self.deleteName == ""):
            print(QMessageBox.warning(self, "警告", "请选中要删除的用户", QMessageBox.Yes, QMessageBox.Yes))
            return
        if (QMessageBox.information(self, "提示", "删除用户:%s,%s\n用户一经删除将无法恢复，是否继续?" % (self.deleteId, self.deleteName),
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No) == QMessageBox.No):
            return
        # 从User表删除用户
        sql = "DELETE FROM User WHERE StudentId='%s'" % (self.deleteId)
        db.exec_(sql)
        # 归还所有书籍
        sql = "SELECT * FROM User_Book  WHERE StudentId='%s' AND BorrowState=1" % self.deleteId
        self.query = db.query(sql)
        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        while (self.query != ()):
            bookId = self.query[0][1]
            sql = "UPDATE Book SET NumCanBorrow=NumCanBorrow+1 WHERE BookId='%s'" % bookId
            db.exec_(sql)
        sql = "UPDATE User_Book SET ReturnTime='%s',BorrowState=0 WHERE StudentId='%s' AND BorrowState=1" % (
            timenow, self.deleteId)
        db.exec_(sql)
        print(QMessageBox.information(self, "提示", "删除用户成功", QMessageBox.Yes, QMessageBox.Yes))
        self.updateUI()
        return

    def EditStu(self):
            #获得表格输入
            if (self.Editing_Edit_Widget.item(0,0) == None or self.Editing_Edit_Widget.item(0,1) == None or self.Editing_Edit_Widget.item(0,2) == None or self.Editing_Edit_Widget.item(0,3) == None):
                print(QMessageBox.warning(self, "警告", "信息不完整,无法修改", QMessageBox.Yes, QMessageBox.Yes))
                return
            studentId = self.Editing_Edit_Widget.item(0,0).text()
            studentName = self.Editing_Edit_Widget.item(0,1).text()
            password = self.Editing_Edit_Widget.item(0,2).text()
            tel = self.Editing_Edit_Widget.item(0,3).text()

            sql = "SELECT * FROM User  WHERE StudentId='%s'" % studentId
            self.query = db.query(sql)
            if (self.query == ()):
                print(QMessageBox.warning(self, "警告", "没有此学生ID", QMessageBox.Yes, QMessageBox.Yes))
                return
            # 从User表修改用户
            sql = "UPDATE USER SET Name='%s',Password='%s',tel='%s' WHERE StudentId='%s'" % (studentName,password,tel,studentId)
            db.exec_(sql)
            print(QMessageBox.information(self, "提示", "修改用户成功", QMessageBox.Yes, QMessageBox.Yes))
            studentId = self.Editing_Edit_Widget.item(0,0).setText('')
            studentName = self.Editing_Edit_Widget.item(0,1).setText('')
            password = self.Editing_Edit_Widget.item(0,2).setText('')
            tel = self.Editing_Edit_Widget.item(0,3).setText('')
            self.updateUI()
            return

    def updateUI(self):
        self.getResult()
        self.TableWidget.setRowCount(self.userCount)
        self.setRows()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainMindow = Stu_Manage()
    mainMindow.show()
    sys.exit(app.exec_())
