from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash

#Se utilizó como base del programa el tutorial encontrado aquí https://pythonspot.com/login-authentication-with-flask/
#Se modificó para que la base de datos guardara la contraseñacon hash como medida de seguridad. El tutorial
#para hashear contraseñas se encuentra aquí https://dev.to/kaelscion/authentication-hashing-in-sqlalchemy-1bem


engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()

########################################################################
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hashed_password = Column(String)

#----------------------------------------------------------------------

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

# create tables
Base.metadata.create_all(engine)