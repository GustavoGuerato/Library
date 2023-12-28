import password
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from login import Ui_MainWindow as Ui_Login
from signup import Ui_CadastroWindow
from mainmenu import Ui_MainWindow as Ui_MainMenu
import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="gg08142325",
    database="test"
)

cursor = conexao.cursor()


class Cadastro(QMainWindow, Ui_CadastroWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class Inicial(QMainWindow, Ui_MainMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class Login(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.CriarContaBtn.clicked.connect(self.abrir_tela_cadastro)
        self.loginBtn.clicked.connect(self.logar)

    def verifica(self):
        if not self.NomeInput and self.SenhaInput:
            self.InputErro.setText('preencha todos os dados')

    @staticmethod
    def logar():
        inicial.show()

    @staticmethod
    def abrir_tela_cadastro():
        cadastro.show()


cursor.close()
conexao.close()
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    login = Login()
    cadastro = Cadastro()
    inicial = Inicial()
    login.show()
    sys.exit(qt.exec())
