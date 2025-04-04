from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel 
from typing import List
from sqlalchemy.orm import Session
from database import engine,Base,SessionLocal
from models import Todo as TodoModel

Base.metadata.create_all(bind=engine)
#metadata: Contains all technical information about the table models defined in the Base class.
#create_all: Physically creates the table
#bind: Specifies which database to create a table in

app=FastAPI()
#todos=[] #temporary data storage for development case

#Pyandtic Input
class TodoInput(BaseModel):
    task:str
    completed:bool=False

#Pydantic Output    
class TodoOutput(TodoInput):
    id:int # Assigned by the system in order, no user enters

    class Config: 
        orm_mode=True #SQLAlchemy to Pydanctic model

#This function allows connecting to the database for each request (API call).
def get_db():
    db=SessionLocal() #A connection (session) to the database is opened
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "FastAPI toDo app with PostgreSQL."}


@app.get("/todos", response_model=List[TodoOutput])
def get_todos(db:Session= Depends(get_db)): 
    return db.query(TodoModel).all()

@app.get("/todos/{todo_id}", response_model=TodoOutput)
def get_todo(todo_id:int, db:Session=Depends(get_db)):
    todo=db.query(TodoModel).filter(TodoModel.id==todo_id).first()
    if todo == None:
        raise HTTPException(status_code=404,detail=f"ID={todo_id} is not found.")
    return todo

@app.post("/todos", response_model=TodoOutput)
def create_todos(todo_data: TodoInput, db: Session=Depends(get_db)):    
    new_todo=TodoModel(**todo_data.model_dump())
    db.add(new_todo)
    db.commit() #Makes the change permanent
    db.refresh(new_todo) 
    return new_todo

@app.put("/todos/{todo_id}", response_model=TodoOutput)
def update_todo(todo_id:int, updated_data:TodoInput, db:Session=Depends(get_db)):
    todo=db.query(TodoModel).filter(TodoModel.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found.")    
    
    todo.task=updated_data.task
    todo.completed=updated_data.completed

    db.commit()
    db.refresh(todo)
    return todo
    
@app.delete("/todos/{todo_id}")
def delete_Todo(todo_id:int, db: Session=Depends(get_db)):
    todo=db.query(TodoModel).filter(TodoModel.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found.")
    
    db.delete(todo)
    db.commit()
    return {"message": f"Todo (id={todo_id}) deleted succesfully."}



