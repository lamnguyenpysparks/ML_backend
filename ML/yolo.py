from ultralytics import YOLO
from PIL import Image

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

im1 = Image.open("data/Great Things studio_TT-504.jpg")

results = model.predict(source=[im1, im1])
print(results)