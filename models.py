
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Podcasts(db.Model):
    __tablename__ = 'podcasts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country = db.Column(db.String(120))
    address = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    episodes = db.relationship('Episode', backref='podcast', lazy=True)
   
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
     return f'<Podcast {self.id} {self.name}>'


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    episodes = db.relationship('Episode', backref='artist', lazy=True)  
    
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
     return f'<Artist {self.id} {self.name}>' 


class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    release_time = db.Column(db.DateTime(), nullable=False)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcasts.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    
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

