import praw
import os
from dotenv import load_dotenv
import re

load_dotenv()

def fetch_data():
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT")
    )

    user_input = "ENTER THE USERNAME URL OR THE USERNAME WITHOUT /u"
    match = re.search(r"(?:reddit\.com\/u(?:ser)?\/)([\w-]+)", user_input)
    username = match.group(1) if match else user_input
    user = reddit.redditor(username)

    comments = []
    for comment in user.comments.new(limit=None):
        comments.append({
            "subreddit": str(comment.subreddit),
            "body": comment.body,
            "created_utc": comment.created_utc,
            "permalink": f"https://www.reddit.com{comment.permalink}"
        })

    return comments

docs = fetch_data()

