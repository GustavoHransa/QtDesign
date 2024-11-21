import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from imparOupar import Ui_MainWindow  # Substitua pelo nome do seu arquivo de interface gerada

class ParImpar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que verifica par ou ímpar
        self.ui.pushButton.clicked.connect(self.verificar_par_impar)
    
    def verificar_par_impar(self):
        try:
            numero = int(self.ui.lineEditNum1.text())
            if numero % 2 == 0:
                resultado = "O número é par."
            else:
                resultado = "O número é ímpar."
            
            # Exibir o resultado em uma caixa de mensagem
            QMessageBox.information(self, "Resultado", resultado)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ParImpar()
    janela.show()
    sys.exit(app.exec_())