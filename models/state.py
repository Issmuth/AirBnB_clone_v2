#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade='all, delete-orphan', backref='state')

    @property
    def cities(self):
        """Returns a list of cities linked to state_id"""
        from models import storage
        objs = storage.all()

        city_list = []
        for k, v in objs.items():
            if k.split('.')[0] == 'City':
                if v.state_id == self.id:
                    city_list.append(v)

        return city_list
