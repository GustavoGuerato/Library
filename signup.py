# Form implementation generated from reading ui file 'SignUp.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CadastroWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SignUpButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SignUpButton.setGeometry(QtCore.QRect(150, 340, 111, 51))
        self.SignUpButton.setObjectName("SignUpButton")
        self.NomeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.NomeLabel.setGeometry(QtCore.QRect(40, 60, 81, 31))
        self.NomeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.NomeLabel.setObjectName("NomeLabel")
        self.NomeInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.NomeInput.setGeometry(QtCore.QRect(130, 70, 231, 22))
        self.NomeInput.setObjectName("NomeInput")
        self.SobrenomeInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SobrenomeInput.setGeometry(QtCore.QRect(130, 110, 231, 22))
        self.SobrenomeInput.setObjectName("SobrenomeInput")
        self.SobrenomeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SobrenomeLabel.setGeometry(QtCore.QRect(40, 100, 81, 31))
        self.SobrenomeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.SobrenomeLabel.setObjectName("SobrenomeLabel")
        self.EmailLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.EmailLabel.setGeometry(QtCore.QRect(40, 140, 81, 31))
        self.EmailLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.EmailLabel.setObjectName("EmailLabel")
        self.TelefoneLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.TelefoneLabel.setGeometry(QtCore.QRect(40, 190, 81, 31))
        self.TelefoneLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.TelefoneLabel.setObjectName("TelefoneLabel")
        self.EmailInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.EmailInput.setGeometry(QtCore.QRect(130, 150, 231, 22))
        self.EmailInput.setObjectName("EmailInput")
        self.TelInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.TelInput.setGeometry(QtCore.QRect(130, 200, 231, 22))
        self.TelInput.setObjectName("TelInput")
        self.SenhaLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SenhaLabel.setGeometry(QtCore.QRect(40, 240, 81, 31))
        self.SenhaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.SenhaLabel.setObjectName("SenhaLabel")
        self.SenhaInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SenhaInput.setGeometry(QtCore.QRect(130, 250, 231, 22))
        self.SenhaInput.setObjectName("SenhaInput")
        self.InfoLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.InfoLabel.setGeometry(QtCore.QRect(170, 300, 49, 16))
        self.InfoLabel.setText("")
        self.InfoLabel.setObjectName("InfoLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SignUp"))
        self.SignUpButton.setText(_translate("MainWindow", "Cadastrar"))
        self.NomeLabel.setText(_translate("MainWindow", "Nome:"))
        self.SobrenomeLabel.setText(_translate("MainWindow", "Sobrenome:"))
        self.EmailLabel.setText(_translate("MainWindow", "E-Mail"))
        self.TelefoneLabel.setText(_translate("MainWindow", "Telefone"))
        self.SenhaLabel.setText(_translate("MainWindow", "Senha"))
