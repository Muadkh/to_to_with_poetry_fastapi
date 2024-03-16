
from typing import Optional
from sqlmodel import Field, Session, SQLModel, select
from fastapi import FastAPI, Depends
from to_do.data_model import add_Todo, task_list, todo_update
from to_do.todo_table import engine
from to_do.table_model import Todo, days_option

app= FastAPI(
      title='To_do APIs',
      version="0.0.1",
      servers=[{
            "url":"",
            "description":"Development Server"
      }]

)

def get_session():
    with Session(engine) as session:
        yield session 

@app.get("/")
def to_do_root():
    return {"Hello": True}

@app.post("/create_table_model_/",response_model=Todo)
async def create_table():
    SQLModel.metadata.create_all(engine)
    return {"message": "Successfully created table in Database"}
@app.post("/add_to_do/",response_model=Todo)
async def add_todo(todo:add_Todo, session:Session=Depends(get_session)):
        to_do=Todo.model_validate(todo)
        session.add(to_do)
        session.commit()
        session.refresh(to_do)
        return to_do   
@app.get("/get_to_do/")
async def get_todo_all(select_day:days_option , session:Session=Depends(get_session)):
         statement= select(Todo).where(Todo.day == select_day)
         result= session.exec(statement).all()
         return result
@app.delete("/delete_to_do/")
async def delete_todo_(select_day:days_option,todo_id:int , session:Session=Depends(get_session)):
         statement= select(Todo).where(Todo.id == todo_id , Todo.day == select_day)
         result= session.exec(statement).one()
         session.delete(result)
         session.commit()
         return {'Task Deleted', True}
@app.patch("/update_to_do/")
async def update_todo_(select_day:days_option,todo_id:int ,update:todo_update, session:Session=Depends(get_session)):
        statement= select(Todo).where(Todo.id == todo_id , Todo.day == select_day)
        result= session.exec(statement).one()
        if update.content is not None:
            result.content=update.content
        if update.set_time is not None:
              result.set_time= update.set_time
        if update.day is not None:
              result.day=update.day
        session.add(result)
        session.commit()
        session.refresh(result)
        return result