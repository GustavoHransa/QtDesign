import sys
from PyQt5 import QtWidgets
from login import Ui_LoginForm  # Importa a interface gerada

class LoginApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)

        # Conectar o botão de login ao método de verificação
        self.ui.pushButton.clicked.connect(self.check_login)

    def check_login(self):
        username = self.ui.lineUsuario.text()
        password = self.ui.lineSenha.text()

        # Aqui você pode implementar sua lógica de autenticação
        if username == "admin" and password == "1234":
            self.ui.labelMessage.setText("Login bem-sucedido!")
        else:
            self.ui.labelMessage.setText("Usuário ou senha incorretos!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())