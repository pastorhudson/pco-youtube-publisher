# pco-youtube-publisher
This is a simple script to publish a youtube channel's latest 15 videos to a Planning Center Publishing page.

# Setup
- Download this repository
`git clone https://github.com/pastorhudson/pco-youtube-publisher.git`

- In the pco-youtube-publishing directory edit the .env file with your settings:
```
PCO_CLIENT_ID=Application ID
PCO_CLIENT_SECRET=Secret
PCO_PUBLISHING_SLUG=test
PCO_PUBLISHING_TITLE=TEST
YOUTUBE_CHANNEL=Channel ID
```
- So if your Youtube channel address is `https://www.youtube.com/channel/UCnSsWxgHMVOPpzRJWTM7eDA/`
Then your `YOUTUBE_CHANNEL=UCnSsWxgHMVOPpzRJWTM7eDA`

- Setup a virtual environment (Optional-Recomended)
Linux `python3 -m venv ./venv`

- Install requirements
`pip install -r requirements.txt`

- Run the script
`python3 pco-youtube-publisher.py`
