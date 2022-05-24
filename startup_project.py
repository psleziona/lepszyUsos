from models import User, Subject
from main import session, Base, engine
import csv

subjects = ['Reading','Language arts',' Speech and Debate','English',
        'Basic Math','Algebra','Consumer Math','Geometry', 'Life Science',
        'Earth Science','Physical Science','Health','Social Studies','Geography']

def generate_users():
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for r in reader:
            u = User(first_name=r[0], last_name=r[1], email=r[2])
            session.add(u)
        session.commit()

def generate_subjects():
    for sub in subjects:
        s = Subject(name=sub)
        session.add(s)
    session.commit()

