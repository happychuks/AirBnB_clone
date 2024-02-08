#!/usr/bin/python3
"""
    This Module contains the Amenity class!
"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey

class Amenity(BaseModel, Base):
    """
        The Amenity class!
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    if __name__ == "db":
        place_amenities = relationship(
            "Place",
            secondary=place_amenity, back_populates="amenities"
        )
        pass
