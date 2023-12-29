from time import sleep
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt6.QtGui import QIcon
from login import Ui_MainWindow as Ui_Login
from signup import Ui_CadastroWindow
from Livros import Ui_MainWindow as Ui_livros
from PaginaInicial import Ui_MainWindow as Ui_MainMenu
from esqueciSenha import Ui_MainWindow as Ui_esqueciSenha
import mysql.connector
import string
import random
import sys


class JanelaComIcone(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.definir_icone_janela()

    def definir_icone_janela(self):
        icone = QIcon('../LibraConnect.ico')
        self.setWindowIcon(icone)


class EsqueciSenha(JanelaComIcone, Ui_esqueciSenha):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ChangeButton.clicked.connect(self.trocar_senha)

    def trocar_senha(self):
        nome = self.NomeInput.text()
        email = self.EmailInput.text()

        if self.verifica_dados(nome, email):
            nova_senha_temporaria = self.gerar_senha()
            try:
                update_senha = 'UPDATE clientes SET Senha = %s WHERE NomeCliente = %s AND Email = %s'
                cursor.execute(update_senha, (nova_senha_temporaria, nome, email))
                conexao.commit()
                print("Senha temporária trocada com sucesso!")
                self.NovaSenhaInput.setText(f'A sua nova senha é {nova_senha_temporaria}')
                return nova_senha_temporaria
            except mysql.connector.Error as err:
                print(f"Erro ao trocar a senha temporária: {err}")
        return None

    @staticmethod
    def gerar_senha(tamanho=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        return senha

    @staticmethod
    def verifica_dados(nome, email):
        try:
            query = 'SELECT * FROM clientes WHERE NomeCliente = %s AND Email = %s'
            cursor.execute(query, (nome, email))
            resultado = cursor.fetchone()

            if resultado:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Erro ao verificar dados: {err}")
            return False


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

    def adicionar_cliente(self, nome, sobrenome, email, telefone, senha):
        add_cliente = (
            'INSERT INTO clientes (NomeCliente, SobrenomeCliente, Email, Telefone, Senha) VALUES (%s, %s, %s, %s, %s)')
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
        self.LivrosBtn.clicked.connect(self.abrir_livros)
        self.livros = Livros()

    def abrir_livros(self):
        self.livros.show()


class Livros(JanelaComIcone, Ui_livros):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.carregar_livros()
        self.pushButton_2.clicked.connect(self.emprestar_livro)

    def carregar_livros(self):
        try:
            query = 'SELECT titulo FROM livros'
            cursor.execute(query)
            livros = cursor.fetchall()

            for livro in livros:
                item = QListWidgetItem(livro[0])
                self.listaLivros.addItem(item)

        except mysql.connector.Error as err:
            print(f"Erro ao carregar livros: {err}")


    def emprestar_livro(self, item):
        livro_id = self.listaLivros.currentItem().text().split('-')[0].strip()
        try:
            update_disponibilidade = 'UPDATE livros SET disponivel = 0 WHERE id = %s'
            cursor.execute(update_disponibilidade, (livro_id,))
            conexao.commit()
            print(f"Livro com ID {livro_id} emprestado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao marcar livro como emprestado: {err}")


class Login(JanelaComIcone, Ui_Login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.CriarContaBtn.clicked.connect(self.abrir_tela_cadastro)
        self.loginBtn.clicked.connect(self.logar)
        self.SenhaBtn.clicked.connect(self.abrir_tela_esqueci_senha)

    def logar(self):
        nome = self.NomeInput.text()
        senha = self.SenhaInput.text()

        if self.verificalogin(nome, senha):
            self.InputErro.setText('Login Bem Sucedido')
            sleep(5)
            inicial.show()
            login.close()
        else:
            self.InputErro.setText('Verifique seus dados!')

    def verificalogin(self, nome, senha):
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

    def abrir_tela_cadastro(self):
        cadastro.show()

    def abrir_tela_esqueci_senha(self):
        senha.show()


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
    senha = EsqueciSenha()
    login.show()
    sys.exit(qt.exec())
