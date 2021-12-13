from PyQt5 import QtWidgets
from database import DataBase

class AddBook(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.label_bookname = QtWidgets.QLabel("Kitabın Adı: ")
        self.lineEdit_bookname = QtWidgets.QLineEdit()
        self.label_author = QtWidgets.QLabel("Yazarı: ")
        self.lineEdit_author = QtWidgets.QLineEdit()
        self.label_numberOfpages = QtWidgets.QLabel("Sayfa sayısı: ")
        self.lineEdit_numberOfpages = QtWidgets.QLineEdit()
        self.label_publisher = QtWidgets.QLabel("Yayınevi: ")
        self.lineEdit_publisher = QtWidgets.QLineEdit()

        self.button_register = QtWidgets.QPushButton("Kayıt Et")
        self.button_register.clicked.connect(self.register)

        self.button_back = QtWidgets.QPushButton("Ana menüye dön")
        self.button_back.clicked.connect(self.back)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.label_bookname)
        h_box.addWidget(self.lineEdit_bookname)

        h1_box = QtWidgets.QHBoxLayout()
        h1_box.addWidget(self.label_author)
        h1_box.addWidget(self.lineEdit_author)

        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addWidget(self.label_numberOfpages)
        h2_box.addWidget(self.lineEdit_numberOfpages)

        h3_box = QtWidgets.QHBoxLayout()
        h3_box.addWidget(self.label_publisher)
        h3_box.addWidget(self.lineEdit_publisher)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addWidget(self.button_register)
        v_box.addWidget(self.button_back)

        self.setLayout(v_box)

        self.setFixedHeight(400)
        self.setFixedWidth(300)

        self.show()

    def register(self):

        db = DataBase()
        db.KitapEkle(self.lineEdit_bookname.text(),self.lineEdit_author.text(),self.lineEdit_numberOfpages.text(),self.lineEdit_publisher.text())

    def back(self):
        from mainScreen import MainScreen
        self.mainscreen = MainScreen()
        self.mainscreen.show()
        self.close()
        


