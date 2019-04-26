
# Final Project

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import csv
import codecs
import sys
import random
import json

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Application configurations
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

# Database configurations
Base = declarative_base()
DBSession = scoped_session(sessionmaker())
engine = create_engine('sqlite:///movie_data.sqlite')
Base.metadata.bind = engine
DBSession.configure(bind=engine)

def initialion():
    Base.metadata.create_all(engine)
    return engine

collections = ('collections',Column('Type',String, ForeignKey('Type.id')),
                       Column('Director',String, ForeignKey('Director.id')),
                       Column('Rating',String, ForeignKey('Rating.id')))

# Database Columns Setting
class Type(Base):
    __tablename__ = "Type"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    Distributor = Column(String(250))
    Source = Column(String(250))
    movies = relationship('Movie',backref='Type')

class Director(Base):
    __tablename__ = "Director"
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    Release_Date = Column(String(250))
    movies = relationship('Movie', backref='Director')

class Rating(Base):
    __tablename__ = "Rating"
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    Director = Column(String(250))
    Source = Column(String(250))
    movies = relationship('Movie', backref='Rating')

class Movie(Base):
    __tablename__ = "Movie"
    id = Column(Integer, primary_key=True)
    Title = Column(String)# Only unique title can exist in this data model
    Type_id = Column(String, ForeignKey("Type.id")) #ok to be null for now
    Director_id = Column(String, ForeignKey("Director.id")) # ok to be null for now
    Rating_id = Column(String, ForeignKey("Rating.id"))

    def __repr__(self):
        return "{}  {}  {}  {}".format(self.Title, self.Type_id,
                                       self.Director_id,self.Rating_id)

# Movie Recommendation
class Movie_Recommend:
    def __init__(self, number):
          self.number = number

    def movie_randomselect():
        csv_file = open('movies_clean.csv')
        csv_reader_lines = csv.reader(csv_file)
        data = []
        data_result = []
        a = 0
        result = ''
        for one_line in csv_reader_lines:
            data.append(one_line)
            a = a + 1
        for b in range(1, 11):
            i = random.randint(0, 999)
            data_result.append(str(data[i][1]) + '  ' + str(data[i][11]) +
                               '  ' + str(data[i][13]) + '  ' + str(data[i][15]) + '</br>')
            result = result + str(data_result[b - 1])
        return result


# New Data Addition
def create_type(type_name):
        type_name = Type(name=type_name)
        DBSession.add(type_name)
        DBSession.commit()
        return type_name

def create_director(director_name):
        director_name = Director(name=director_name)
        DBSession.add(director_name)
        DBSession.commit()
        return director_name

def create_rating(rating):
        rating = Rating(name=rating)
        DBSession.add(rating)
        DBSession.commit()
        return rating

# Movie Type Selection
def type_select(typename):
    typename = Movie.query.filter_by(Type_id=typename).first()
    if typename:
        results = DBSession.query(Type_id=typename).all()
        for r in results:
            print(r)
    else:
        return 'Wrong Input. Please Enter a New Type.'


##### Set up Controllers (route functions) #####

# Main Route

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new/<titlename>/<typename>/<directorname>/<ratingname>/')
def add_new_movie(titlename,typename,directorname,ratingname):
    create_type(typename)
    create_director(directorname)
    create_rating(ratingname)
    movie_add = Movie(Title=titlename, Type_id=typename, Director_id=directorname,
                      Rating_id=ratingname)
    DBSession.add(movie_add)
    DBSession.commit()
    return "You successfully add a new movie: {} to database! The type is {}.The director is {}. " \
        "The rating is {}.".format(movie_add.Title, movie_add.Type_id,
                                   movie_add.Director_id, movie_add.Rating_id)
@app.route('/total_number')
def total():# Route function names can be anything unique
    with engine.connect() as con:  # connect to the database
        result = con.execute("select * from Movie")  # return result
        num = 0
        for lines in result:
            print(lines)
            num = num + 1
    return '<h1>{} movies recorded.<h1>'.format(num)

@app.route('/recommend')
def recommend_movie():
    a = Movie_Recommend.movie_randomselect()
    return a

@app.route('/youtube')
def youtube():
    with open('youtube-data.json') as f:
        response_json = f.read()
        data1 = json.loads(response_json)

    items_to_embed = []
    for item in data1['items']:
        if 'playlistId' in item['id']:
            item['url'] = 'http://www.youtube.com/embed/?listType=playlist&list={0}'.format(item['id']['playlistId'])
            items_to_embed.append(item)
        elif 'videoId' in item['id']:
            item['url'] = "http://www.youtube.com/embed/{0}".format(item['id']['videoId'])
            items_to_embed.append(item)

    return render_template('youtube.html', items_to_embed=items_to_embed, search_term="vox videos")

initialion()
with open("movies_clean.csv", "r", encoding='utf8') as F:
    df0 = csv.reader(F)
    data = list(df0)
for i in range(1, len(data)):
        new_movie = Movie(Title = data[i][1],Type_id = data[i][11],
                          Director_id = data[i][13],Rating_id = data[i][15])
        new_type = Type(name = data[i][11],Distributor= data[i][9],Source= data[i][10])
        new_director = Director(name= data[i][13],Release_Date=data[i][6])
        new_rating = Rating(name= data[i][15],Director=data[i][13],Source=data[i][10])

        DBSession.add(new_movie)
        DBSession.add(new_type)
        DBSession.add(new_director)
        DBSession.add(new_rating)
        DBSession.commit()
new_movie_test = Movie(Title='AAAAA', Type_id='BBBBB',
                      Director_id='CCCCC', Rating_id='DDDDD')
DBSession.add(new_movie_test)
DBSession.commit()
app.run()
