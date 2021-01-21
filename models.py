import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json


database_path = os.environ['database_url']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.create_all()



'''
Actor

'''

class Actors(db.Model):
    id = db.Column(Integer() , primary_key=True)
    name = db.Column(String)
    age = db.Column(Integer())
    gender = db.Column(String)
    actorMovie = db.relationship('ActorMoviesMap' , backref='Actors' , lazy=True)



    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Movies(db.Model):
    id = db.Column(Integer(), primary_key=True)
    title = db.Column(String)
    relaseDate = db.Column(db.DateTime())
    movieActor = db.relationship('ActorMoviesMap' , backref='Movies' , lazy=True)


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class ActorMoviesMap(db.Model):
    id = db.Column(Integer(), primary_key=True)
    Actor_id = db.Column(db.Integer , db.ForeignKey(Actors.id) , nullable=False)
    Movie_id = db.Column(db.Integer , db.ForeignKey(Movies.id) , nullable=False)


    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()




