from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from SignIn import SignInWidget
import sip
from AdminHome import AdminHome
from StudentHome import StudentHome


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.widget = SignInWidget()
        self.resize(1240, 620)
        self.setCentralWidget(self.widget)
        
        # "菜单栏"
        bar = self.menuBar()
        self.Menu = bar.addMenu("菜单栏")
        self.quitSignInAction = QAction("退出登录", self)
        self.quitAction = QAction("退出", self)
        self.Menu.addAction(self.quitSignInAction)
        self.Menu.addAction(self.quitAction)
        self.quitSignInAction.setEnabled(False)
        
        self.widget.is_admin_signal.connect(self.adminSignIn)
        self.widget.is_student_signal[str].connect(self.studentSignIn)
        self.Menu.triggered.connect(self.menuTriggered)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Main", "图书馆系统"))

    def adminSignIn(self):
        sip.delete(self.widget)
        self.widget = AdminHome()
        self.setCentralWidget(self.widget)
        self.quitSignInAction.setEnabled(True)

    def studentSignIn(self, studentId):
        sip.delete(self.widget)
        self.widget = StudentHome(studentId)
        self.setCentralWidget(self.widget)
        self.quitSignInAction.setEnabled(True)

    def menuTriggered(self, q):
        if (q.text() == "退出登录"):
            sip.delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_student_signal[str].connect(self.studentSignIn)
            # 按钮使能
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "退出"):
            qApp = QApplication.instance()
            qApp.quit()
        return


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainMindow = Main()
    mainMindow.show()
    sys.exit(app.exec_())
