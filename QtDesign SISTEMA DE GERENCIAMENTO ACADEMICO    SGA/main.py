import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from listachamada.listachamada import JanelaChamadas
from cadastro.cadastroaluno import JanelaCadastroAlunos
from cadastrodenota.cadastronota import JanelaCadastroNotas
from relatorio.relatorio import JanelaRelatorios
from telainicial.telainicial import JanelaInicial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciamento Escolar")
        self.setGeometry(100, 100, 800, 600)

        # Menu
        menu = self.menuBar()
        arquivo_menu = menu.addMenu("Arquivo")

        # Ações do menu
        self.criar_acoes(arquivo_menu)

        # Tela inicial
        self.tela_inicial = JanelaInicial()
        self.setCentralWidget(self.tela_inicial)

    def criar_acoes(self, menu):
        # Ação para Chamadas
        chamadas_action = QAction("Chamadas", self)
        chamadas_action.triggered.connect(self.abrir_chamadas)
        menu.addAction(chamadas_action)

        # Ação para Cadastro de Alunos
        cadastro_alunos_action = QAction("Cadastro de Alunos", self)
        cadastro_alunos_action.triggered.connect(self.abrir_cadastro_alunos)
        menu.addAction(cadastro_alunos_action)

        # Ação para Cadastro de Notas
        cadastro_notas_action = QAction("Cadastro de Notas", self)
        cadastro_notas_action.triggered.connect(self.abrir_cadastro_notas)
        menu.addAction(cadastro_notas_action)

        # Ação para Relatórios
        relatorios_action = QAction("Relatórios", self)
        relatorios_action.triggered.connect(self.abrir_relatorios)
        menu.addAction(relatorios_action)

    def abrir_chamadas(self):
        self.janela_chamadas = JanelaChamadas()
        self.janela_chamadas.show()

    def abrir_cadastro_alunos(self):
        self.janela_cadastro_alunos = JanelaCadastroAlunos()
        self.janela_cadastro_alunos.show()

    def abrir_cadastro_notas(self):
        self.janela_cadastro_notas = JanelaCadastroNotas()
        self.janela_cadastro_notas.show()

    def abrir_relatorios(self):
        self.janela_relatorios = JanelaRelatorios()
        self.janela_relatorios.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

    from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class JanelaChamadas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chamadas")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tela de Chamadas"))
        self.setLayout(layout)

class JanelaCadastroAlunos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Alunos")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Nome do Aluno:"))
        self.nome_input = QLineEdit()
        layout.addWidget(self.nome_input)

        layout.addWidget(QLabel("Idade do Aluno:"))
        self.idade_input = QLineEdit()
        layout.addWidget(self.idade_input)

        self.cadastrar_button = QPushButton("Cadastrar Aluno")
        layout.addWidget(self.cadastrar_button)

        self.setLayout(layout)

class JanelaCadastroNotas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Notas")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Nome do Aluno:"))
        self.nome_input = QLineEdit()
        layout.addWidget(self.nome_input)

        layout.addWidget(QLabel("Nota:"))
        self.nota_input = QLineEdit()
        layout.addWidget(self.nota_input)

        self.cadastrar_button = QPushButton("Cadastrar Nota")
        layout.addWidget(self.cadastrar_button)

        self.setLayout(layout)

class JanelaRelatorios(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relatórios")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Relatórios de Alunos e Notas"))

        self.gerar_relatorio_button = QPushButton("Gerar Relatório")
        layout.addWidget(self.gerar_relatorio_button)

        self.setLayout(layout)

class JanelaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela Inicial")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Bem-vindo ao Sistema de Gerenciamento Escolar"))

        self.iniciar_button = QPushButton("Iniciar")
        layout.addWidget(self.iniciar_button)

        self.setLayout(layout)

