# Reddit-Save-Bot
A small bot I made to save my Reddit saved stuff offline.

## Requirements
* A Reddit application, make one here: https://www.reddit.com/prefs/apps/ (Be careful to chose `script`). You can put `http://localhost:8080` for the Redirect URI.
* A config file, containing the following:
  * `CLIENT_ID` = Your script ID
  * `SECRET_KEY` = Your script secret key
  * `USERNAME` = Your Reddit username
  * `PASSWORD` = Your Reddit password
  
## How to use it
Just launch the `main.py` script: `py main.py`. The results will be stored into `data.json`. For each entry, there will be these informations:

* Common:
  * `id`: Post ID
  * `subreddit_id`: Subreddit posted in ID
  * `url`: Post URL
  * `subreddit`: Subreddit posted in
  * `author`: Author of the post
  * `author_fullname`: Author's ID
  * `creation_utc`: Date of creation
  * `score`: Score of the post
  * `type`: Type of post (only " Post " or " Comment " at the moment)
  
* Comments specific:
  * `body`: Raw content of the comment
  * `body_html`: HTML content of the comment
  
* Posts specific:
  * `title`: Title of the post

## TODO:
* Database storage
* Checking for duplicate when gathering the saved posts
