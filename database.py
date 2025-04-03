#database.py 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://todo_user:todo_pass@localhost:5432/tododb"

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base=declarative_base()