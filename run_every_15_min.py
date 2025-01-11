from pco_youtube_publisher import post_youtube_content, publish_pco_page
from requests import requests

while True:
    try:
        post_youtube_content()
        publish_pco_page()
        requests.get(os.environ.get('HEARTBEAT_URL'))
        time.sleep(900)
    except Exception as e:
        print(e)