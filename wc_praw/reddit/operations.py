import datetime
import os
import praw
import pandas as pd

from dataclasses import dataclass, asdict
from decouple import config
from tqdm import tqdm


reddit = praw.Reddit(
    client_id=config("REDDIT_KEY"),
    client_secret=config("REDDIT_SECRET"),
    user_agent="NA"
)



date_asof = datetime.datetime.strftime(datetime.datetime.now(),"%m-%d-%Y")
date_file_format = datetime.datetime.strftime(datetime.datetime.now(),"%m%d%Y")


def get_top_100_subreddits():
    # read table from the webiste
    top_100 = pd.read_html('https://frontpagemetrics.com/top')
    top_100_subreddits = top_100[0]

    # return subreddit names as list 
    subreddit_names = [subreddit.split('/')[-1] for subreddit in top_100_subreddits.Reddit]
    return subreddit_names


def extract_attributes_from_subreddits(subreddit_names):
    # get subreddit objects
    subreddits = [reddit.subreddit(subreddit_name) for subreddit_name in subreddit_names]

    # return attributes from each subreddit list of dict
    
    subreddit_data = [extract_attributes_from_subreddit(subreddit) for subreddit in tqdm(subreddits)]
    return subreddit_data    
    

def store_subreddits_to_csv(subreddit_data, subreddit_names):
    # store the result in dataframe
    subreddits_df = pd.DataFrame(subreddit_data)

    # add a few columns
    subreddits_df['created_date'] = subreddits_df.created.apply(convert_timestamp)
    subreddits_df['name'] = top_100_subreddits
    subreddits_df['asof'] = date_asof

    # save as csv
    subreddits_df.to_csv(f'top_100_subreddits_{date_file_format}.csv', index=False)

    
def store_submissions_to_csv(category, num_subreddits=10, limit=10):
    
    print('Getting list of subreddits...')
    
    submissions = []
    
    for subreddit in tqdm(top_100_subreddits[:num_subreddits]):
        submission_objects = get_submissions(subreddit, category, limit)
        submission_data = [submission_factory(submission_obj) for submission_obj in submission_objects]
        submissions += [asdict(submission) for submission in submission_data]
    
    print('Data extraction complete.')
    print('Storing data to csv...')
    
    pd.DataFrame(submissions).to_csv(f'{category}_submissions_{date_file_format}.csv', index=False)

