import os
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

URI = os.environ.get("POSTGRES_URI")
db = create_engine(URI)

words = pd.read_csv("../dump_csv/word_dump.csv")
sents = pd.read_csv("../dump_csv/sent_dump.csv")

words.to_sql(
    "words",
    db,
    schema="public",
    if_exists="append",
    index=False
)

sents.to_sql(
    "sents",
    db,
    schema="public",
    if_exists="append",
    index=False
)