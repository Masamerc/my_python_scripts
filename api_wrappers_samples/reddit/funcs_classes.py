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



@dataclass
class Submission:
    subreddit_url: str
    subreddit_name: str
    title: str
    selftext: str
    author: str
    created: int
    
    over_18: bool
    edited: bool
    is_original_content: bool
    locked: bool
    spoiler: bool
    
    num_comments: int
    num_crossposts: int
    num_duplicates: int
    num_reports: int
    num_upvotes: int
    num_downvotes: int
    
    def __post_init__(self):
        self.title = self.title.replace(',', ' ')
        self.selftext = self.selftext.replace(',', ' ')
        self.created = convert_timestamp(self.created)
    
    
def submission_factory(subreddit):
    return  Submission(
    subreddit.subreddit.url,
    subreddit.subreddit.url.split('/')[-2],
    subreddit.title,
    subreddit.selftext,
    subreddit.author.name,
    subreddit.created,
    subreddit.over_18,
    subreddit.edited,
    subreddit.is_original_content,
    subreddit.locked,
    subreddit.spoiler,
    subreddit.num_comments,
    subreddit.num_crossposts,
    subreddit.num_duplicates,
    subreddit.num_reports,
    subreddit.ups,
    subreddit.downs
    )


@dataclass
class Comment:
    author: str
    created: int
    body: str
    ups: int
    downs: int
    subreddit: str
    submission: str
        
    def __post_init__(self):
        self.body = self.body.replace(',', ' ')
        self.created = convert_timestamp(self.created)
        
        
def comment_factory(comment):
    return Comment(
        comment.author.name,
        comment.created,
        comment.body,
        comment.ups,
        comment.downs,
        comment.subreddit.title,
        comment.submission.title
    )


# testcoms = get_comments(mr10h[0])
# comments = [comment_factory(comment) for comment in testcoms]