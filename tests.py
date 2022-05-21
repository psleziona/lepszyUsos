from unicodedata import name
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

class Tests(unittest.TestCase):

    def setUp(self):
        engine = create_engine('postgresql://rfvxuilezcmske:09baec9e130d4ea6e9385adf72b4f732972d9b4453aecd5aa6c97294561a9d8a@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/daa5pddldgnckt')
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