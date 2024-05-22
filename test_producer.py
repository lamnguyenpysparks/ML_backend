from kafka import KafkaProducer
from config import KAFKA_SERVERS, TASK_INPUT

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVERS)

if __name__ == "__main__":
    import json
    
    msg = {
  "task_id": 7,
  "file_location": "data/Great Things studio_TT-505.jpg"
}
    
    producer.send(topic=TASK_INPUT, value=json.dumps(msg).encode())
    producer.flush()