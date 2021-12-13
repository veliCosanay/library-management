from PyQt5 import QtWidgets

class MainScreen(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.button_addbook = QtWidgets.QPushButton("kitap ekle")
        self.button_addbook.clicked.connect(self.addBook)
        self.button_listbook = QtWidgets.QPushButton("kitapları listele")
        self.button_listbook.clicked.connect(self.listBook)
        self.button_upbook = QtWidgets.QPushButton("kitapları düzenle")
        self.button_upbook.clicked.connect(self.upbook)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button_addbook)
        v_box.addWidget(self.button_listbook)
        v_box.addWidget(self.button_upbook)

        self.setFixedHeight(400)
        self.setFixedWidth(672)

        self.setLayout(v_box)

        

    def addBook(self):
        from addbook import AddBook
        self.addbook = AddBook()
        self.addbook.show()
        self.close()

    def listBook(self):
        from listbook import ListBook
        self.listbook = ListBook()
        self.listbook.show()
        self.close()

    def upbook(self):
        from listbook2 import ListBook
        self.listbook = ListBook()
        self.listbook.show()
        self.close()

