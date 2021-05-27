
from flask import json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Podcast(db.Model):
    __tablename__ = 'podcasts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120))
    country = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    genre = db.Column(db.String(120))
    episodes = db.relationship('Episode', backref='podcast', lazy=True)

    def __init__(self, name, city, country, image_link, genre):
        self.name = name
        self.city = city
        self.country = country
        self.image_link = image_link
        self.genre = genre
   
    #adds new entry
    def add(self):
        db.session.add(self)
        db.session.commit()   
    #updates db
    def update(self):
        db.session.commit()
    #deletes entry from db
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    #jsonifies object
    def podcast_json(self):
            return {
                'id': self.id,
                'name': self.name,
                'city': self.city,
                'country': self.country,
                'image_link': self.image_link,
                'genre': self.genre,
            }

    def __repr__(self):
     return f'<Podcast {self.id} {self.name}>'

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    episodes = db.relationship('Episode', backref='artist', lazy=True)  

    def __init__(self, name, city, country, image_link, genre):
        self.name = name
        self.city = city
        self.country = country
        self.image_link = image_link
    
    #adds new entry
    def add(self):
        db.session.add(self)
        db.session.commit()   
    #updates db
    def update(self):
        db.session.commit()
    #deletes entry from db
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    #jsonifies object
    def artist_json(self):
            return {
                'id': self.id,
                'name': self.name,
                'city': self.city,
                'country': self.country,
                'image_link': self.image_link
            }

    def __repr__(self):
     return f'<Artist {self.id} {self.name}>' 


class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    release_time = db.Column(db.DateTime(), nullable=False)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcasts.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

    def __init__(self, name, release_time, podcast_id, artist_id):
        self.name = name
        self.release_time = release_time
        self.podcast_id = podcast_id
        self.artist_id = artist_id  
    
    #adds new entry
    def add(self):
        db.session.add(self)
        db.session.commit()   
    #updates db
    def update(self):
        db.session.commit()
    #deletes entry from db
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
      
    def __repr__(self):
     return f'<Episode {self.id} {self.name}>'

