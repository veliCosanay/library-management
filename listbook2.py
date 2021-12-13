from PyQt5 import QtCore, QtWidgets
from database import DataBase


class ListBook(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.table = QtWidgets.QTableWidget()

        liste = ["İd", "Kitabın Adı", "Yazarı", "Sayfa Sayısı", "Yayınevi"]
        for i in range(len(liste)):
            self.rowPosition = self.table.rowCount()
            self.table.insertColumn(self.rowPosition)
        self.table.setHorizontalHeaderLabels(liste)

        self.db = DataBase()
        liste = self.db.KitapListele()

        for _ in liste:
            self.rowPosition = self.table.rowCount()
            self.table.insertRow(self.rowPosition)

        for row, book in enumerate(liste):

            for column, prop in enumerate(book):
                item = QtWidgets.QTableWidgetItem(str(prop))
                item.setTextAlignment(QtCore.Qt.AlignCenter)

                self.table.setItem(row, column,
                                QtWidgets.QTableWidgetItem(
                                    item))

        self.button_update = QtWidgets.QPushButton("Güncelle")
        self.button_update.clicked.connect(self.update)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.table)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.button_update)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)

        self.setLayout(v_box)

        self.setFixedHeight(400)
        self.setFixedWidth(672)

    def getId(self):
        liste = self.table.selectedItems()
        return liste[0].text()

    def update(self):
        liste = self.table.selectedItems()
        from updatebook import UpdateBook
        self.updatebook = UpdateBook(liste[0].text())
        self.updatebook.show()
        self.close()