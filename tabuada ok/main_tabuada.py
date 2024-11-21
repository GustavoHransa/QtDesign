import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from tabuada import Ui_MainWindow  # Substitua pelo nome do seu arquivo de interface gerada

class Tabuada(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que calcula a tabuada
        self.ui.pushButton.clicked.connect(self.calcular_tabuada)
    
    def calcular_tabuada(self):
        try:
            numero = int(self.ui.lineEdit.text())
            tabuada = self.gerar_tabuada(numero)
            # Exibir a tabuada em uma caixa de mensagem
            QMessageBox.information(self, "Tabuada", tabuada)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")
    
    def gerar_tabuada(self, n):
        resultado = ""
        for i in range(1, 11):  # Gera a tabuada de 1 a 10
            resultado += f"{n} x {i} = {n * i}\n"
        return resultado

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Tabuada()
    janela.show()
    sys.exit(app.exec_())