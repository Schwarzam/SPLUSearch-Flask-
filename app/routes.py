from flask import render_template, request, session, flash, redirect, url_for
from app.forms import RegistrationForm, LoginForm
from app.models import User, ClassFactory, TableRef
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
import pandas as pd
from app.graph import Graph
from io import BytesIO
import matplotlib.pyplot as plt
import base64
import numpy as np
import astropy
from astropy.coordinates import SkyCoord
from astropy import units as u

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        login_user(user)
        return redirect(url_for('login'))
    return render_template("register.html", form=form, title="register")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Hello! {current_user.username}', 'info')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Failed. Please check email and password', 'danger')
    return render_template("login.html", form=form, title='login')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/searchby")
def choose():
    return render_template('choose.html')

@app.route("/coords", methods=['GET', 'POST'])
@login_required
def coords():
    flash('It takes around 8s for each object.', 'info')
    if request.method == "POST":
        ra = request.form.get("RA")
        dec = request.form.get("Dec")
        if ' ' or '  ' in ra:
            ra = ra.replace(' ', '')
        if ', ' in ra:
            ml = ra.split(', ')
        else:
            ml = ra.split(',')
        if ' ' or '  ' in dec:
            dec = dec.replace(' ', '')
        if ', ' in dec:
            ml2 = dec.split(', ')
        else:
            ml2 = dec.split(',')
        df1 = pd.DataFrame({'RA':ml})
        df2 = pd.DataFrame({'Dec':ml2})
        result = pd.concat([df2, df1], axis=1)
        df = pd.DataFrame(columns = ['ID','RA','Dec','PhotoFlag','FWHM','r_auto', 'image'])
        for index, row in result.iterrows():
            Galaxy = TableRef.query.filter()
            ra2 = np.array([])
            dec2 = np.array([])
            for x in Galaxy:
              ra2 = np.append(ra2, float(x.RA))
              dec2 = np.append(dec2, float(x.DEC))
            c = SkyCoord(ra=float(row.RA)*u.degree, dec=float(row.Dec)*u.degree)
            catalog = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
            idx, d2d, d3d = c.match_to_catalog_sky(catalog)
            Field = TableRef.query.filter_by(id = f'{idx+1}').first()
            Field = Field.NAME
            Field = ClassFactory(Field)
            Galaxy = Field.query.filter()
            ra2 = np.array([])
            dec2 = np.array([])
            for x in Galaxy:
                ra2 = np.append(ra2, float(x.RA))
                dec2 = np.append(dec2, float(x.Dec))
            c = SkyCoord(ra=float(row.RA)*u.degree, dec=float(row.Dec)*u.degree)
            catalog = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
            idx, d2d, d3d = c.match_to_catalog_sky(catalog)
            Galaxy = Galaxy[idx]
            image = f"http://legacysurvey.org/viewer/cutout.jpg?ra={Galaxy.RA}&dec={Galaxy.Dec}&layer=dr8&pixscale=0.50"
            data = {'ID':[Galaxy.ID],'RA':[Galaxy.RA],'Dec':[Galaxy.Dec],'PhotoFlag':[Galaxy.PhotoFlag],'FWHM':[Galaxy.FWHM],'r_auto':[Galaxy.r_auto], 'image':[image]}
            df1 = pd.DataFrame(data, columns=['ID','RA','Dec','PhotoFlag','FWHM','r_auto', 'image'])
            df = df.append(df1)
        return render_template('resultRA.html', id=df, auto = None)
    else:
        return render_template('RaDec.html')

@app.route("/galaxysearch", methods=['GET', 'POST'])
@login_required
def galaxy():
    if request.method == "POST":
        id = request.form.get("gal")
        if ' ' or '  ' in id:
            id = id.replace(' ', '')
        if ', ' in id:
            mylist = id.split(', ')
        else:
            mylist = id.split(',')
        df = pd.DataFrame(columns = ['ID','RA','Dec','PhotoFlag','FWHM','r_auto', 'image'])
        for x in mylist:
            FIELD = x.split(sep='.')
            FIELD = FIELD[1]
            if '-' in FIELD:
                FIELD = FIELD.replace('-','_')
            Galaxy = ClassFactory(FIELD).query.filter_by(ID = f'{x}').first_or_404()
            image = f"http://legacysurvey.org/viewer/cutout.jpg?ra={Galaxy.RA}&dec={Galaxy.Dec}&layer=dr8&pixscale=0.50"
            data = {'ID':[Galaxy.ID],'RA':[Galaxy.RA],'Dec':[Galaxy.Dec],'PhotoFlag':[Galaxy.PhotoFlag],'FWHM':[Galaxy.FWHM],'r_auto':[Galaxy.r_auto], 'image':[image]}
            df1 = pd.DataFrame(data, columns=['ID','RA','Dec','PhotoFlag','FWHM','r_auto', 'image'])
            df = df.append(df1)
        return render_template('result.html', id=df, auto = None)
    else:
        return render_template('galaxy.html', id=None)

