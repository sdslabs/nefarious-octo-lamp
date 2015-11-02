__author__ = 'gautham'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, func, UniqueConstraint
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    language = Column(String(50))
    info = Column(String(1000))

    __table_args__ = (UniqueConstraint('name','id'),)


class Year(Base):
    __tablename__ = 'years'
    id = Column(Integer, primary_key=True)
    year = Column(Integer)


class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    genre = Column(String(50))


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    album_title = Column(String(100))
    language = Column(String(50))
    info = Column(String(1000))
    band_id = Column(Integer, ForeignKey('bands.id'))
    band_name = Column(String(100), ForeignKey('bands.name'))

    band = relationship('Band', backref=backref('bands'))

    __table_args__ = (UniqueConstraint('band_id','band_name'),)

class Track(Base):
    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    file = Column(String(100))
    title = Column(String(100))
    album_id = Column(Integer, ForeignKey('albums.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    artist = Column(String(100))
    # track number
    track = Column(Integer)
    plays = Column(Integer, default=0)
    year = Column(Integer)
    length = Column(Float)
    creation_time = Column(DateTime, default=func.now())


    album = relationship('Album', backref=backref('tracks'))
    genre = relationship('Genre', backref=backref('genres'))