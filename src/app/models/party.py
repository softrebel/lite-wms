from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


Party=Base.classes.Party
Party.person = relationship("Person")
Party.company = relationship("Company")
print('slm')