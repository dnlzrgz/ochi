import json
import httpx
from models import Story

BASE_URL = 'https://hacker-news.firebaseio.com/v0/'


def get_stories_ids(c: httpx.Client) -> list:
    # TODO: improve return type
    r = c.get('topstories.json')
    if not r.status_code == httpx.codes.OK:
        # TODO: handle
        r.raise_for_status()

    return r.json()


def get_story_data(c: httpx.Client, id: str) -> dict:
    # TODO: improve return type
    r = c.get(f'item/{id}.json')
    if not r.status_code == httpx.codes.OK:
        # TODO: handle
        r.raise_for_status()

    return r.json()


def main() -> None:
    stories: list[Story] = []
    with httpx.Client(base_url=BASE_URL) as c:
        stories_ids = get_stories_ids(c)
        for id in stories_ids[:10]:
            data = get_story_data(c, id)
            stories.append(Story(**data))

    for story in stories:
        print(story.title)


if __name__ == '__main__':
    main()
