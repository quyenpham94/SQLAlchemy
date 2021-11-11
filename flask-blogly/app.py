"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User
# add debug toolbar here 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()
 

@app.route('/')
def home_page():
    """Home page redirects to list of users."""

    return redirect('/')

@app.route('/users')
def info_users():
    """Page shows all information of all users."""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods=["GET"])
def users_new_form():
    """Show a form to create a new user"""

    return render_template('users/new.html')

@app.route('/users/new', methods=["POST"])
def users_new():
    """Handle form submission for creating new user."""

    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)
    
    db.session.add(new_user)
    db.session.commit()
    
    return redirect("/users")
