from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
db_url=os.getenv('DB_URL')
engine = create_engine(db_url, echo=True)