import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from login import Ui_MainWindow as Ui_Login
from signup import Ui_CadastroWindow


class Cadastro(QMainWindow, Ui_CadastroWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.SignUpButton.clicked.connect(self.abrir_login)

    def abrir_login(self):
        login.show()
        self.close()


class Login(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.CriarContaBtn.clicked.connect(self.abrir_tela_cadastro)

    def abrir_tela_cadastro(self):
        cadastro = Cadastro()
        cadastro.show()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    login = Login()
    login.show()

    sys.exit(qt.exec())
