# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        icon = QtGui.QIcon.fromTheme("system-search")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NomeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.NomeLabel.setGeometry(QtCore.QRect(40, 100, 36, 16))
        self.NomeLabel.setObjectName("NomeLabel")
        self.NomeInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.NomeInput.setGeometry(QtCore.QRect(80, 100, 261, 22))
        self.NomeInput.setStyleSheet("QLineEdit{\n"
"border-radius: 10px\n"
"}")
        self.NomeInput.setObjectName("NomeInput")
        self.SenhaLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SenhaLabel.setGeometry(QtCore.QRect(40, 140, 35, 16))
        self.SenhaLabel.setObjectName("SenhaLabel")
        self.SenhaInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SenhaInput.setGeometry(QtCore.QRect(80, 140, 261, 22))
        self.SenhaInput.setStyleSheet("QLineEdit{\n"
"border-radius: 10px}")
        self.SenhaInput.setObjectName("SenhaInput")
        self.loginBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(40, 250, 91, 41))
        self.loginBtn.setStyleSheet("QPushButton {\n"
"                border-radius: 10px;\n"
"                padding: 10px;\n"
"                background-color: #7FF517;\n"
"                color: #ffffff;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #71D716;\n"
"            }")
        self.loginBtn.setObjectName("loginBtn")
        self.SenhaBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SenhaBtn.setGeometry(QtCore.QRect(240, 250, 101, 41))
        self.SenhaBtn.setStyleSheet("QPushButton {\n"
"                border-radius: 10px;\n"
"                padding: 10px;\n"
"                background-color: #FF0000;\n"
"                color: #ffffff;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #ED0000;\n"
"            }")
        self.SenhaBtn.setObjectName("SenhaBtn")
        self.CriarContaBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CriarContaBtn.setGeometry(QtCore.QRect(140, 250, 91, 41))
        self.CriarContaBtn.setStyleSheet("QPushButton {\n"
"                border-radius: 10px;\n"
"                padding: 10px;\n"
"                background-color: #3498db;\n"
"                color: #ffffff;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #2980b9;\n"
"            }")
        self.CriarContaBtn.setObjectName("CriarContaBtn")
        self.InputErro = QtWidgets.QLabel(parent=self.centralwidget)
        self.InputErro.setGeometry(QtCore.QRect(90, 200, 191, 20))
        self.InputErro.setText("")
        self.InputErro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputErro.setObjectName("InputErro")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log-in Biblioteca"))
        self.NomeLabel.setText(_translate("MainWindow", "Nome:"))
        self.SenhaLabel.setText(_translate("MainWindow", "Senha:"))
        self.loginBtn.setText(_translate("MainWindow", "Log-in"))
        self.SenhaBtn.setText(_translate("MainWindow", "Esqueci a senha"))
        self.CriarContaBtn.setText(_translate("MainWindow", "Criar Conta"))
