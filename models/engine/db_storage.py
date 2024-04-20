#!/usr/bin/python3
"""Module that defines the database storage engine."""
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
import os
classes = [User, State, City, Amenity, Place, Review]


class DBStorage:
    """Database storage class."""

    __engine = None
    __session = None

    def __init__(self):
        """initializes a db storage engine."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB'),),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the current databases based on the specified cls."""
        obj_dict = {}
        obj_list = []
        if not cls:
            for cl in classes:
                obj_list.extend(self.__session.query(cl).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            obj_list.extend(self.__session.query(cls).all())

        for obj in obj_list:
            key = (obj.__class__.__name__) + '.' + obj.id
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Adds the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Save all the changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all the tables in the database and initialize
        the session attribute."""
        Base.metadata.create_all(self.__engine)
        sessionmade = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
        Session = scoped_session(sessionmade)
        self.__session = Session()

    def close(self):
        """closes the session."""
        self.__session.close()
