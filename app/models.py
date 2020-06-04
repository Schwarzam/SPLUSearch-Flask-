from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = "User"
            #
            #
            #
            #
            #
            #
          
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


def ClassFactory(name):
    tabledict={'__tablename__' : name,
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
    newclass = type(name, (db.Model,), tabledict)
    return newclass



class TableRef(db.Model):
    __tablename__ = 'Ref'
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
