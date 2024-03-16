
from  datetime  import datetime ,date, time
from typing import Optional
from pydantic import field_validator

from sqlmodel import Field, SQLModel
from to_do.table_model import days_option 

class add_Todo(SQLModel):
    content: str 
    day:days_option
    set_time:str
    
class task_list(SQLModel):
    list:list[dict]
    
class todo_update(SQLModel):
    content: Optional[str] 
    day:Optional[days_option]
    set_time:Optional[str]

