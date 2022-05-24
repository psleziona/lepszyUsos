import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QSizePolicy
from PyQt6.QtGui import QIcon

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        label = QLabel('Jan Kowalski', parent=self)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LepszyUSOS login')
        self.setWindowIcon(QIcon(''))
        self.setFixedSize(400, 200)

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Email'] = QLabel('Email')
        labels['Password'] = QLabel('Password')
        labels['Banner'] = QLabel('lepszyUSOS')
        labels['Banner'].setStyleSheet('font-size: 25px;')
        labels['Email'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.lineEdits['Email'] = QLineEdit()
        self.lineEdits['Password'] = QLineEdit()
        self.lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(labels['Banner'], 0, 0, 1, 3)

        layout.addWidget(labels['Email'], 1, 0, 1, 1)
        layout.addWidget(self.lineEdits['Email'], 1, 1, 1, 2)

        layout.addWidget(labels['Password'], 2, 0, 1, 1)
        layout.addWidget(self.lineEdits['Password'], 2, 1, 1, 2)

        button_login = QPushButton('&Log In', clicked=self.checkCredential)
        layout.addWidget(button_login, 3, 2, 1, 1)

        self.status = QLabel('')
        self.status.setStyleSheet('color: red;')
        layout.addWidget(self.status, 5, 0, 1, 3)

    def checkCredential(self):
        email = self.lineEdits['Email'].text()
        password = self.lineEdits['Password'].text()

        if email == "login" and password == "password":
            self.mainApp = MainApp()
            self.mainApp.show()
            self.close()
        else:
            self.status.setText('invalid password or email')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    loginWindow = LoginWindow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')