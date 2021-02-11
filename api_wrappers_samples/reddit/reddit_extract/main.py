import datetime
import os
import praw
import pandas as pd

from dataclasses import dataclass, asdict
from decouple import config
from tqdm import tqdm

from reddit_extractor import Comment, Submission, submission_factory, comment_factory


date_asof = datetime.datetime.strftime(datetime.datetime.now(),"%m-%d-%Y")
date_file_format = datetime.datetime.strftime(datetime.datetime.now(),"%m%d%Y")

reddit = praw.Reddit(
    client_id=config("REDDIT_KEY"),
    client_secret=config("REDDIT_SECRET"),
    user_agent="NA"
)


def extract_attributes_from_subreddit(subreddit):
    return {
        "active_user_count": subreddit.active_user_count,
        "url": subreddit.url,
        "title": subreddit.title,
        "subscribers": subreddit.subscribers,
        "subreddit_type": subreddit.subreddit_type,
        "spoilers_enabled": subreddit.spoilers_enabled,
        "public_description": subreddit.public_description,
        "over18": subreddit.over18,
        "created": subreddit.created,
        "created_utc": subreddit.created_utc,
        "lang": subreddit.lang,
        "videos_allowed": subreddit.allow_videos,
        "images_allowed": subreddit.allow_images
    }


def convert_timestamp(ts):
    datetime_obj = datetime.datetime.fromtimestamp(ts)
    date = datetime.datetime.strftime(datetime_obj,"%m-%d-%Y")
    return date



def get_submissions(subreddit_name: str, category: str, limit: int) -> list:
    '''
    Categories: hot, new or top
    
    >>> get_submissions('MrRobot', 'hot', 10)
    '''
    subreddit = reddit.subreddit(subreddit_name)
    if category == 'hot':
        submission_obj = subreddit.hot(limit=limit)
    elif category == 'new':
        submission_obj = subreddit.new(limit=limit)
    else:
        submission_obj = subreddit.top(limit=limit)
    
    return [sub for sub in submission_obj]



def get_comments(submission: praw.models.reddit.submission.Submission, body: bool=False) -> list:
    if body:
        return [comment.body for comment in submission.comments]
    return list(submission.comments)



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
    subreddits_df['name'] = subreddit_names
    subreddits_df['asof'] = date_asof

    # save as csv
    subreddits_df.to_csv(f'output/top_100_subreddits_{date_file_format}.csv', index=False)

    
def store_submissions_to_csv(subreddit_names, category, num_subreddits=10, limit=10):
    
    print('Getting list of subreddits...')
    
    submissions = []
    
    for subreddit in tqdm(subreddit_names[:num_subreddits]):
        submission_objects = get_submissions(subreddit, category, limit)
        # add error handling
        submission_data = []
        for submission_obj in submission_objects:
            if submission_obj:
                submission_data.append(submission_factory(submission_obj))

        for submission in submission_data:
            if submission:
                try:
                    submissions.append(asdict(submission))
                except TypeError as e:
                    print(submission)
                    print(e)
                    continue
    
    print('Data extraction complete.')
    print('Storing data to csv...')
    
    pd.DataFrame(submissions).to_csv(f'output/{category}_submissions_{date_file_format}.csv', index=False)



if __name__ == "__main__":
    # # subreddit extraction
    subreddit_names = get_top_100_subreddits()
    # subreddit_data = extract_attributes_from_subreddits(subreddit_names)
    # store_subreddits_to_csv(subreddit_data, subreddit_names)
    
    # submission extraction
    # for category in ['hot', 'new', 'top']:
    #     store_submissions_to_csv(subreddit_names, category, num_subreddits=50, limit=10)

    # retry
    store_submissions_to_csv(subreddit_names, 'top', num_subreddits=50, limit=10)
    