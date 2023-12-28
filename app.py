from time import sleep
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from login import Ui_MainWindow as Ui_Login
from signup import Ui_CadastroWindow
from mainmenu import Ui_MainWindow as Ui_MainMenu
import mysql.connector
import sys


class JanelaComIcone(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.definir_icone_janela()

    def definir_icone_janela(self):
        icone = QIcon('LibraConnect.ico')
        self.setWindowIcon(icone)


class Cadastro(JanelaComIcone, Ui_CadastroWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.SignUpButton.clicked.connect(self.cadastrar)

    def cadastrar(self):
        nome = self.NomeInput.text()
        sobrenome = self.SobrenomeInput.text()
        email = self.EmailInput.text()
        telefone = self.TelInput.text()
        senha = self.SenhaInput.text()

        self.adicionar_cliente(nome, sobrenome, email, telefone, senha)

    @staticmethod
    def adicionar_cliente(nome, sobrenome, email, telefone, senha):
        add_cliente = ('INSERT INTO clientes (NomeCliente, SobrenomeCliente, Email, Telefone, Senha) VALUES (%s, %s, '
                       '%s, %s, %s)')
        dados_cliente = (nome, sobrenome, email, telefone, senha)

        try:
            cursor.execute(add_cliente, dados_cliente)
            conexao.commit()
            print("Cliente adicionado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar cliente: {err}")


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
        nome = self.NomeInput.text()
        senha = self.SenhaInput.text()

        if self.verificalogin(nome, senha):
            self.InputErro.setText('login Bem Sucedido')
            sleep(5)
            inicial.show()
            login.close()
        else:
            self.InputErro.setText('Verifique seus dados!')

    @staticmethod
    def verificalogin(nome, senha):
        try:
            query = 'SELECT * FROM clientes WHERE NomeCliente = %s AND Senha = %s'
            cursor.execute(query, (nome, senha))
            resultado = cursor.fetchone()

            if resultado:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Erro ao verificar login: {err}")
            return False

    @staticmethod
    def abrir_tela_cadastro():
        cadastro.show()


conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="nova_senha",
    database="test"
)

cursor = conexao.cursor()

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    login = Login()
    cadastro = Cadastro()
    inicial = Inicial()
    login.show()
    sys.exit(qt.exec())
