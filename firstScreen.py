
from PyQt5 import QtWidgets

from loginScreen import LoginScreen

from registerScreen import RegisterScreen


class FirstScreen(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        # giriş yazısı
        self.label_maintext = QtWidgets.QLabel("HG KARŞİM")

        # giriş butonu
        self.button_login = QtWidgets.QPushButton("Giriş yap")

        self.button_login.clicked.connect(self.login)

        # kayıt butonu
        self.button_register = QtWidgets.QPushButton("Kayıt ol")

        self.button_register.clicked.connect(self.register)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.button_login)
        h_box.addStretch()
        h_box.addWidget(self.button_register)
        h_box.addStretch()

        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addStretch()
        h2_box.addWidget(self.label_maintext)
        h2_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h2_box)
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.setLayout(v_box)

        self.setFixedHeight(400)
        self.setFixedWidth(672)
        

    def login(self):

        self.loginscreen = LoginScreen()
        self.loginscreen.show()
        self.close()

    def register(self):

        self.registerscreen = RegisterScreen()
        self.registerscreen.show()
        self.close()
