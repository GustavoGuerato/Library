# Form implementation generated from reading ui file 'Carrinho.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 500)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listaCarrinho = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listaCarrinho.setGeometry(QtCore.QRect(10, 20, 601, 351))
        self.listaCarrinho.setObjectName("listaCarrinho")
        self.DevolverBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DevolverBtn.setGeometry(QtCore.QRect(100, 420, 141, 51))
        self.DevolverBtn.setObjectName("DevolverBtn")
        self.FinishBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.FinishBtn.setGeometry(QtCore.QRect(330, 420, 141, 51))
        self.FinishBtn.setObjectName("FinishBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Carrinho"))
        self.DevolverBtn.setText(_translate("MainWindow", "Devolver Livro"))
        self.FinishBtn.setText(_translate("MainWindow", "Finalizar Emprestimo"))
