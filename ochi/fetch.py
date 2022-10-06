import asyncio

import httpx

from ochi.models.story import Story

# TODO: handle exceptions


async def fetch_ids(c: httpx.AsyncClient, uri: str = 'topstories.json') -> list[str]:
    resp = await c.get(uri)
    if not resp.status_code == httpx.codes.OK:
        resp.raise_for_status()

    return resp.json()


async def fetch_story(c: httpx.AsyncClient, id: str) -> Story:
    resp = await c.get(f'item/{id}.json')
    if not resp.status_code == httpx.codes.OK:
        resp.raise_for_status()

    return Story(**resp.json())


async def fetch_stories(c: httpx.AsyncClient, ids: list[str]) -> list[Story]:
    tasks = []

    for id in ids:
        tasks.append(fetch_story(c, id))

    stories = await asyncio.gather(*tasks)
    stories = sorted(stories, reverse=True, key=lambda story: story.id)

    return stories
