Simple script to check whether some of your subreddits are not in a multireddit (yup, I love to keep my stuff organized).

# Usage

1. [Create a script application](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application)
2. `cp config.py.example config.py`
3. Set up variables in `config.py`
4. `python3 check.py` and enter your Reddit password

Apparently, there is no way of using Reddit API without your password unless you register your application. Let me know if you know how to avoid this!

# Prerequisites:
*  `pip3 install praw`