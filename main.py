from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from models import Base

engine = create_engine('mariadb://lepszyUSOS:a9d8x37WQrhdgSlH@192.168.192.42:3306/lepszyUSOS')

Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()