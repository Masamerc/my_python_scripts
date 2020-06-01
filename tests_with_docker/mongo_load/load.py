from pymongo import MongoClient
import pickle
from datetime import datetime
from collections import Counter

client = MongoClient(
    host="localhost",
    port=27017
)

db = client.sentword
words_col = db.words
sents_col = db.sents

words_col.ensure_index("timestamp", expireAfterSeconds=60) #deprecated, use create_index instead 

TIMESTAMP = datetime.utcnow()
URL = "https://example.com"

words = ["Doom", "Doom", "ACNH", "DOOM", "ACNH", "COD:MW"]

word_count = Counter(words)
word_count_with_metadata = {
    "word_count": dict(word_count),
    "url": URL,
    "timestamp": TIMESTAMP,
}

words_col.insert(word_count_with_metadata) # deprecated? use insert_one() or insert_many() instead