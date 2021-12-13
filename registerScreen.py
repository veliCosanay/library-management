from PyQt5 import QtWidgets
import time
from database import DataBase


class RegisterScreen(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.label_text = QtWidgets.QLabel("KAYIT OL")

        # kullanıcı adı texti
        self.label_userName = QtWidgets.QLabel("Kullanıcı adınızı giriniz: ")

        # kullanıcı adı girişi
        self.lineEdit_userName = QtWidgets.QLineEdit()

        # şifre texti
        self.label_password = QtWidgets.QLabel("Şifrenizi giriniz: ")

        # şifre girişi
        self.lineEdit_password = QtWidgets.QLineEdit()
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)

        # kayıt butonu
        self.button_register = QtWidgets.QPushButton("Kayıt Ol")

        self.button_register.clicked.connect(self.register)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.label_userName)
        h_box.addWidget(self.lineEdit_userName)

        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addWidget(self.label_password)
        h2_box.addWidget(self.lineEdit_password)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.label_text)
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addLayout(h2_box)
        v_box.addStretch()
        v_box.addWidget(self.button_register)

        self.setLayout(v_box)

        self.setFixedHeight(400)
        self.setFixedWidth(672)

    def register(self):
        
        db = DataBase()
        db.UyeEkle(self.lineEdit_userName.text(), self.lineEdit_password.text())

        QtWidgets.QMessageBox.about(
                self, "Bilgi", "Kayıt başarılı. Ana menüye gönderiliyorsunuz.")
        time.sleep(2)
        
        from loginScreen import LoginScreen
        self.loginscreen = LoginScreen()
        self.loginscreen.show()
        self.close()
