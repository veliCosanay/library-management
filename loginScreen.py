from PyQt5 import QtCore, QtWidgets

from database import DataBase

from registerScreen import RegisterScreen

from mainScreen import MainScreen


class LoginScreen(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.label_text = QtWidgets.QLabel("KÜTÜPHANE UYGULAMASI")
        self.label_text.setStyleSheet("font-size: 25px;")
        self.label_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text.setFixedWidth(300)
        self.label_text2 = QtWidgets.QLabel("KULLANICI GİRİŞİ")
        self.label_text2.setStyleSheet("font-size: 15px;")
        self.label_text2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text2.setFixedWidth(300)

        # kullanıcı adı texti
        self.label_userName = QtWidgets.QLabel("Kullanıcı adınızı giriniz: ")
        self.label_userName.setFixedWidth(150)

        # kullanıcı adı girişi
        self.lineEdit_userName = QtWidgets.QLineEdit()
        self.lineEdit_userName.setFixedWidth(175)

        # şifre texti
        self.label_password = QtWidgets.QLabel("Şifrenizi giriniz: ")
        self.label_password.setFixedWidth(150)

        # şifre girişi
        self.lineEdit_password = QtWidgets.QLineEdit()
        self.lineEdit_password.setFixedWidth(175)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.returnPressed.connect(self.login)

        # giriş butonu
        self.button_login = QtWidgets.QPushButton("Giriş")
        self.button_login.clicked.connect(self.login)

        # kayıt butonu
        self.button_register = QtWidgets.QPushButton("Kayıt ol")
        self.button_register.clicked.connect(self.register)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        v_box_labels = QtWidgets.QVBoxLayout()
        v_box_labels.addWidget(self.label_text)
        v_box_labels.addWidget(self.label_text2)
        h_box.addLayout(v_box_labels)
        h_box.addStretch()

        h1_box = QtWidgets.QHBoxLayout()
        h1_box.addStretch()
        h1_box.addWidget(self.label_userName)
        # h1_box.addStretch()
        h1_box.addWidget(self.lineEdit_userName)
        h1_box.addStretch()

        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addStretch()
        h2_box.addWidget(self.label_password)
        # h2_box.addStretch()
        h2_box.addWidget(self.lineEdit_password)
        h2_box.addStretch()

        h3_box = QtWidgets.QHBoxLayout()
        h3_box.addStretch()
        h3_box.addWidget(self.button_register)
        h3_box.addWidget(self.button_login)
        h3_box.addStretch()


        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addLayout(h1_box)
        v_box.addStretch()
        v_box.addLayout(h2_box)
        v_box.addStretch()
        v_box.addLayout(h3_box)

        self.setLayout(v_box)

        self.setFixedHeight(400)
        self.setFixedWidth(672)
        self.setWindowTitle("SA")

    def login(self):

        db = DataBase()
        if db.UyeKontrol(self.lineEdit_userName.text(),self.lineEdit_password.text()):
            self.mainscreen = MainScreen()
            self.mainscreen.show()
            self.close()
        else:
            QtWidgets.QMessageBox.about(
                self, "Hata", "Kullanıcı adı ya da şifre yanlış tekrar deneyin")

    def register(self):

        self.registerscreen = RegisterScreen()
        self.registerscreen.show()
        self.close()