from repositories.models import Task, get_db
from sqlalchemy.orm import Session

def insert_task(db : Session, client_id: str, file_location: str):
    task = Task(client_id=client_id, file_location=file_location)
    db.add(task)
    db.commit()
    return task

def read_task(db : Session, task_id: str):
    res = db.query(Task).filter(Task.task_id == task_id).first()
    return res

def update_task(db : Session, task_id: str, output_file_location: str):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    task.output_file_location = output_file_location
    db.commit()
    return task
    
if __name__ == '__main__':
    for db in get_db():
        # insert_task(db, '1', 'data/file.txt')
        a = read_task(db, '1')
        print(a)