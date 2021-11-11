from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW!
class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets" # create new table names pets

    @classmethod
    def get_by_species(cls, species):
        cls.query.filter_by(species=species).all()

    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger > 20).all()


    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>" 

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True) # SERIAL

    name = db.Column(db.String(50),
                     nullable=False, # NOT NULL
                     unique=True) # UNIQUE

    species = db.Column(db.String(30), nullable=True) #VARCHAE(30)

    hunger = db.Column(db.Integer, nullable=False, default=20)

    # put this after define table
    def greet(self):
        return f"Hi, I am {self.name} the {self.species}"

    def feed(self, amt = 20):
        """Update hunger based off of amount"""
        self.hunger -= amt 
        self.hunger = max(self.hunger,0)
