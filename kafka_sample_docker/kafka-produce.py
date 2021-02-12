from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

for _ in range(10):
    producer.send('sample2', {'data': 23})

producer.flush()