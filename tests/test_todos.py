
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import text
import pytest
from fastapi.testclient import TestClient
from main_fastapi import app
from database import SessionLocal
from models import Todo

@pytest.fixture(autouse=True, scope="session")
def clear_database():
    db = SessionLocal()
    db.query(Todo).delete()
    db.execute(text("ALTER SEQUENCE public.todos_id_seq RESTART WITH 1;"))
    db.commit()
    db.close()

client = TestClient(app)


#GET Test
def test_get_todos():
    response=client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(),list)

    
#POST Test
def test_create_todo():
    todo_test_data={
        "task":"Task for Test" ,
        "completed":False
    }

    response=client.post("/todos", json=todo_test_data)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["task"]=="Task for Test"
    assert json_response["completed"]==False
    assert "id" in json_response

#GET With ID TEST
def test_get_todo_by_id():
    todo_test_data={
        "task": "Test for get todo by id",
        "completed":False
    }

    create_response=client.post("/todos",json=todo_test_data)
    assert create_response.status_code == 200

    todo_id=create_response.json()["id"]
    
    response=client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    json_response=response.json()

    assert json_response["id"]==todo_id
    assert json_response["task"]== "Test for get todo by id"
    assert json_response["completed"]==False

#PUT Test
def test_update_todo():
    todo_test_data={
        "task": "Test for put(update) todo",
        "completed":False
    } 

    create_response=client.post("/todos",json=todo_test_data)
    assert create_response.status_code == 200
    
    todo_id=create_response.json()["id"]
    
    updated_todo={
        "task":"Uptated: Test for put(update) todo",
        "completed":True
    }

    response=client.put(f"/todos/{todo_id}",json=updated_todo)
    assert response.status_code == 200

    json_response=response.json()
    assert json_response["id"]==todo_id
    assert json_response["task"] =="Uptated: Test for put(update) todo"
    assert json_response["completed"] == True

#DELETE TEST
def test_delete_todo():
    todo_test_data={
        "task": "Test for DELETE todo",
        "completed":False
    } 

    create_response=client.post("/todos",json=todo_test_data)
    assert create_response.status_code == 200
    
    todo_id=create_response.json()["id"]

    delete_response = client.delete(f"/todos/{todo_id}")
    assert delete_response.status_code == 200
    get_response = client.get(f"/todos/{todo_id}")
    assert get_response.status_code == 404