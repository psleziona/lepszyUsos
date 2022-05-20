from unicodedata import name
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

class Tests(unittest.TestCase):

    def setUp(self):
        engine = create_engine('mariadb://lepszyUSOS:a9d8x37WQrhdgSlH@192.168.192.42:3306/lepszyUSOS')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(models.User).filter(models.User.first_name == 'Alojz' and models.User.last_name == 'Kokot').delete()
        self.session.commit()

    def test_add_user(self):
        new_user = models.User(first_name = 'Alojz', last_name = 'Kokot')
        self.session.add(new_user)
        self.session.commit()
        query = self.session.query(models.User).filter(models.User.first_name == 'Alojz' and models.User.last_name == 'Kokot').all()
        self.assertEqual(new_user.user_id, query[0].user_id)


if __name__ == '__main__':
    unittest.main()