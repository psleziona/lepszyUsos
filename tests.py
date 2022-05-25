from unicodedata import name
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
import user_actions

class Tests(unittest.TestCase):

    def setUp(self):
        engine = create_engine('postgresql://rfvxuilezcmske:09baec9e130d4ea6e9385adf72b4f732972d9b4453aecd5aa6c97294561a9d8a@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/daa5pddldgnckt')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.test_user1 = models.User(first_name='test', last_name='test', email='testowty@test.pl')
        self.test_user2 = models.User(first_name='test2', last_name='test2', email='testowy2@tescik.pl')
        self.subjects = self.session.query(models.Subject).all()
        self.group1 = models.Class_group(group_name='testowa')
        self.group1.subject_id = self.subjects[1].subject_id
        self.group1.users.append(self.test_user1)
        self.group1.users.append(self.test_user2)
        self.group1.users[0].is_teacher = True

    def tearDown(self):
        self.session.query(models.User).filter(models.User.first_name == 'Alojz' and models.User.last_name == 'Kokot').delete()
        self.session.commit()

    def test_add_user(self):
        new_user = models.User(first_name = 'Alojz', last_name = 'Kokot', email='alko@gmail.com')
        self.session.add(new_user)
        self.session.commit()
        query = self.session.query(models.User).filter(models.User.first_name == 'Alojz' and models.User.last_name == 'Kokot').first()
        self.assertEqual(new_user.user_id, query.user_id)
    

    def test_login(self):
        self.assertTrue(self.test_user1.confirm_password(self.test_user1.login))

if __name__ == '__main__':
    unittest.main()
