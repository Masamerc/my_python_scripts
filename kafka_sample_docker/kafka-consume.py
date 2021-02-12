from kafka import KafkaConsumer
from json import load, loads

consumer = KafkaConsumer(
    'sample2',
    bootstrap_servers=['localhost:9092'],
    # auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

def format_msg(msg:str) -> str:
    fmt_msg = f'''
    Data: {msg.value['data']}
    Timestamp: {msg.timestamp}
    Topic: {msg.topic}
    '''

    return fmt_msg

for msg in consumer:
    msg = format_msg(msg)
    print(msg)