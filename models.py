from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(50))
    password = Column(String(30))
    title = Column(String(30))
    phone = Column(String(12))
    activity = Column(Boolean)

    classes = relationship('User_class', backref='user')

class Class(Base):
    __tablename__ = "class"
    class_id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String(30))
    descritpion = Column(String(300))
    schedule_date = Column(DateTime)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    users = relationship('User_class', backref='sign_class')

class User_role(Base):
    __tablename__ = "user_role"
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(30))
    

class User_class(Base):
    __tablename__ = 'user_class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id')) 
    class_id =Column(Integer, ForeignKey('class.class_id')) 
    role_id = Column(Integer, ForeignKey('user_role.role_id'))

    roles = relationship('User_role', backref='classes')
