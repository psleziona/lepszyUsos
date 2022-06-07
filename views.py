import sys
from user_actions import user_login
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)
        self.setFixedSize(800, 600)

        mainV = MainView()
        subjectCreate = createSubject()
        groupCreate = createGroup()

        label1 = QLabel("Widget in Tab 1.")
        label2 = QLabel("Widget in Tab 2.")

        tabWidget = QTabWidget()

        tabWidget.addTab(mainV, "Main")
        tabWidget.addTab(label1, "My classes")
        tabWidget.addTab(label2, "Assign to class")
        tabWidget.addTab(subjectCreate, "Create class")
        tabWidget.addTab(groupCreate, "Create group")

        layout.addWidget(tabWidget, 0, 0)

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LeBszyUSOS')
        self.resize(800, 600)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        label = {}
        label['User'] = QLabel('Jan Kowalski', parent=self)
        button_logout = QPushButton('&Log out', clicked=self.logout)
        layout.addWidget(button_logout)
        
    def logout(self):
        self.LoginWindow = LoginWindow()
        self.LoginWindow.show()
        self.close()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LeBszyUSOS login')
        self.setFixedSize(400, 200)

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Email'] = QLabel('Email')
        labels['Password'] = QLabel('Password')
        labels['Banner'] = QLabel('LeBszyUSOS')
        labels['Banner'].setStyleSheet('font-size: 25px;')
        labels['Email'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.lineEdits['Email'] = QLineEdit()
        self.lineEdits['Email'].setText = "Email"
        
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
        check = user_login(email, password)
        if check:
            #user = session.query(User).filter(User.login == login).first()
            self.mainApp = MainApp()
            self.mainApp.show()
            self.close()
        else:
            self.status.setText('invalid password or email')

class createSubject(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setFixedSize(400, 200)

        self.label = QLabel("Subject name:")
        self.textInput = QLineEdit()

        self.button = QPushButton("&Hit me", clicked=self.createSubject)

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.textInput, 0, 1)
        layout.addWidget(self.button, 1, 1)

        self.setLayout(layout)

    def createSubject(self):
        subjectName = self.textInput.text()
        print('\nClicked create new subject ' + subjectName)

class createGroup(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setFixedSize(400, 200)

        self.groupNameLabel = QLabel("Group name:")
        self.teacherName = QLabel("Teacher name:")
        self.subjectName = QLabel("Subject name:")
        self.groupName = QLineEdit()

        self.teacherId = QComboBox()

        self.teacherId.addItem("Jon")
        self.teacherId.addItem("Alex")
        self.teacherId.addItem("Jude")

        self.subjectId = QComboBox()

        self.subjectId.addItem("English")
        self.subjectId.addItem("Geometry")

        self.button = QPushButton("&Hit me", clicked=self.createSubject)

        layout.addWidget(self.groupNameLabel, 0, 0)
        layout.addWidget(self.groupName, 0, 1)

        layout.addWidget(self.teacherName, 1, 0)
        layout.addWidget(self.teacherId, 1, 1)

        layout.addWidget(self.subjectName, 2, 0)
        layout.addWidget(self.subjectId, 2, 1)

        layout.addWidget(self.button, 3, 1)

        self.setLayout(layout)

    def createSubject(self):
        groupName = self.groupName.text()
        teacherName = str(self.teacherId.currentText())
        subjectName = str(self.subjectId.currentText())
        print('\nClicked create new group ' + groupName + ' ' + teacherName + ' ' + subjectName)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    loginWindow = LoginWindow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')