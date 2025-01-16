from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from lista2025 import Ui_MainWindow


class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # Conectar botoes as funções
        self.adicionar.clicked.connect(self.Add_Files)
        self.remover.clicked.connect(self.Remover_Meta)

    #Criar funçoes dos botões

    # Adicionar metas
    def Add_Files(self):
        meta = self.lineEdit.text()
        if meta:
            item = QListWidgetItem(meta)
            item.setCheckState(0)

            self.listWidget.addItem(item)
            self.lineEdit.clear()

        
    # Remover Metas
        
    def Remover_Meta(self):
        selected_item = self.listWidget.currentRow()
        if selected_item >= 0:
            self.listWidget.takeItem(selected_item)

        
if __name__ == "__main__":
    app = QApplication([])
    window = main()
    window.show()
    app.exec_()



    