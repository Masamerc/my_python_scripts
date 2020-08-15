import os
import praw

from dataclasses import dataclass
from decouple import config


reddit = praw.Reddit(
    client_id=config("REDDIT_KEY"),
    client_secret=config("REDDIT_SECRET"),
    user_agent="NA"
)

# initialize subreddit instance of "Mr.Robot" subreddit
mr = reddit.subreddit("MrRobot")

# get 10 sumissions from "hot" category
def get_submissions(subreddit_with_category, limit) -> list: # example: mr.hot(limit=10)
    return [sub for sub in subreddit_with_category(limit=limit)]

# extract comments from submissions
def get_comments(submission, attribute=None) -> list:
    if attribute:
        return [comment.body for comment in submission.comments]
    return list(submission.comments)


hot_mr_subs = get_submissions(mr.hot, 10)

breakpoint()
