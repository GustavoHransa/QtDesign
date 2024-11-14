import sys
from PyQt5 import QtWidgets
from calculadora import Ui_MainWindow  # Importa a interface gerada

class CalculatorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão de calcular ao método
        self.ui.pushButtonCalcular.clicked.connect(self.calculate)

    def calculate(self):
        # Obtém os valores de entrada
        num1 = float(self.ui.lineEditnum1.text())
        num2 = float(self.ui.lineEditnum2.text())
        
        # Verifica qual radio button está selecionado e realiza a operação
        if self.ui.radioButtonSomar.isChecked():
            result = num1 + num2
        elif self.ui.radioButtonSubtrair.isChecked():
            result = num1 - num2
        elif self.ui.radioButtonMultiplicar.isChecked():
            result = num1 * num2
        elif self.ui.radioButtonDividir.isChecked():
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Erro: Divisão por zero"
        else:
            result = "Selecione uma operação"
        
        # Exibe o resultado
        self.ui.labelResultado.setText(str(result))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())