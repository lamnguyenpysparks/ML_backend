from managers.kafka_managers import consumer, producer
from repositories.task_repository import update_task
from repositories.models import get_db
from ultralytics import YOLO
from PIL import Image
import json
from datetime import datetime
from config import TASK_OUTPUT
# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

for db in get_db():
    for m in consumer:
        start = datetime.now()
        # try:
        data = json.loads(m.value)
        fn = data["file_location"]
        im1 = Image.open(fn)
        results = model.predict(source=im1, save=True)
        msg = {"task_id" : data["task_id"], "file_location" : fn.replace("data/", f"{results[0].save_dir}/")}
        update_task(db, data["task_id"], msg["file_location"])
        producer.send(TASK_OUTPUT, json.dumps(msg).encode())
        print(results)
        # except:
        #     pass
        print(f'PROCESSING TIME : {datetime.now() - start} . FINISH {msg}')