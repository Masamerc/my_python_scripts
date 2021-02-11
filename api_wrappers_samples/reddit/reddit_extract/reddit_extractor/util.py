import datetime
from dataclasses import dataclass

def convert_timestamp(ts):
    datetime_obj = datetime.datetime.fromtimestamp(ts)
    date = datetime.datetime.strftime(datetime_obj,"%m-%d-%Y")
    return date

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
    try:
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
    except AttributeError as e:
        print(e)
        pass