import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

load_dotenv()

SCHEMA = os.getenv("DB_SCHEMA", "peta_budaya_indonesia")

db = SQLAlchemy(metadata=MetaData(schema=SCHEMA))