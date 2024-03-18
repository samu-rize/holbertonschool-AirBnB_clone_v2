#!/usr/bin/python3
"""
Module for the DBStorage class, a storage engine using SQLAlchemy
to interact with a MySQL database for the AirBnB Clone project.
"""

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker, Session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    """
    Storage engine using SQLAlchemy to interact with a MySQL database.

    Attributes:
    __engine (sqlalchemy.Engine): The SQLAlchemy engine.
    __session (sqlalchemy.Session): The SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new instance of DBStorage.

        Creates the SQLAlchemy engine.
        """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")
            ),
            pool_pre_ping=True
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Retrieves all objects of a given class from the database.

        Args:
        cls (class): The class to filter objects by.

        Returns:
        dict: A dictionary containing all objects,
        formatted as "{class_name}.{id}".
        """
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            objects = self.__session.query(cls)

        else:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())

        return {
            "{}.{}".format(
                type(obj).__name__,
                obj.id): obj for obj in objects}

    def new(self, obj):
        """
        Adds a new object to the current database session.

        Args:
        obj: The object to be added.
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database session.

        Args:
        obj: The object to be deleted.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and starts a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
