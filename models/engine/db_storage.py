#!/usr/bin/Python3
"""Engine module for the MySQL database"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ


user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')


class DBStorage:
    """Database storage class"""

    __engine = None
    __session = None
    __classes = [State, City, User, Place, Review, Amenity]

    def __init__(self):
        """DBStorage Constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
    if env == "test":
        Base.MetaData.drop_all()

    def all(self, cls=None):
        """Method returns a dictionary of objects"""
        my_dict = {}
        if cls in self.__classes:
            result = DBStorage.__session.query(cls)
            for row in result:
                key = "{}.{}".format(row.__class__.__name__, row.id)
                my_dict[key] = row
        elif cls is None:
            for cl in self.__classes:
                result = DBStorage.__session.query(cl)
                for row in result:
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    my_dict[key] = row
        return my_dict

    def new(self, obj):
        """Method that adds a new object to the current database"""
        DBStorage.__session.add(obj)

    def save(self):
        """Method commits all changes to the current database"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """Method that deletes a new object to the current database"""
        DBStorage.__session.delete(obj)

    def reload(self):
        """Method which creates the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()

    def close(self):
        """method that calls remove"""
        DBStorage.__session.close()
