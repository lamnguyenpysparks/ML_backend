from kafka import KafkaProducer, KafkaConsumer
from config import KAFKA_SERVERS, TASK_INPUT

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVERS)
consumer = KafkaConsumer(TASK_INPUT, bootstrap_servers=KAFKA_SERVERS, group_id="task_group")

if __name__ == "__main__":
    from kafka import KafkaConsumer
    
    consumer = KafkaConsumer(TASK_INPUT, bootstrap_servers=KAFKA_SERVERS, auto_offset_reset='earliest')
    for m in consumer:
        print(m)