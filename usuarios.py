import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tableDef import *

engine = create_engine('sqlite:///tutorial.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User(username = "Diego")
user.set_password("Sowel")
session.add(user)

user = User(username = "Cristopher")
user.set_password("elLider")
session.add(user)

user = User(username = "Pietro")
user.set_password("switch")
session.add(user)

# commit the record the database
session.commit()

session.commit()