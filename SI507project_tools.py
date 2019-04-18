
import random
import pandas as pd
import numpy as np

from flask import Flask,render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_movies.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # For database use
session = db.session

###random select movies

class Movie_Recommend:
    def __init__(self, number):
          self.number = number

    def movie_randomselect(num):
        import csv
        csv_file = open('movies_clean.csv')
        csv_reader_lines = csv.reader(csv_file)
        data = []
        data_result = []
        a = 0
        result = ''
        for one_line in csv_reader_lines:
            data.append(one_line)
            a = a + 1
        for a in range(1, num):
            i = random.randint(0, 3145)
            data_result.append(str(data[i][1]) + '  ' + str(data[i][11]) +
                               '  ' + str(data[i][13]) + '  ' + str(data[i][15]) + '</br>')
            result = result + str(data_result[a - 1])
        return result


    def movie_total_number():
        data_x = pd.read_csv('movies_clean.csv')
        train_data = np.array(data_x)
        train_x_list = train_data.tolist()
        return len(train_x_list)

collections = db.Table('collections',db.Column('Type_id',db.String, db.ForeignKey('Type.id')),
                       db.Column('Director_id',db.String, db.ForeignKey('Director.id')),
                       db.Column('Rating_id',db.String, db.ForeignKey('Rating.id')))

class Type(db.Model):
    __tablename__ = "Type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    types = db.relationship('Type',secondary=collections,backref=db.backref('Type',lazy='dynamic'),lazy='dynamic')
    movies = db.relationship('Movie',backref='Type')

class Director(db.Model):
    __tablename__ = "Director"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Director')

class Rating(db.Model):
    __tablename__ = "Rating"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Rating')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64),unique=True) # Only unique title can exist in this data model
    Type_id = db.Column(db.String, db.ForeignKey("Type.id")) #ok to be null for now
    Director_id = db.Column(db.String, db.ForeignKey("Director.id")) # ok to be null for now
    Rating_id = db.Column(db.String, db.ForeignKey("Rating.id"))

    def __repr__(self):
        return "{}  {}  {}  {}".format(self.title, self.Type_id, self.Director_id,self.Rating_id)

###database addition

def create_type(type_name):
    type_name = Type.query.filter_by(name=type_name).first()
    if type_name:
        return type_name
    else:
        type_name = Type(name=type_name)
        session.add(type_name)
        session.commit()
        return type_name

def create_director(director_name):
    director_name = Director.query.filter_by(name=director_name).first()
    if director_name:
        return director_name
    else:
        director_name = Director(name=director_name)
        session.add(director_name)
        session.commit()
        return director_name

def create_rating(rating):
    rating = Rating.query.filter_by(name=rating).first()
    if rating:
        return rating
    else:
        director_name = Rating(name=rating)
        session.add(rating)
        session.commit()
        return rating

if __name__ == '__main__':
    db.create_all()


