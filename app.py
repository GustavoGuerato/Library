from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QCheckBox, QLabel

from PyQt6.QtGui import QIcon, QPalette, QColor
from PyQt6.QtCore import Qt
from login import Ui_MainWindow as Ui_Login
from signup import Ui_CadastroWindow
from Livros import Ui_MainWindow as Ui_livros
from PaginaInicial import Ui_MainWindow as Ui_MainMenu
from esqueciSenha import Ui_MainWindow as Ui_esqueciSenha
from Carrinho import Ui_MainWindow as Ui_carrinho
from Conta import Ui_MainWindow as Ui_Conta
from NovaSenha import Ui_MainWindow as Ui_Novasenha
from Config import Ui_MainWindow as Ui_Config
import mysql.connector
import string
import random
import sys
from time import sleep


class JanelaComIcone(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.definir_icone_janela()

    def definir_icone_janela(self):
        icone = QIcon('LibraConnect.ico')
        self.setWindowIcon(icone)


class Novasenha(JanelaComIcone, Ui_Novasenha):
    def __init__(self, cursor, parent=None):
        super().__init__(parent)
        self.cursor = cursor
        self.nome = None
        self.email = None
        self.senha_atual = None
        self.setupUi(self)
        self.ChangeButton.clicked.connect(self.alterar_senha)

    def set_info(self, nome, email, senha_atual):
        self.nome = nome
        self.email = email
        self.senha_atual = senha_atual

    def alterar_senha(self):
        nova_senha = self.NovaSenhaInput.text()
        confirma_senha = self.confirmaSenhaInput.text()

        try:
            if nova_senha and confirma_senha and nova_senha != self.senha_atual:
                update_senha = 'UPDATE clientes SET Senha = %s WHERE NomeCliente = %s AND Email = %s'
                self.cursor.execute(update_senha, (nova_senha, self.nome, self.email))
                self.cursor.commit()
                print("Senha alterada com sucesso!")
            else:
                print("Por favor, insira e confirme uma nova senha diferente da atual.")
        except Exception as e:
            print(f"Erro ao alterar a senha: {e}")


class Config(JanelaComIcone, Ui_Config):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.DarkCheckBox.clicked.connect(self.dark_mode)
        self.IdiomaBox.currentIndexChanged.connect(self.trocar_idioma)

        self.translations = {
            "Dark Mode": {"Portugues": "Modo Escuro", "Ingles": "Dark Mode", "Espanhol": "Modo Oscuro"},
            "White mode": {"Portugues": "Modo Claro", "Ingles": "White Mode", "Espanhol": "Modo Claro"},
            # Adicione mais traduções conforme necessário
        }

    def dark_mode(self):
        palette = self.palette()

        if self.DarkCheckBox.isChecked():
            palette.setColor(QPalette.ColorRole.Window, QColor('#333333'))
            palette.setColor(QPalette.ColorRole.WindowText, QColor('#ffffff'))
        else:
            palette.setColor(QPalette.ColorRole.Window, QColor('#ffffff'))
            palette.setColor(QPalette.ColorRole.WindowText, QColor('#000000'))

        self.setPalette(palette)

    def trocar_idioma(self):
        idioma_selecionado = self.IdiomaBox.currentText()

        for key, translation in self.translations.items():
            translated_text = translation.get(idioma_selecionado, key)
            widget = self.findChild(QCheckBox, key)
            if widget:
                widget.setText(translated_text)


class Config(JanelaComIcone, Ui_Config):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.DarkCheckBox.clicked.connect(self.dark_mode)
        self.IdiomaBox.currentIndexChanged.connect(self.trocar_idioma)

        self.translations = {
            "Dark Mode": {"Portugues": "Modo Escuro", "Ingles": "Dark Mode", "Espanhol": "Modo Oscuro"},
            "White mode": {"Portugues": "Modo Claro", "Ingles": "White Mode", "Espanhol": "Modo Claro"},
        }

    def dark_mode(self):
        palette = self.palette()

        if self.DarkCheckBox.isChecked():
            palette.setColor(QPalette.ColorRole.Window, QColor('#333333'))
            palette.setColor(QPalette.ColorRole.WindowText, QColor('#ffffff'))
        else:
            palette.setColor(QPalette.ColorRole.Window, QColor('#ffffff'))
            palette.setColor(QPalette.ColorRole.WindowText, QColor('#000000'))

        self.setPalette(palette)

    def trocar_idioma(self):
        idioma_selecionado = self.IdiomaBox.currentText()

        for key, translation in self.translations.items():
            translated_text = translation.get(idioma_selecionado, key)
            widget = self.findChild(QCheckBox, key)
            if widget:
                widget.setText(translated_text)


class Conta(JanelaComIcone, Ui_Conta):
    def __init__(self, cursor, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.senha = Novasenha(cursor)
        self.SenhaBtn.clicked.connect(self.abrir_tela_senha)

    def abrir_tela_senha(self):
        self.senha.show()


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

        check_duplicate_query = (
            'SELECT COUNT(*) FROM clientes WHERE NomeCliente = %s AND SobrenomeCliente = %s AND Email = %s AND '
            'Telefone = %s AND Senha = %s'
        )
        check_data = (nome, sobrenome, email, telefone, senha)

        try:
            cursor.execute(check_duplicate_query, check_data)
            result = cursor.fetchone()

            if result[0] > 0:
                print("Erro: Cliente com dados duplicados já existe no banco de dados.")
            else:
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
        self.CarrinhoBtn.clicked.connect(self.abrir_carrinho)
        self.ContaBtn.clicked.connect(self.abrir_conta)
        self.ConfigBtn.clicked.connect(self.abrir_config)
        self.livros = Livros()
        self.carrinho = Carrinho()
        self.conta = Conta(cursor)
        self.config = Config()

    def abrir_livros(self):
        self.livros.show()

    def abrir_carrinho(self):
        self.carrinho.show()

    def abrir_conta(self):
        self.conta.show()

    def abrir_config(self):
        self.config.show()


class Livros(JanelaComIcone, Ui_livros):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.carregar_livros()
        self.pushButton_2.clicked.connect(self.emprestar_livro)
        self.pushButton.clicked.connect(self.colocar_no_carrinho)

    def carregar_livros(self):
        try:
            query = 'SELECT Titulo FROM livros WHERE status = 1 AND carrinho = 0'
            cursor.execute(query)
            livros = cursor.fetchall()

            self.listaLivros.clear()

            for livro in livros:
                item = QListWidgetItem(livro[0])
                self.listaLivros.addItem(item)

        except mysql.connector.Error as err:
            print(f"Erro ao carregar livros: {err}")

    def emprestar_livro(self):
        if self.listaLivros.currentItem():
            livro_titulo = self.listaLivros.currentItem().text()

            try:
                update_disponibilidade = 'UPDATE livros SET status = 0 WHERE titulo = %s'
                cursor.execute(update_disponibilidade, (livro_titulo,))
                print(f"Livro '{livro_titulo}' emprestado com sucesso!")
                conexao.commit()
            except mysql.connector.Error as err:
                print(f"Erro ao marcar livro como emprestado: {err}")
                conexao.rollback()
            except Exception as e:
                print(f"Erro desconhecido: {e}")
                conexao.rollback()

    def colocar_no_carrinho(self):
        if self.listaLivros.currentItem():
            livro_titulo = self.listaLivros.currentItem().text()

            try:
                update_disponibilidade = 'UPDATE livros SET carrinho = 1, status = 0 WHERE titulo = %s'
                cursor.execute(update_disponibilidade, (livro_titulo,))
                print(f"Livro '{livro_titulo}' foi colocado no carrinho com sucesso!")
                conexao.commit()
            except mysql.connector.Error as err:
                print(f"Erro ao colocar livro no carrinho: {err}")
                conexao.rollback()
            except Exception as e:
                print(f"Erro desconhecido: {e}")
                conexao.rollback()


class Carrinho(JanelaComIcone, Ui_carrinho):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.carregar_livros_carrinho()
        self.FinishBtn.clicked.connect(self.finalizar_emprestimo)
        self.DevolverBtn.clicked.connect(self.devolver_livro)

    def carregar_livros_carrinho(self):
        try:
            query = 'SELECT Titulo FROM livros WHERE status = 0 AND carrinho = 1'
            cursor.execute(query)
            livros = cursor.fetchall()

            self.listaCarrinho.clear()

            for livro in livros:
                item = QListWidgetItem(livro[0])
                self.listaCarrinho.addItem(item)

        except mysql.connector.Error as err:
            print(f"Erro ao carregar livros do carrinho: {err}")

    def finalizar_emprestimo(self):
        livro_titulo = self.listaCarrinho.currentItem().text()
        try:
            update_disponibilidade = 'UPDATE livros SET carrinho = 0 WHERE titulo = %s'
            cursor.execute(update_disponibilidade, (livro_titulo,))
            print(f"Livro '{livro_titulo}' emprestado com sucesso!")
            conexao.commit()
        except mysql.connector.Error as err:
            print(f"Erro ao marcar livro como emprestado: {err}")
            conexao.rollback()
        except Exception as e:
            print(f"Erro desconhecido: {e}")
            conexao.rollback()

    def devolver_livro(self):
        livro_titulo = self.listaCarrinho.currentItem().text()
        try:
            update_disponibilidade = 'UPDATE livros SET carrinho = 0, status = 1 WHERE titulo = %s'
            cursor.execute(update_disponibilidade, (livro_titulo,))
            print(f"Livro '{livro_titulo}' foi devolvido com sucesso!")
            conexao.commit()
        except mysql.connector.Error as err:
            print(f"Erro ao marcar livro como devolvido: {err}")
            conexao.rollback()
        except Exception as e:
            print(f"Erro desconhecido: {e}")
            conexao.rollback()


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
