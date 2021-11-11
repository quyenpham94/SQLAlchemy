"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.kenyons.com/wp-content/uploads/2017/04/default-image-620x600.jpg"

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
                
    first_name = db.Column(db.Text,
                           nullable=False)

    last_name = db.Column(db.Text,
                           nullable=False)

    image_url = db.Column(db.Text,
                          nullable=False,
                          default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


