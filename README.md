# pco-youtube-publisher
This is a simple script to publish a youtube channel's latest 10 videos to a Planning Center Publishing page.
It's the latest 10 videos because I've noticed instability with the Church Center App when adding more videos.
The configuration for your youtube channel and the page you want to publish to is in the .env file.
The Slug and Title will be created if it doesn't exist.

It takes a youtube channel like this:
[![Youtube Channel](https://raw.githubusercontent.com/pastorhudson/pco-youtube-publisher/master/images/youtube.png)](https://https://raw.githubusercontent.com/pastorhudson/pco-youtube-publisher/master/images/youtube.png)

And turns it into a Church Center page like this:
[![Church Center Page](https://raw.githubusercontent.com/pastorhudson/pco-youtube-publisher/master/images/church_center.png)](https://https://raw.githubusercontent.com/pastorhudson/pco-youtube-publisher/master/images/youtube.png)

https://yourcbcfamily.churchcenter.com/pages/media

## Setup
- Download this repository
`git clone https://github.com/pastorhudson/pco-youtube-publisher.git`

- In the pco-youtube-publishing directory edit the .env file with your settings:
```
PCO_CLIENT_ID=Application ID
PCO_CLIENT_SECRET=Secret
PCO_PUBLISHING_SLUG=test
PCO_PUBLISHING_TITLE=TEST
YOUTUBE_CHANNEL=Channel ID
LIVE_EMBED_CODE=<h1>Live</h1><iframe src="https://vimeo.com/event/174541/embed" width="560" height="315" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
```
- Get your youtube channel ID here https://www.youtube.com/account_advanced
- Get your Planning Center Personal API Key here https://api.planningcenteronline.com/oauth/applications
- If you add embed code for your live stream then it will post this video embed as the first in the list. We use vimeo and it has an option for reoccuring event. So our event embed doesn't change and when it's not live it just shows upcoming:

[![LIVE EMBED](https://raw.githubusercontent.com/pastorhudson/pco-youtube-publisher/master/images/vimeo_sm.png)](https://https://raw.githubusercontent.com/pastorhudson/pco-youtube-publisher/master/images/vimeo_sm.png)

- You need Python 3.8 or greater
- Setup a python virtual environment (Optional)
Linux `python3.8 -m venv ./venv`
- Activate python virtual environment
Linux `source ./venv/bin/activate`

- Install requirements
`pip install -r requirements.txt`

- Run the script
`python3 pco-youtube-publisher.py`

## Crontab
- I've provided update.sh as a simple script to use for running this as a cron job.
- You just need to edit the path's in the update.sh. They need to be full directories since cron doesn't run as user.