@app.route("/galaxysearchSpectrum", methods=['GET', 'POST'])
@login_required
def galaxySpec():
    if request.method == "POST":
        id = request.form.get("gal")
        if ' ' or '  ' in id:
            id = id.replace(' ', '')
        if ', ' in id:
            mylist = id.split(', ')
        else:
            mylist = id.split(',')
        for x in mylist:
            FIELD = x.split(sep='.')
            FIELD = FIELD[1]
        if '-' in FIELD:
            FIELD = FIELD.replace('-','_')
        Galaxy = ClassFactory(FIELD).query.filter_by(ID = f'{x}').first_or_404()
        image = f"http://legacysurvey.org/viewer/cutout.jpg?ra={Galaxy.RA}&dec={Galaxy.Dec}&layer=dr8&pixscale=0.50"
        data = {'ID':[Galaxy.ID],'RA':[Galaxy.RA],'Dec':[Galaxy.Dec],'PhotoFlag':[Galaxy.PhotoFlag],'FWHM':[Galaxy.FWHM],'r_auto':[Galaxy.r_auto], 'image':[image]}
        plot = Graph(Galaxy)
        figfile = BytesIO()
        fig = plot.autoplot().savefig(figfile, format='png')
        figfile.seek(0)
        figdata_png = base64.b64encode(figfile.getvalue())
        result = str(figdata_png)[2:-1]
        petro = BytesIO()
        fig2 = plot.petroplot().savefig(petro, format='png')
        petro.seek(0)
        petro_png = base64.b64encode(petro.getvalue())
        result2 = str(petro_png)[2:-1]
        image = f"http://legacysurvey.org/viewer/cutout.jpg?ra={Galaxy.RA}&dec={Galaxy.Dec}&layer=dr8&pixscale=0.50"
        data = {'ID':[Galaxy.ID],'RA':[Galaxy.RA],'Dec':[Galaxy.Dec],'PhotoFlag':[Galaxy.PhotoFlag],'FWHM':[Galaxy.FWHM],'r_auto':[Galaxy.r_auto], 'image':[image]}
        df1 = pd.DataFrame(data, columns=['ID','RA','Dec','PhotoFlag','FWHM','r_auto', 'image'])
        return render_template('result.html', id=df1, auto = result, petro = result2)
    else:
        return render_template('galaxy.html', id=None)


@app.route("/coordsSpec", methods=['GET', 'POST'])
@login_required
def coordsSpec():
    flash('It takes around 8s for each object.', 'info')
    if request.method == "POST":
        ra = request.form.get("RA")
        dec = request.form.get("Dec")
        Galaxy = TableRef.query.filter()

        ra2 = np.array([])
        dec2 = np.array([])
        for x in Galaxy:
             ra2 = np.append(ra2, float(x.RA))
             dec2 = np.append(dec2, float(x.DEC))

        c = SkyCoord(ra=float(ra)*u.degree, dec=float(dec)*u.degree)
        catalog = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
        idx, d2d, d3d = c.match_to_catalog_sky(catalog)

        Field = TableRef.query.filter_by(id = f'{idx+1}').first()
        Field = Field.NAME
        Field = ClassFactory(Field)
        Galaxy = Field.query.filter()

        ra2 = np.array([])
        dec2 = np.array([])
        for x in Galaxy:
            ra2 = np.append(ra2, float(x.RA))
            dec2 = np.append(dec2, float(x.Dec))

        c = SkyCoord(ra=float(ra)*u.degree, dec=float(dec)*u.degree)
        catalog = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
        idx, d2d, d3d = c.match_to_catalog_sky(catalog)

        Galaxy = Galaxy[idx]


        image = f"http://legacysurvey.org/viewer/cutout.jpg?ra={Galaxy.RA}&dec={Galaxy.Dec}&layer=dr8&pixscale=0.50"
        data = {'ID':[Galaxy.ID],'RA':[Galaxy.RA],'Dec':[Galaxy.Dec],'PhotoFlag':[Galaxy.PhotoFlag],'FWHM':[Galaxy.FWHM],'r_auto':[Galaxy.r_auto], 'image':[image]}
        df1 = pd.DataFrame(data, columns=['ID','RA','Dec','PhotoFlag','FWHM','r_auto', 'image'])
        plot = Graph(Galaxy)
        figfile = BytesIO()
        fig = plot.autoplot().savefig(figfile, format='png')
        figfile.seek(0)
        figdata_png = base64.b64encode(figfile.getvalue())
        result = str(figdata_png)[2:-1]
        petro = BytesIO()
        fig2 = plot.petroplot().savefig(petro, format='png')
        petro.seek(0)
        petro_png = base64.b64encode(petro.getvalue())
        result2 = str(petro_png)[2:-1]
        return render_template('resultRA.html', id=df1, auto = result, petro = result2)
    else:
        return render_template('RaDec.html')
