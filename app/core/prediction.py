from fastapi import APIRouter, Request, BackgroundTasks, UploadFile, Depends
from repositories.models import get_db
import json
from repositories.task_repository import insert_task, read_task
from managers.kafka_managers import producer
from fastapi.responses import FileResponse
from uuid import uuid4
from config import TASK_INPUT, TASK_OUTPUT

prediction_api = APIRouter()

@prediction_api.post("/prediction", tags=["prediction"])
async def predict(
                    client_id : str,
                    token : str,
                    file : UploadFile,
                  ):
    for db in get_db():
        fn = f"data/{file.filename}"
        with open(fn, "wb") as buffer:
            while content := await file.read(1024):  # async read chunk
                buffer.write(content)
        res = insert_task(db, client_id, fn)
        producer.send(topic=TASK_INPUT, value=json.dumps({"task_id" : res.task_id, "file_location" : fn}).encode(), key=str(res.task_id).encode())
        producer.flush()
        return {"task_id" : res.task_id, "file_location" : fn}
    
@prediction_api.get("/result", tags=["prediction"])
async def result(task_id : str):
    for db in get_db():
        res = read_task(db, task_id)
        return FileResponse(res.output_file_location)
    