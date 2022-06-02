from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Subject, Group, group_users
import csv

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

engine = create_engine('postgresql://pzgphpclbrjtqg:d7d021ff1705985a500f9ab45b40996fedee5a7f1b6bc051ff36a3fbd27d1d9c@ec2-54-228-125-183.eu-west-1.compute.amazonaws.com:5432/dcnfl455o5meun', echo=True, future=True)

Session = sessionmaker(bind=engine)
session = Session()

subjects = ['Reading','Language arts',' Speech and Debate','English',
        'Basic Math','Algebra','Consumer Math','Geometry', 'Life Science',
        'Earth Science','Physical Science','Health','Social Studies','Geography']

if __name__ == '__main__':
    print('''##########ADMIN PANEL##########
        1 - usuń bazę
        2 - stwórz baze
        3 - generuj użytkowników
        4 - generuje przedmioty
        0 - wyjdź''')
    while(True):
        option = int(input())
        if option == 1:
            Base.metadata.drop_all(engine)
        elif option == 2:
            Base.metadata.create_all(engine)
        elif option == 3:
            generate_users()
        elif option == 4:
            generate_subjects()
        elif option == 0:
            break
        print('Oczekiwanie na akcje')

