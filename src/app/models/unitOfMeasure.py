from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


UnitOfMeasure=Base.classes.UnitOfMeasure