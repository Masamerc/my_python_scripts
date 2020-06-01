#!/usr/env/bin/python3

import os
from googleapiclient.discovery import build

API_KEY = os.environ.get("YOUTUBE_API_KEY")


youtube = build(serviceName='youtube', version='v3', developerKey=API_KEY)

channel_request = youtube.channels().list(
    part='statistics',
    id='UCCezIgC97PvUuR4_gbFUs5g'
)

comments_request = youtube.commentThreads().list(
    part='snippet',
    videoId='YYXdXT2l-Gg'
)


def make_commentThreads_request(part: str, video_id: str) -> None:
    request = youtube.commentThreads().list(
        part=part,
        videoId=video_id,
        maxResults=100
    )
    return request.execute()


def extract_element(object: dict, element_name: str) -> str:
    return object["snippet"]["topLevelComment"]["snippet"][element_name]


def create_comment_date(object: dict) -> dict:
    return {
        "comment": extract_element(object, "textOriginal"),
        "author": extract_element(object, "authorDisplayName"),
        "like_count": extract_element(object, "likeCount"),
        "updated_at": extract_element(object, "updatedAt")
        }


if __name__ == "__main__":

    comments = make_commentThreads_request('snippet', '8oJYud7TV58')
    items = comments["items"]

    comments_list = [create_comment_date(item) for item in items]
    comments_list.sort(key=lambda x: x["like_count"])

    for comment in comments_list:
        print(comment["author"])
        print(comment["comment"])
        print(f"Likes: {comment['like_count']}")
        print(f"Date: {comment['updated_at']}")
        print("-"*15)
