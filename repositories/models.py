from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////home/lam/db1', echo=True)
Base = declarative_base()


class User(Base):

    __tablename__ = "all_user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    full_name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    username = Column(String)
    disabled = Column(Boolean)
    
class Task(Base):

    __tablename__ = "all_task"

    task_id = Column(Integer, primary_key=True)
    client_id = Column(String)
    file_location = Column(String)
    output_file_location = Column(String)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()