import urllib3
from pco_youtube_publisher import post_youtube_content, publish_pco_page
import time
import os

# Create an instance of a PoolManager for handling HTTP requests
http = urllib3.PoolManager()

while True:
    try:
        post_youtube_content()
        publish_pco_page()
        # Use urllib3 to perform the GET request
        heartbeat_url = os.environ.get('HEARTBEAT_URL')
        if heartbeat_url:
            response = http.request('GET', heartbeat_url)
            print(f"Heartbeat response: {response.status}")  # Optional: Log the status code
        else:
            print("HEARTBEAT_URL environment variable is not set.")
        time.sleep(900)
    except Exception as e:
        print(f"An error occurred: {e}")
