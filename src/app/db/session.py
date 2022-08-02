from sqlalchemy import create_engine,MetaData,Column, Integer, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from app.core.config import settings


metadata = MetaData()
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    # required for sqlite
    # connect_args={"check_same_thread": False},
)

# Table('Party',metadata, Column('Id', Integer, 
# primary_key=True), autoload=True, autoload_with=engine)
Base = automap_base(metadata=metadata)

# Base.prepare(autoload_with=engine)
Base.prepare(autoload_with=engine, reflect=True, schema='dbo')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
