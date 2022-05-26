from main import session
from models import User, Subject, Group

def show_user_class(user_id, where_teacher=False, where_student=False):
    studs = session.query(User).filter(User.user_id == user_id).first()
    teach = session.query(Group).filter(Group.teacher == user_id).all()
    if where_teacher:
        return teach
    if where_student:
        return studs.groups
    return studes.extends(teach)

def show_available_classes():
    return session.query(Class_group).all()

def user_login(login, password):
    user = session.query(User).filter(User.login == login).first()
    if user is not None:
        if user.confirm_password(password):
            return True
    return False


def sign_to_class(login, class_id):
    user = session.query(User).filter(User.login == login).first()
    group = session.query(Class_group).filter(Class_group.class_id == class_id).first()
    if user is not None and group is not None:
        group.users.append(user)
        session.commit()
        return True
    return False



