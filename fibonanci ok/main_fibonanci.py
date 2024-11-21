
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from fibonanci import Ui_MainWindow  # Importa a interface gerada

class Fibonacci(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que realiza a soma
        self.ui.pushButton.clicked.connect(self.calcular_fibonacci)
    
    def calcular_fibonacci(self):
        try:
            num_termos = int(self.ui.lineEdit.text())
            fib_sequence = self.fibonacci(num_termos)
            # Exibir a sequência em uma caixa de mensagem
            QMessageBox.information(self, "Sequência de Fibonacci", str(fib_sequence))
        except ValueError:
           QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")
    
    def fibonacci(self, n):
        fib_sequence = []
        a, b = 0, 1
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b
        return fib_sequence

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Fibonacci()
    janela.show()
    sys.exit(app.exec_())

