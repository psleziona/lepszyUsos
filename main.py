from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from models import Base

engine = create_engine('postgres://rfvxuilezcmske:09baec9e130d4ea6e9385adf72b4f732972d9b4453aecd5aa6c97294561a9d8a@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/daa5pddldgnckt')

Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()