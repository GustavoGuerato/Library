# Form implementation generated from reading ui file 'NovaSenha.ui'
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
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ChangeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ChangeButton.setGeometry(QtCore.QRect(110, 300, 151, 51))
        self.ChangeButton.setObjectName("ChangeButton")
        self.SenhaAtualInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SenhaAtualInput.setGeometry(QtCore.QRect(200, 60, 161, 22))
        self.SenhaAtualInput.setObjectName("SenhaAtualInput")
        self.NovaSenhaInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.NovaSenhaInput.setGeometry(QtCore.QRect(200, 120, 161, 22))
        self.NovaSenhaInput.setObjectName("NovaSenhaInput")
        self.EmailLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.EmailLabel.setGeometry(QtCore.QRect(70, 60, 111, 21))
        self.EmailLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.EmailLabel.setObjectName("EmailLabel")
        self.NomeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.NomeLabel.setGeometry(QtCore.QRect(98, 120, 81, 20))
        self.NomeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.NomeLabel.setObjectName("NomeLabel")
        self.ErroInput = QtWidgets.QLabel(parent=self.centralwidget)
        self.ErroInput.setGeometry(QtCore.QRect(80, 250, 211, 20))
        self.ErroInput.setText("")
        self.ErroInput.setObjectName("ErroInput")
        self.NomeLabel_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.NomeLabel_2.setGeometry(QtCore.QRect(80, 170, 101, 20))
        self.NomeLabel_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.NomeLabel_2.setObjectName("NomeLabel_2")
        self.confirmaSenhaInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.confirmaSenhaInput.setGeometry(QtCore.QRect(200, 170, 161, 22))
        self.confirmaSenhaInput.setObjectName("confirmaSenhaInput")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "trocar senha"))
        self.ChangeButton.setText(_translate("MainWindow", "Recuperar Senha"))
        self.EmailLabel.setText(_translate("MainWindow", "Senha Atual"))
        self.NomeLabel.setText(_translate("MainWindow", "Nova Senha"))
        self.NomeLabel_2.setText(_translate("MainWindow", "Confirme senha"))
