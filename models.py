from sqlalchemy import Column, Integer, String, Boolean
from database import Base
#Base is the hub that "knows" all tables in the project.

class Todo(Base):
    __tablename__="todos" 

    id=Column(Integer, primary_key=True, index=True)
    task=Column(String, nullable=False)
    completed=Column(Boolean, default=False)
    
