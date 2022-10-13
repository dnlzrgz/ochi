import asyncio
from typing import List

import httpx

from ochi.models.story import Story


async def fetch_ids(c: httpx.AsyncClient, uri: str = 'topstories.json') -> List[int]:
    resp = await c.get(uri)
    if not resp.status_code == httpx.codes.OK:
        resp.raise_for_status()

    return resp.json()


async def fetch_story(c: httpx.AsyncClient, id: int) -> Story:
    resp = await c.get(f'item/{id}.json')
    if not resp.status_code == httpx.codes.OK:
        resp.raise_for_status()

    return Story(**resp.json())


async def fetch_stories(c: httpx.AsyncClient, ids: List[int]) -> List[Story]:
    tasks = []

    for id in ids:
        tasks.append(fetch_story(c, id))

    stories = await asyncio.gather(*tasks)
    stories = sorted(stories, reverse=True, key=lambda story: story.id)

    return stories
