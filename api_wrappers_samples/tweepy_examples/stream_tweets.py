import csv
import datetime
import tweepy
import time
import os
import re
import logging as log

from uuid import uuid1
from decouple import config
from pathlib import Path


class StdOutStream(tweepy.StreamListener):
    def on_status(self, status: tweepy.Status) -> None:
        print(f'''
        Content: {status.text}
        Author: {status.author.name}
        Time: {status.created_at}
        ''')


class DataPipeStream(tweepy.StreamListener):

    def on_status(self, status: tweepy.Status):
        file_name = f'streamed_{datetime.datetime.now():%d%m%Y}.csv'
        file_exists = Path(os.path.join(os.getcwd(), file_name)).exists()

        if file_exists == False:
            log.info('Started writing to ' + file_name)
            with open(file_name, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'content', 'author', 'time'])

        with open(file_name, 'a') as f:
            log.info(f'Tweet detected. Writing data to file - at {datetime.datetime.now()}')
            writer = csv.writer(f)
            writer.writerow([str(uuid1()), self.sanitize_text(status.text), status.author.name, status.created_at])
            time.sleep(1)


    def sanitize_text(self, text:str) -> str:
        return re.sub(r'[\n,]', ' ', text)

        

if __name__ == '__main__':

    log.basicConfig(level=log.INFO)

    api_key = config('API_KEY')
    api_secret_key = config('API_KEY_SECRET')
    access_token = config('ACCESS_TOKEN')
    access_secret_token = config('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_secret_token)

    stdout_stream = tweepy.Stream(auth, StdOutStream())
    datapipe_csv_stream = tweepy.Stream(auth, DataPipeStream())

    # stream-load tweets that match condition
    print('Starting stream...')
    datapipe_csv_stream.filter(track=['ps5', '楽天', '買えた'], languages=['ja'])
