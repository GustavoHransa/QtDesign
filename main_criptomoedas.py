import subprocess,sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from criptomoedas import Ui_MainWindow 

class executarBat(QMainWindow,Ui_MainWindow):
   
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.BTC.clicked.connect(self.bat_file_path)
        bat_file_path = "teste.txt"
        subprocess.Popen(bat_file_path)

    def bat_file_path(self):
       
        self.Resultado.setText(f"Executando")

app= QApplication(subprocess,sys.argv)
janela = executarBat()
janela.show()
sys.exit(app.exec_())