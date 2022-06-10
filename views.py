from ast import Assign
from imp import reload
from pickle import NONE
from signal import signal
import sys
from types import NoneType
from matplotlib.ft2font import LOAD_VERTICAL_LAYOUT

from pip import main
from main import session
from user_actions import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from models import *



class MainApp(QWidget):
    def __init__(self, user):
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)
        self.setFixedSize(800, 600)
        self.id = user.user_id

        self.mainV = MainView(user)
        self.my_classes = showMyClass(user, self)
        self.assignment_view = assigneToClass(user, self)
        self.my_classes.connect()

        self.tabWidget = QTabWidget()

        self.tabWidget.addTab(self.mainV, "Main")
        self.tabWidget.addTab(self.my_classes, "My classes")
        self.tabWidget.addTab(self.assignment_view, "Assign to class")
           
             
        if is_admin(self.id):
            subjectCreate = createSubject()
            groupCreate = createGroup()
            userCreate = createUser()

            self.tabWidget.addTab(subjectCreate, "Create class")
            self.tabWidget.addTab(groupCreate, "Create group")
            self.tabWidget.addTab(userCreate, "Create user")
            
        layout.addWidget(self.tabWidget, 0, 0)
        
        
        
        

class MainView(QWidget):
    def __init__(self, user):
        super().__init__()
        self.setWindowTitle('LeBszyUSOS')
        self.resize(800, 600)
        self.name = user.first_name
        self.lname = user.last_name
        self.login = user.login
        
        hbox = {}
        hbox['Main ribon'] = QHBoxLayout()
        hbox['Change password'] = QGridLayout()
        vbox = QVBoxLayout()

        currentUser = QLabel(f'{self.name} {self.lname}', parent=self)
        button_logout = QPushButton('&Log out', clicked=self.logout)
        button_logout.setGeometry(5, 5, 5, 5)

        hbox['Main ribon'].addWidget(currentUser)
        hbox['Main ribon'].addWidget(button_logout)

        changePasswordLabel = QLabel("Change password:")
        currentPasswordLabel = QLabel("Current password:")
        newPasswordLabel1 = QLabel("new password:")
        newPasswordLabel2 = QLabel("repeat password:")

        self.currentPasswordInput = QLineEdit()
        self.currentPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.newPassword1Input = QLineEdit()
        self.newPassword1Input.setEchoMode(QLineEdit.EchoMode.Password)

        self.newPassword2Input = QLineEdit()
        self.newPassword2Input.setEchoMode(QLineEdit.EchoMode.Password)

        self.button = QPushButton("&Change password", clicked=self.changePassword)

        hbox['Change password'].addWidget(changePasswordLabel, 0, 0)
        hbox['Change password'].addWidget(currentPasswordLabel, 1, 0)
        hbox['Change password'].addWidget(newPasswordLabel1, 2, 0)
        hbox['Change password'].addWidget(newPasswordLabel2, 3, 0)

        hbox['Change password'].addWidget(self.currentPasswordInput, 1, 1)
        hbox['Change password'].addWidget(self.newPassword1Input, 2, 1)
        hbox['Change password'].addWidget(self.newPassword2Input, 3, 1)

        hbox['Change password'].addWidget(self.button, 4, 1)

        vbox.addLayout(hbox['Main ribon'])
        vbox.addLayout((hbox['Change password']))

        vbox.addWidget(currentUser)

        self.setLayout(vbox)
        
    def logout(self):
        self.mainApp.setParrent(NONE)
        self.login = LoginWindow()
        self.login.show()
        self.close()

    def changePassword(self):
        current_password = self.currentPasswordInput.text()
        new_password = self.newPassword1Input.text()
        new_password2 = self.newPassword2Input.text()
        if new_password == new_password2:
            check = user_login(self.login, current_password)
            if check:
                User.change_password(self, new_password)

