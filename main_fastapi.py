from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import List, Optional

app=FastAPI()
todos=[] #temporary data storage for development case

class TodoInput(BaseModel):
    task:str
    completed:bool=False
    
class Todo(TodoInput):
    id:int # Assigned by the system in order, no user enters


@app.get("/")
def read_root():
    return {"message": "FastAPI toDo app."}


@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    raise HTTPException(status_code=404,detail=f"ID={todo_id} is not found.")

@app.post("/todos", response_model=Todo)
def create_todos(todo_data: TodoInput):
    new_id=1 if not todos else todos[-1].id+1
    todo=Todo(id=new_id,**todo_data.dict())
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id:int, updated_data:TodoInput):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            updated_todo=Todo(id=todo_id,**updated_data.dict())
            todos[index]=updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="ToDo not found.")


@app.delete("/todos/{todo_id}")
def delete_Todo(todo_id:int):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(index)
            for i,todo in enumerate(todos,start=1):
                todo.id=i
            return {"message":f"Todo (id={todo_id}) deleted and reordered tasks."}
    raise HTTPException(status_code=404, detail="Todo not found.")



