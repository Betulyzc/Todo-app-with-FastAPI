#database.py 
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base=declarative_base()
#Base is the hub that "knows" all tables in the project.
#The base class from which all model (table) classes will derive