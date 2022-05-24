from sqlalchemy import Column, Table, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import bcrypt

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    login = Column(String(15))
    password = Column(String(200))
    is_admin = Column(Boolean)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.login = self.first_name[:2] + self.last_name[:2] + str(self.user_id)
        self.create_password()
        
    def create_password(self):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(self.login.encode('utf8'), salt)

    def confirm_password(self, password):
        return bcrypt.checkpw(password.encode('utf8'), self.password)

    def change_password(self, new_pass):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(new_pass, salt)
        return True

    groups = relationship('Class_group', backref='users')

class Subject(Base):
    __tablename__ = "subject"
    subject_id = Column(Integer, primary_key = True, autoincrement=True, nullable=False)
    name = Column(String(30), nullable=False)

    groups = relationship('Class_group')


class Class_group(Base):
    __tablename__ = 'class_group'
    class_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    is_teacher = Column(Boolean, nullable=False)
    group_name = Column(String(40), nullable=False)
    subject = Column(ForeignKey('subject.subject_id'), nullable=False)
    group_user = Column(ForeignKey('users.user_id'), nullable=False)
