import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from mediaAritmetica import Ui_MainWindow  # Substitua pelo nome do seu arquivo de interface gerada

class MediaAritmetica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que calcula a média
        self.ui.pushButton.clicked.connect(self.calcular_media)
    
    def calcular_media(self):
        try:
            nota1 = float(self.ui.lineEditNum1.text())
            nota2 = float(self.ui.lineEditNum2.text())
            nota3 = float(self.ui.lineEditNum3.text())
            
            media = (nota1 + nota2 + nota3) / 3
            
            # Exibir a média em uma caixa de mensagem
            QMessageBox.information(self, "Média Aritmética", f"A média das notas é: {media:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MediaAritmetica()
    janela.show()
    sys.exit(app.exec_())