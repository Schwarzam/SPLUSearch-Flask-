import os
from flask import Flask
from flask_session.__init__ import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

db = SQLAlchemy(app)

#
#
#
#
#

from app import routes
