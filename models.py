from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import random
import string

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    email = Column(String(32), index=True)

class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
             'id': self.id,
             'name': self.name,
        }


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    cat_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories)
    title = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    category = relationship(Categories, backref='items')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'cat_id': self.cat_id,
            'description': self.description,
            'title': self.title,
            'user_id': self.user_id
        }

engine = create_engine('sqlite:///ItemCatalog.db')


Base.metadata.create_all(engine)
