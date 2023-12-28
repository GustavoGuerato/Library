from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from login import Ui_MainWindow as Ui_Login
from signup import Ui_CadastroWindow
from mainmenu import Ui_MainWindow as Ui_MainMenu
import mysql.connector
import sys

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="nova_senha",
    database="test"
)

cursor = conexao.cursor()


class JanelaComIcone(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.definir_icone_janela()

    def definir_icone_janela(self):

        icone = QIcon(r'LibraConnect.ico')
        self.setWindowIcon(icone)


class Cadastro(JanelaComIcone, Ui_CadastroWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class Inicial(JanelaComIcone, Ui_MainMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class Login(JanelaComIcone, Ui_Login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.CriarContaBtn.clicked.connect(self.abrir_tela_cadastro)
        self.loginBtn.clicked.connect(self.logar)

    def logar(self):
        if not self.NomeInput and not self.SenhaInput:
            self.InputErro.setText('Preencha todos os dados')
        else:
            inicial.show()

    def abrir_tela_cadastro(self):
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
