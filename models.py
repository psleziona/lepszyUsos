from sqlalchemy import Column, Table, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import bcrypt
import random
import math

Base = declarative_base()

group_users = Table("group_users", Base.metadata, Column('user_id', ForeignKey('users.user_id')), Column('group_id', ForeignKey('group.group_id', ondelete='CASCADE')))

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    login = Column(String(15))
    password = Column(String(200))
    is_admin = Column(Boolean)

    groups = relationship('Group', secondary=group_users)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.login = self.first_name[:3] + self.last_name[:3] + str(math.floor(random.random() * 1000))
        self.create_password()


    def create_password(self):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(self.login.encode('utf8'), salt)
        self.password = self.password.decode('utf8')

    def confirm_password(self, password):
        return bcrypt.checkpw(password.encode('utf8'), self.password.encode('utf8'))

    def change_password(self, new_pass):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(new_pass.encode('utf8'), salt)
        self.password = self.password.decode('utf8')
        return True


class Subject(Base):
    __tablename__ = "subject"
    subject_id = Column(Integer, primary_key = True, autoincrement=True, nullable=False)
    name = Column(String(30), nullable=False)


class Group(Base):
    __tablename__ = 'group'
    group_id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    group_name = Column(String(50), nullable=False)
    teacher = Column(ForeignKey('users.user_id'))
    subject_id = Column(ForeignKey('subject.subject_id'))
    users = relationship('User', secondary=group_users)
    as_teacher = relationship('User', backref='as_teach', foreign_keys=[teacher])

    def assign_teacher(self, teacher):
        self.teacher = teacher.user_id


