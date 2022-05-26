from main import session
from models import User, Subject, Class_group

def assing_person_to_group(user_id, group_id):
    class_query = session.query(Class_group).filter(Class_group.class_id == group_id).first()
    user_query = session.query(User).filter(User.user_id == user_id).first()
    class_query.users.append(user_query)
    session.commit()

def show_all_groups():
    return session.query(Class_group).all()
