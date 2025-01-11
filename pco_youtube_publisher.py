import pypco
import feedparser
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv()


def get_channel_feed(channel_id):
    NewsFeed = feedparser.parse(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
    return NewsFeed


def get_youtube_json_payload_from_rss(channel_id):

    entry = get_channel_feed(channel_id).entries
    elements = []
    try:
        if os.environ.get('LIVE_EMBED_CODE') and date.today().weekday() == int(os.environ.get('LIVE_DAY')):
            elements.append(os.environ.get('LIVE_EMBED_CODE'))
    except ValueError:
        pass

    for counter, e in enumerate(entry):
        if counter < int(os.environ.get('YOUTUBE_VIDEOS_TO_POST')):
            title = f"<p><h1>{e.title}</h1</p>\n"
            elements.append(title)
            elements.append(
                f"""<p><iframe width="560" height="314" src="{e.link.replace('watch?v=', '/embed/', 1)}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>"""
                )
    elements.append(
    f'<p><h1 style="text-align: center;"><a title="More Videos" href="https://youtube.com/channel/{channel_id}" target="_blank" rel="noopener">More Videos</a></h1></p>')
    html_txt = "".join(elements)
    return html_txt


def post_youtube_content():
    html_txt = get_youtube_json_payload_from_rss(os.environ.get('YOUTUBE_CHANNEL'))
    pco = pypco.PCO(os.environ.get('PCO_CLIENT_ID'), os.environ.get('PCO_CLIENT_SECRET'))
    slug = os.environ.get("PCO_PUBLISHING_SLUG")
    payload = pco.template('Page',
                           {'title': os.environ.get('PCO_PUBLISHING_TITLE'),
                            "content": html_txt,
                            "slug": os.environ.get('PCO_PUBLISHING_SLUG'),
                            })
    pco.post('/publishing/v2/pages', payload)
    return


def publish_pco_page():
    pco = pypco.PCO(os.environ.get('PCO_CLIENT_ID'), os.environ.get('PCO_CLIENT_SECRET'))
    publish_url = pco.get(f'/publishing/v2/abstract_pages/'
                          f'page-{os.environ.get("PCO_PUBLISHING_SLUG")}'
                          f'')
    pco.post(publish_url['data']['attributes']['page_actions'][0]['url'], {})
    subdomain = pco.get('/publishing/v2')['data']['attributes']['subdomain']
    print(f"Published Youtube Channel content to https://{subdomain}.churchcenter.com/pages/{os.environ.get('PCO_PUBLISHING_SLUG')}")


if __name__ == '__main__':
    # Posts your youtube content as a draft
    post_youtube_content()

    # Publishes the page
    publish_pco_page()
