import sys
from main import session
from user_actions import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from models import User, Subject, Group

class MainApp(QWidget):
    def __init__(self, user):
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)
        self.setFixedSize(800, 600)


        mainV = MainView(user)
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
    def __init__(self, user):
        super().__init__()
        self.setWindowTitle('LeBszyUSOS')
        self.resize(800, 600)
        self.first_name = user.first_name
        self.last_name = user.last_name
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        label = {}
        label['User'] = QLabel(f'{self.first_name} {self.last_name}', parent=self)
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
            user = session.query(User).filter(User.login == email).first()
            self.mainApp = MainApp(user)
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
        s = Subject(name=subjectName)
        session.add(s)
        session.commit()

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
        users = show_teacher()
        
        for user in users:
            user_full = str(user[0]) + ". " + user[1] + " " + user[2]
            self.teacherId.addItem(user_full)
        
        self.subjectId = QComboBox()
        subjects = show_subjects()
        
        for subject in subjects:
            subject_full = str(subject[0]) + ". " + subject[1]
            self.subjectId.addItem(subject_full)
            
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
        
        teacher_id = int(teacherName.split(".")[0])
        subjects_id = int(subjectName.split(".")[0])
        print('\nClicked create new group ' + groupName + ' ' + teacherName + ' ' + subjectName)
        g= Group(group_name=groupName, teacher = teacher_id, subject_id = subjects_id)
        session.add(g)
        session.commit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    loginWindow = LoginWindow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')