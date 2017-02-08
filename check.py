# Create a submission to /r/test
import getpass

import praw

import config

password = getpass.getpass("Password for Reddit ({})".format(config.USERNAME))

reddit = praw.Reddit(
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    user_agent="1111",
    username=config.USERNAME,
    password=password,
)


msubs = set()
subs_map = {}

for mr in reddit.user.multireddits():
    for sr in mr.subreddits:
        msubs.add(sr)
        l = subs_map.get(sr, [])
        l.append(mr)
        subs_map[sr] = l

subs = set(reddit.user.subreddits())

for sub in subs.difference(msubs):
    print("Subreddit {} is not in a multi!".format(str(sub)))

for sub in msubs.difference(subs):
    print("Subreddit {} is in multis {}, but you're not subscribed to it".format(str(sub), str(subs_map[sub])))