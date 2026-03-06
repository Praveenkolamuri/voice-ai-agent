from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///appointments.db"

engine = create_engine(DATABASE_URL)