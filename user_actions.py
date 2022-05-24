from main import session
from models import User, Subject, Class_group

def get_group_listeners(id):
    query = session.query(Class_group).filter(Class_group.class_id == id).all()[0]
    return query.users
