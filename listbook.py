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

        self.button_back = QtWidgets.QPushButton("Geri gel")
        self.button_back.clicked.connect(self.back)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.table)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.button_back)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)

        self.setLayout(v_box)

        self.setFixedHeight(400)
        self.setFixedWidth(672)

    def back(self):
        from mainScreen import MainScreen
        self.mainscreen = MainScreen()
        self.mainscreen.show()
        self.close()