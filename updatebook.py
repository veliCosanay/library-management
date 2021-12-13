from PyQt5 import QtWidgets
import time
from database import DataBase
#GERİ tuşu olsun listbook2 ye göndersin

class UpdateBook(QtWidgets.QWidget):
    def __init__(self,id):
        self.selected_id = id
        super().__init__()
        self.init_ui()

    def init_ui(self):
        db = DataBase()
        data = db.duzen(self.selected_id)
        print(data)
        self.label_id = QtWidgets.QLabel("İd: ")
        self.lineEdit_id = QtWidgets.QLineEdit(str(data[0]))
        self.lineEdit_id.setEnabled(False)
    
        self.label_bookname = QtWidgets.QLabel("Kitabın Adı: ")
        self.lineEdit_bookname = QtWidgets.QLineEdit(str(data[1]))
        self.label_author = QtWidgets.QLabel("Yazarı: ")
        self.lineEdit_author = QtWidgets.QLineEdit(str(data[2]))
        self.label_numberOfpages = QtWidgets.QLabel("Sayfa sayısı: ")
        self.lineEdit_numberOfpages = QtWidgets.QLineEdit(str(data[3]))
        self.label_publisher = QtWidgets.QLabel("Yayınevi: ")
        self.lineEdit_publisher = QtWidgets.QLineEdit(str(data[4]))

        self.button_update = QtWidgets.QPushButton("Güncelle")
        self.button_update.clicked.connect(self.update)

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addWidget(self.label_id)
        h_box4.addWidget(self.lineEdit_id)
        
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
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addWidget(self.button_update)

        self.setLayout(v_box)

        self.setFixedHeight(400)
        self.setFixedWidth(672)

        self.show()

    def update(self):

        from listbook import ListBook
        self.listbook = ListBook()

        db = DataBase()
        db.KitapDüzenle(self.selected_id,self.lineEdit_bookname.text(),self.lineEdit_author.text(),self.lineEdit_numberOfpages.text(),self.lineEdit_publisher.text())
        
        QtWidgets.QMessageBox.about(
                self, "Güncelleme Başarılı", "Ana menüye gönderiliyorsunuz.")
        time.sleep(5)
        
        from mainScreen import MainScreen
        self.mainscreen = MainScreen()
        self.mainscreen.show()
        self.close()
