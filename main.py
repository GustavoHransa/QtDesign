import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow ,QLineEdit, QLabel, QMessageBox
from home import Ui_MainWindow as ui_home
from cadastro import Ui_MainWindow as ui_cadastro
from agenda import Ui_MainWindow as ui_agenda
from relatorio import Ui_MainWindow as ui_relatorio
from controle import Ui_MainWindow as ui_controle

nome_arquivo ='pacientes.json'

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_home()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.cadastro)
        self.ui.pushButton_2.clicked.connect(self.cantrole)
        self.ui.pushButton_3.clicked.connect(self.relatorio)
        self.ui.pushButton_4.clicked.connect(self.agenda)
        self.ui.pushButton_5.clicked.connect(self.sair)

      


    def cadastro(self):
        self.abrir_cadastro = Cadastro(self)
        self.abrir_cadastro.show()
        self.close()
class Cadastro(QMainWindow):
        def __init__(self, main_window):
            super().__init__()
            self.ui = ui_cadastro()
            self.ui.setupUi(self)
            self.main_window = main_window
            self.ui.pushButton_6.clicked.connect(self.voltar_home)
            self.ui.pushButton_5.clicked.connect(self.salvar_cadastro)

            self.label_nome = QLabel("Nome:")
            self.lineedit_nome = QLineEdit()

            self.label_idade = QLabel("Idade:")
            self.lineedit_idade = QLineEdit()

        def voltar_home(self):
             self.main_window.show()
             self.close()


        def salvar_cadastro(self):
             

        self.addWidget(self.home_page)
        self.addWidget(self.cadastro_page)
        self.addWidget(self.agenda_page)
        self.addWidget(self.relatorio_page)
        self.addWidget(self.controle_dieta_page)

        self.setCurrentWidget(self.home_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())