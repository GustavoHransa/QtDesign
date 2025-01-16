from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox
from lista import Ui_MainWindow
from PyQt5 import QtCore


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Definir a data atual no QDateEdit
        self.dateEdit.setDate(QtCore.QDate.currentDate())  # Define a data atual

        self.salvar.clicked.connect(self.Save_List)

    def Add_Files(self):
        meta = self.lineEdit.text()
        if meta:
            item = QListWidgetItem(meta)
            item.setCheckState(QtCore.Qt.Unchecked) 
            self.listWidget.addItem(item)
            self.lineEdit.clear()

    def Remover_Meta(self):
        selected_item = self.listWidget.currentRow()
        if selected_item >= 0:
            self.listWidget.takeItem(selected_item)

    def Save_List(self):
        selected_date = self.dateEdit.date().toString("dd/MM/yyyy") 
        message = f"A lista de chamada foi salva com a data: {selected_date}"
       
        QMessageBox.information(self, "Lista Salva", message)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()