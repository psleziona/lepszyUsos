from logging import NullHandler
from operator import concat
from select import select
from sqlalchemy import *
from main import session
from models import User, Subject, Group

def show_user_class(user_id, where_teacher=False, where_student=False):
    studs = session.query(User).filter(User.user_id == user_id).first()
    teach = session.query(Group).filter(Group.teacher == user_id).all()
    if where_teacher:
        return teach
    if where_student:
        return studs.groups
    return studs.extends(teach)

def show_teacher():
    return session.query(User.user_id, User.first_name, User.last_name).all()
    
def show_subjects():
    return session.query(Subject.subject_id, Subject.name).all()

def show_available_classes():
    return session.query(Group.group_id, Group.group_name, Subject.name, User.first_name, User.last_name).join(Subject, Subject.subject_id == Group.subject_id).join(User, Group.teacher == User.user_id).all() 

def user_login(login, password):
    user = session.query(User).filter(User.login == login).first()
    if user is not None:
        if user.confirm_password(password):
            return True
    return False

def sign_to_class(login, group_id):
    user = session.query(User).filter(User.login == login).first()
    group = session.query(Group).filter(Group.group_id == group_id).first()
    if user is not None and group is not None:
        if Group.teacher != user.user_id:
            group.users.append(user)
            session.commit()
            return True
    return False

def is_admin(user_id):
    admin = session.query(User).filter(User.user_id == user_id).first()
    if admin.is_admin == True:
        return True
    return False   


def show_groups_without_user(user_id):
    groups = session.query(Group).all()
    usr = session.query(User).filter(User.user_id == user_id).first()
    if usr is not None:
        return [group for group in groups if usr not in group.users]
    return groups
