from datetime import datetime, time
from enum import Enum
from typing import Optional
from pydantic import field_validator
from sqlmodel import SQLModel, Field



class days_option(str, Enum):
    today="Today",
    tomorrow="Tomorrow",
    someday="Someday"



class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str 
    day:days_option
    set_time:str