class createUser(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        self.labels = {}
        self.input = {}

        self.labels['first name'] = QLabel("First name:")
        self.labels['last name'] = QLabel("Last name:")
        self.labels['Email'] = QLabel("email:")
        self.labels['Admin'] = QLabel("admin:")
        self.labels['Info'] = QLabel("")

        layout.addWidget(self.labels['first name'], 0, 0)
        layout.addWidget(self.labels['last name'], 1, 0)
        layout.addWidget(self.labels['Email'], 2, 0)
        layout.addWidget(self.labels['Admin'], 3, 0)
        layout.addWidget(self.labels['Info'], 5, 1)

        self.input['first name'] = QLineEdit()
        self.input['last name'] = QLineEdit()
        self.input['Email'] = QLineEdit()
        self.input['Admin'] = QCheckBox()

        layout.addWidget(self.input['first name'], 0, 1)
        layout.addWidget(self.input['last name'], 1, 1)
        layout.addWidget(self.input['Email'], 2, 1)
        layout.addWidget(self.input['Admin'], 3, 1)

        self.button = QPushButton("&Add user", clicked=self.createUser)

        layout.addWidget(self.button, 4, 1)

        self.setLayout(layout)

    def createUser(self):
        firstName = str(self.input['first name'].text())
        lastName = str(self.input['last name'].text())
        Email = str(self.input['Email'].text())

        Admin = self.input['Admin'].isChecked()
        new_user = User(first_name = firstName, last_name = lastName, email = Email, is_admin = Admin)
        session.add(new_user)
        session.commit()
        self.labels['Info'].setText(f"User has been created. The login is {new_user.login}")
    
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
        check = user_login('testes521', 'testes521')
        if check:
            user = session.query(User).filter(User.login == 'testes521').first()
            self.mainApp = MainApp(user)
            self.mainApp.show()
            self.close()
        else:
            self.status.setText('invalid password or email')

class showMyClass(QWidget):
    r = pyqtSignal()
    
    def __init__(self, user, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()
        self.button = QPushButton("&unasigned", clicked = self.unasigne)
        
        self.user = user
        
        self.list = QListWidget()

        self.load_window()
    
        layout.addWidget(self.button)
        layout.addWidget(self.list)
        self.setLayout(layout)
        
    def unasigne(self):
        i = self.list.currentIndex().row()
        self.user_classes[i].users = [usr for usr in self.user_classes[i].users if usr.user_id != self.user.user_id]
        session.commit()
        self.load_window()
        self.r.emit()

    def load_window(self):
        self.user_classes = show_user_class(self.user.user_id)
        self.list.clear()
        for i,c in enumerate(self.user_classes):
            self.list.insertItem(i, c.group_name)
        self.list.setCurrentRow(0)
        
    def connect(self):
        self.r.connect(self.main_window.assignment_view.load_class)

class assigneToClass(QWidget):
    r = pyqtSignal()
    
    def __init__(self, user, main_window):
        super().__init__()
        self.main_window = main_window
        self.r.connect(self.main_window.my_classes.load_window)
        self.layout = QVBoxLayout()

        self.button = QPushButton("&asigne", clicked = self.asigne)

        self.list = QListWidget()
        self.list.setCurrentRow(0)
        self.id = user.login
        self.user_id = user.user_id

        self.load_class()
                     
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.list)
        self.setLayout(self.layout)

    def asigne(self):
        value = self.list.currentItem()
        value = value.text()
        value = value[4:]
        value = int(value.split("|")[0])
        sign_to_class(self.id, value)
        self.load_class()
        self.r.emit()
        
    def load_class(self):
        self.list.clear()
        assign_class = show_groups_without_user(self.user_id)
        
        if assign_class is not None:
            for i, group in enumerate(assign_class):
                try:
                    full_name = f'Id: {group.group_id} | Group name: {group.group_name} | Subject: {group.subject_name.name} | Teacher: {group.as_teacher.first_name} {group.as_teacher.last_name}'
                    self.list.insertItem(i, full_name)     
                except AttributeError:
                    continue
        
            

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