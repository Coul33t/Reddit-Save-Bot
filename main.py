import praw
import json
import sqlite3
from config import CLIENT_ID, SECRET_KEY, USERNAME, PASSWORD

# ('id', 'subreddit_id', 'url', 'title', 'subreddit', 'body_html', 'author', 'author_fullname', 'created_utc', 'score')
def init_db():
    con = sqlite3.connect(DATABASE)
    con.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, subreddit_id TEXT, subreddit_name TEXT,)')
    con.execute('CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT, fullname TEXT)')
    con.commit()
    con.close()

def display(saved):
    for elem in saved:
        print('-----------------')
        if isinstance(elem, praw.models.reddit.comment.Comment):
            post = elem.body.split('\n')
            for line in post:
                print(line)

        elif isinstance(elem,praw.models.reddit.submission.Submission):
            print(elem.title)

def to_json(data, to_save):
    final_save = []

    for elem in saved:
        tmp_dict = {ts: elem[ts] for ts in to_save if ts in elem}

        try:
            tmp_dict['author'] = tmp_dict['author'].name

        except AttributeError:
            tmp_dict['author'] = 'deleted'

        tmp_dict['subreddit'] = tmp_dict['subreddit'].display_name

        if 'body_html' in tmp_dict:
            tmp_dict['type'] = 'comment'
        else:
            tmp_dict['type'] = 'post'

        print(f'Formatted {tmp_dict["author"]}\'s {tmp_dict["type"]}')
        final_save.append(tmp_dict)

    return final_save

if __name__ == '__main__':
    reddit = praw.Reddit(user_agent='yo', client_id=CLIENT_ID,
                         client_secret=SECRET_KEY, username=USERNAME,
                         password=PASSWORD)

    reddit.config.store_json_result = True

    me = praw.models.Redditor(reddit, name='Coul33t')

    saved = [vars(x) for x in me.saved()]

    to_save = ('id', 'subreddit_id', 'url', 'title', 'subreddit', 'body_html', 'author', 'author_fullname', 'created_utc', 'score')
    final_save = to_json(saved, to_save)

    with open('data.json', 'w') as f:
        json.dump(final_save, f)
