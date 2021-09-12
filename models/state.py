#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        name = ""

        @property
        def cities(self):
            """ getter list of city instances related state"""
            myList = []
            new_dict = models.storage.all(City)
            for key, obj in new_dict.items():
                if self.id == obj.state_id:
                    myList.append(obj)
            return myList
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete")
