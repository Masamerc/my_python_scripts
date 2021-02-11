import json
import tweepy
from decouple import config
from tweepy import Cursor


class TweeetFetcher:
    def __init__(self) -> None:
        self.api = self._get_client()


    def _get_client(self):
        api_key = config('API_KEY')
        api_secret_key = config('API_KEY_SECRET')

        access_token = config('ACCESS_TOKEN')
        access_secret_token = config('ACCESS_TOKEN_SECRET')
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_secret_token)

        api = tweepy.API(auth)
        return api


    def get_user_id(self, username: str):
        user = self.api.get_user(username)
        return user.id

    
    def search_tweets(self, q: str, num_items: int, dump_json=False):
        query = Cursor(self.api.search, q=q+' -filter:retweets', languages=['en'], tweet_mode='extended').items(num_items)
        tweets =  [tweet for tweet in query]

        if dump_json:
            tweets_json = [tweet._json for tweet in tweets]
            stringified_query = '_'.join(q.split())
            with open(f'search_dump-{stringified_query}.json', 'w') as f:
                json.dump(tweets_json, f, indent=2)

        return tweets


if __name__ == '__main__':
    fetcher = TweeetFetcher()
    user_result = fetcher.get_user_id('elonmusk')
    result = fetcher.search_tweets(q='evangelion AND delayed', num_items=50, dump_json=True)
