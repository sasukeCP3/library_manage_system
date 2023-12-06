from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import db


class SignInWidget(QtWidgets.QWidget):
    is_admin_signal = pyqtSignal()
    is_student_signal = pyqtSignal(str)

    def __init__(self):
        super(SignInWidget, self).__init__()
        self.setupUi()

    def setupUi(self, ):
        self.resize(1200, 600)

        #设置字体。
        wel_font = QtGui.QFont()
        wel_font.setPointSize(40)

        font = QtGui.QFont()
        font.setPointSize(16)
        # 底层
        self.DownLayout = QtWidgets.QVBoxLayout(self)
        self.DownLayout.setObjectName("DownLayout")
        # 欢迎标识
        self.WelcomeLayout = QtWidgets.QHBoxLayout()
        self.WelcomeLayout.setObjectName("WelcomeLayout")

        self.WelcomeLabel = QtWidgets.QLabel(self)
        self.WelcomeLabel.setFont(wel_font)
        self.WelcomeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.WelcomeLayout.addWidget(self.WelcomeLabel)
        self.DownLayout.addLayout(self.WelcomeLayout)
        # 信息层
        self.InfoLayout = QtWidgets.QFormLayout()
        self.InfoLayout.setObjectName("InfoLayout")
        self.InfoLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.InfoLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.InfoLayout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        # sID标识
        self.sID = QtWidgets.QLabel(self)
        self.sID.setFont(font)
        self.sID.setObjectName("sID")
        self.InfoLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sID)
        # sID框
        self.sID_Edit = QtWidgets.QLineEdit(self)
        self.sID_Edit.setMaximumSize(QtCore.QSize(180, 32))
        self.sID_Edit.setFont(font)
        self.sID_Edit.setObjectName("sID_Edit")
        self.InfoLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sID_Edit)
        # 密码标识
        self.s_Password = QtWidgets.QLabel(self)
        self.s_Password.setFont(font)
        self.s_Password.setObjectName("s_Password")
        self.InfoLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s_Password)
        # 密码框
        self.s_Password_Edit = QtWidgets.QLineEdit(self)
        self.s_Password_Edit.setMaximumSize(QtCore.QSize(180, 32))
        self.s_Password_Edit.setFont(font)
        self.s_Password_Edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.s_Password_Edit.setObjectName("s_Password_Edit")
        self.InfoLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s_Password_Edit)
        # 登录按钮
        self.signIn_button = QtWidgets.QPushButton(self)
        self.signIn_button.setMaximumSize(QtCore.QSize(80, 40))
        self.signIn_button.setFont(font)
        self.signIn_button.setObjectName("signIn_button")
        self.InfoLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.signIn_button)
        self.DownLayout.addLayout(self.InfoLayout)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.signIn_button.clicked.connect(self.signInCheck)
        self.s_Password_Edit.returnPressed.connect(self.signInCheck)
        self.sID_Edit.returnPressed.connect(self.signInCheck)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.WelcomeLabel.setText(_translate("SignInWidget", "欢迎使用图书馆系统"))
        self.sID.setText(_translate("SignInWidget", "学号: "))
        self.s_Password.setText(_translate("SignInWidget", "密码: "))
        self.signIn_button.setText(_translate("SignInWidget", "登录"))

    def signInCheck(self):
        studentId = self.sID_Edit.text()
        password = self.s_Password_Edit.text()
        # 输入框为空
        if (studentId == "" or password == ""):
            print(QMessageBox.warning(self, "警告", "学号和密码不可为空", QMessageBox.Yes, QMessageBox.Yes))
            return
        
        sql = "SELECT * FROM user WHERE StudentId='%s'" % (studentId)
        query = db.query(sql)
        # 账号不存在 & 密码错误 & 学生 & 管理员
        if (query == ()):
            print(QMessageBox.information(self, "警告", "该账号不存在", QMessageBox.Yes, QMessageBox.Yes))
        else:
            query = query[0]
            if (studentId == query[0] and password == query[2]):
                # 管理员
                if (query[3] == 1):
                    self.is_admin_signal.emit()
                # 学生
                else:
                    self.is_student_signal.emit(studentId)
            else:
                print(QMessageBox.information(self, "警告", "密码错误", QMessageBox.Yes, QMessageBox.Yes))
        return


if __name__ == "__main__":

    # app = QApplication(sys.argv)
    # mainMindow = SignInWidget()
    # mainMindow.show()
    # sys.exit(app.exec_())
    pass