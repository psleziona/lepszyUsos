from decimal import Clamped
from unicodedata import name
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Subject, Group
import user_actions

class Tests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        engine = create_engine('postgresql://pzgphpclbrjtqg:d7d021ff1705985a500f9ab45b40996fedee5a7f1b6bc051ff36a3fbd27d1d9c@ec2-54-228-125-183.eu-west-1.compute.amazonaws.com:5432/dcnfl455o5meun')
        Session = sessionmaker(bind=engine)
        cls.session = Session()
        cls.test_user1 = User(first_name='test', last_name='test', email='testowty@test.pl')
        cls.test_user2 = User(first_name='test2', last_name='test2', email='testowy2@tescik.pl')
        cls.subjects = cls.session.query(Subject).all()
        cls.group1 = Group(group_name='testowa')
        cls.group2 = Group(group_name='testowa2')
        cls.group1.subject_id = cls.subjects[1].subject_id
        cls.group1.users.append(cls.test_user1)
        cls.group1.users.append(cls.test_user2)
        cls.group2.users.append(cls.test_user2)
        cls.session.add_all([cls.test_user1, cls.test_user2, cls.group1, cls.group2])
        cls.session.commit()
    
    @classmethod
    def tearDownClass(cls):
        cls.session.query(User).filter(User.first_name == 'Alojz' and models.User.last_name == 'Kokot').delete()
        cls.session.query(Group).filter(Group.group_name == cls.group1.group_name).delete()
        cls.session.query(Group).filter(Group.group_name == cls.group2.group_name).delete()
        cls.session.query(User).filter(User.first_name == 'test').delete()
        cls.session.query(User).filter(User.first_name == 'test2').delete()
        cls.session.commit()

    def test_assign_teacher(cls):
        usr = cls.session.query(User).filter(User.login == cls.test_user1.login).first()
        grp = cls.session.query(Group).filter(Group.group_name == cls.group1.group_name).first()
        grp.assign_teacher(usr)
        cls.assertEqual(usr.user_id, grp.teacher)

    def test_add_user(cls):
        new_user = User(first_name = 'Alojz', last_name = 'Kokot', email='alko@gmail.com')
        cls.session.add(new_user)
        cls.session.commit()
        query = cls.session.query(User).filter(User.first_name == 'Alojz' and User.last_name == 'Kokot').first()
        cls.assertEqual(new_user.user_id, query.user_id)
    
    def test_login(cls):
        cls.assertTrue(user_actions.user_login(cls.test_user1.login, cls.test_user1.login))

    def test_show_where_student(cls):
        user = cls.session.query(User).filter(User.login == cls.test_user2.login).first()
        res = user_actions.show_user_class(user.user_id, where_student=True)
        cls.assertEqual(len(res), 2)

    def test_sign_to_class(cls):
        user = cls.session.query(User).filter(User.login == cls.test_user2.login).first()
        group = cls.session.query(Group).filter(Group.group_name == cls.group2.group_name).first()
        cls.assertTrue(user in group.users)


if __name__ == '__main__':
    unittest.main()
