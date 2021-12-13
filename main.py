import sys

from PyQt5.QtWidgets import QApplication

from loginScreen import LoginScreen

def main():
    app = QApplication(sys.argv)
    loginscreen = LoginScreen()
    loginscreen.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
