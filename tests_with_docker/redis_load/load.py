import pickle
from datetime import datetime
from redis import Redis
from collections import Counter

r = Redis(port=6379)

TIMESTAMP = datetime.now()
URL = "https://example.com"

words = ["Hey", "Hey", "Taro", "How", "Evil", "Evil"]

word_count = Counter(words)
word_count_with_metadata = {
    "word_count": dict(word_count),
    "url": URL,
    "timestamp": TIMESTAMP,
}


r.setex("word_count", 2, pickle.dumps(word_count_with_metadata))

import time
print("Sleeping....")
time.sleep(1)
try:
    print("Data retrieved from redis")
    data = pickle.loads(r.get("word_count"))
    print(f"URL: {data['url']}")
    print(f"DATA: {data['word_count']}")

except Exception as e:
    print("Data expired!")
    



