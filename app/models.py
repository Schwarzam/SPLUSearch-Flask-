from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


def ClassFactory(name):
    tabledict={'__tablename__' : name,
      '__table_args__' : {'extend_existing': True},
      'ID' : db.Column(db.String, primary_key=True),
      'RA' : db.Column(db.String, nullable=False),
      'Dec' : db.Column(db.String, nullable=False),
      'X' : db.Column(db.String, nullable=False),
      'Y' : db.Column(db.String, nullable=False),
      'ISOarea' : db.Column(db.String, nullable=False),
      's2nDet' : db.Column(db.String, nullable=False),
      'PhotoFlag' : db.Column(db.String, nullable=False),
      'FWHM' : db.Column(db.String, nullable=False),
      'FWHM_n' : db.Column(db.String, nullable=False),
      'MUMAX' : db.Column(db.String, nullable=False),
      'A' : db.Column(db.String, nullable=False),
      'B' : db.Column(db.String, nullable=False),
      'THETA' : db.Column(db.String, nullable=False),
      'FlRadDet' : db.Column(db.String, nullable=False),
      'KrRadDet' : db.Column(db.String, nullable=False),
      'nDet_auto' : db.Column(db.String, nullable=False),
      'nDet_petro' : db.Column(db.String, nullable=False),
      'nDet_aper' : db.Column(db.String, nullable=False),
      'uJAVA_auto' : db.Column(db.String, nullable=False),
      'euJAVA_auto' : db.Column(db.String, nullable=False),
      's2n_uJAVA_auto' : db.Column(db.String, nullable=False),
      'uJAVA_petro' : db.Column(db.String, nullable=False),
      'euJAVA_petro' : db.Column(db.String, nullable=False),
      's2n_uJAVA_petro' : db.Column(db.String, nullable=False),
      'uJAVA_aper' : db.Column(db.String, nullable=False),
      'euJAVA_aper' : db.Column(db.String, nullable=False),
      's2n_uJAVA_aper' : db.Column(db.String, nullable=False),
      'F378_auto' : db.Column(db.String, nullable=False),
      'eF378_auto' : db.Column(db.String, nullable=False),
      's2n_F378_auto' : db.Column(db.String, nullable=False),
      'F378_petro' : db.Column(db.String, nullable=False),
      'eF378_petro' : db.Column(db.String, nullable=False),
      's2n_F378_petro' : db.Column(db.String, nullable=False),
      'F378_aper' : db.Column(db.String, nullable=False),
      'eF378_aper' : db.Column(db.String, nullable=False),
      's2n_F378_aper' : db.Column(db.String, nullable=False),
      'F395_auto' : db.Column(db.String, nullable=False),
      'eF395_auto' : db.Column(db.String, nullable=False),
      's2n_F395_auto' : db.Column(db.String, nullable=False),
      'F395_petro' : db.Column(db.String, nullable=False),
      'eF395_petro' : db.Column(db.String, nullable=False),
      's2n_F395_petro' : db.Column(db.String, nullable=False),
      'F395_aper' : db.Column(db.String, nullable=False),
      'eF395_aper' : db.Column(db.String, nullable=False),
      's2n_F395_aper' : db.Column(db.String, nullable=False),
      'F410_auto' : db.Column(db.String, nullable=False),
      'eF410_auto' : db.Column(db.String, nullable=False),
      's2n_F410_auto' : db.Column(db.String, nullable=False),
      'F410_petro' : db.Column(db.String, nullable=False),
      'eF410_petro' : db.Column(db.String, nullable=False),
      's2n_F410_petro' : db.Column(db.String, nullable=False),
      'F410_aper' : db.Column(db.String, nullable=False),
      'eF410_aper' : db.Column(db.String, nullable=False),
      's2n_F410_aper' : db.Column(db.String, nullable=False),
      'F430_auto' : db.Column(db.String, nullable=False),
      'eF430_auto' : db.Column(db.String, nullable=False),
      's2n_F430_auto' : db.Column(db.String, nullable=False),
      'F430_petro' : db.Column(db.String, nullable=False),
      'eF430_petro' : db.Column(db.String, nullable=False),
      's2n_F430_petro' : db.Column(db.String, nullable=False),
      'F430_aper' : db.Column(db.String, nullable=False),
      'eF430_aper' : db.Column(db.String, nullable=False),
      's2n_F430_aper' : db.Column(db.String, nullable=False),
      'g_auto' : db.Column(db.String, nullable=False),
      'eg_auto' : db.Column(db.String, nullable=False),
      's2n_g_auto' : db.Column(db.String, nullable=False),
      'g_petro' : db.Column(db.String, nullable=False),
      'eg_petro' : db.Column(db.String, nullable=False),
      's2n_g_petro' : db.Column(db.String, nullable=False),
      'g_aper' : db.Column(db.String, nullable=False),
      'eg_aper' : db.Column(db.String, nullable=False),
      's2n_g_aper' : db.Column(db.String, nullable=False),
      'F515_auto' : db.Column(db.String, nullable=False),
      'eF515_auto' : db.Column(db.String, nullable=False),
      's2n_F515_auto' : db.Column(db.String, nullable=False),
      'F515_petro' : db.Column(db.String, nullable=False),
      'eF515_petro' : db.Column(db.String, nullable=False),
      's2n_F515_petro' : db.Column(db.String, nullable=False),
      'F515_aper' : db.Column(db.String, nullable=False),
      'eF515_aper' : db.Column(db.String, nullable=False),
      's2n_F515_aper' : db.Column(db.String, nullable=False),
      'r_auto' : db.Column(db.String, nullable=False),
      'er_auto' : db.Column(db.String, nullable=False),
      's2n_r_auto' : db.Column(db.String, nullable=False),
      'r_petro' : db.Column(db.String, nullable=False),
      'er_petro' : db.Column(db.String, nullable=False),
      's2n_r_petro' : db.Column(db.String, nullable=False),
      'r_aper' : db.Column(db.String, nullable=False),
      'er_aper' : db.Column(db.String, nullable=False),
      's2n_r_aper' : db.Column(db.String, nullable=False),
      'F660_auto' : db.Column(db.String, nullable=False),
      'eF660_auto' : db.Column(db.String, nullable=False),
      's2n_F660_auto' : db.Column(db.String, nullable=False),
      'F660_petro' : db.Column(db.String, nullable=False),
      'eF660_petro' : db.Column(db.String, nullable=False),
      's2n_F660_petro' : db.Column(db.String, nullable=False),
      'F660_aper' : db.Column(db.String, nullable=False),
      'eF660_aper' : db.Column(db.String, nullable=False),
      's2n_F660_aper' : db.Column(db.String, nullable=False),
      'i_auto' : db.Column(db.String, nullable=False),
      'ei_auto' : db.Column(db.String, nullable=False),
      's2n_i_auto' : db.Column(db.String, nullable=False),
      'i_petro' : db.Column(db.String, nullable=False),
      'ei_petro' : db.Column(db.String, nullable=False),
      's2n_i_petro' : db.Column(db.String, nullable=False),
      'i_aper' : db.Column(db.String, nullable=False),
      'ei_aper' : db.Column(db.String, nullable=False),
      's2n_i_aper' : db.Column(db.String, nullable=False),
      'F861_auto' : db.Column(db.String, nullable=False),
      'eF861_auto' : db.Column(db.String, nullable=False),
      's2n_F861_auto' : db.Column(db.String, nullable=False),
      'F861_petro' : db.Column(db.String, nullable=False),
      'eF861_petro' : db.Column(db.String, nullable=False),
      's2n_F861_petro' : db.Column(db.String, nullable=False),
      'F861_aper' : db.Column(db.String, nullable=False),
      'eF861_aper' : db.Column(db.String, nullable=False),
      's2n_F861_aper' : db.Column(db.String, nullable=False),
      'z_auto' : db.Column(db.String, nullable=False),
      'ez_auto' : db.Column(db.String, nullable=False),
      's2n_z_auto' : db.Column(db.String, nullable=False),
      'z_petro' : db.Column(db.String, nullable=False),
      'ez_petro' : db.Column(db.String, nullable=False),
      's2n_z_petro' : db.Column(db.String, nullable=False),
      'z_aper' : db.Column(db.String, nullable=False),
      'ez_aper' : db.Column(db.String, nullable=False),
      's2n_z_aper' : db.Column(db.String, nullable=False),}
    newclass = type(name, (db.Model,), tabledict)
    return newclass



class TableRef(db.Model):
    __tablename__ = 'Ref'
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    PID = db.Column(db.String, nullable=False)
    NAME = db.Column(db.String, nullable=False)
    RA = db.Column(db.String, nullable=False)
    DEC = db.Column(db.String, nullable=False)
    EPOC = db.Column(db.String, nullable=False)
    STATUS = db.Column(db.String, nullable=False)
