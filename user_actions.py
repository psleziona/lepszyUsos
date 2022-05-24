from main import session
from models import User, Subject, Class_group

def show_class(user_id, where_teacher=False, where_student=False):
    query = session.query(User).filter(User.user_id == user_id).first()
    res = []
    if where_teacher:
        for c in query.groups:
            if c.is_teacher:
                res.append(c)
        return res
    if where_student:
        for c in query.groups:
            if not c.is_teacher:
                res.append(c)
        return res
    return query.groups
