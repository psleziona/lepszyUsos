from turtle import title
from MySQLdb import DateFromTicks
from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


user_class_assign = Table('user_class', Base.metadata,
    Column('user_id', ForeignKey('users.user_id')),
    Column('class_id', ForeignKey('classes.class_id'))
)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(50))
    password = Column(String(30))
    title = Column(String(30))
    phone = Column(String(12))
    activity = Column(String(20))

class Class(Base):
    __tablename__ = "classes"
    class_id = Column(Integer, primary_key = True)
    name = Column(String(30))
    descritpion = Column(String(300))
    schedule_date = Column(DateTime)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    