from flask import Flask, request, render_template, redirect, session, flash
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Department, Employee, get_directory


app = Flask(__name__)

# this below code should be before db.sth
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = "Chickenzarecool5485754"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/phones')
def list_phones():
    emps = Employee.query.all()
    return render_template('phones.html', emps=emps)