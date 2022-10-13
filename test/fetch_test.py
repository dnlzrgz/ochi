from cgi import test

import httpx
import pytest
import respx
from httpx import Response

from ochi.constants import HN_BASE_URL, HN_CATEGORIES
from ochi.fetch import fetch_ids, fetch_story

TEST_URL = f'{HN_BASE_URL}{HN_CATEGORIES["top"]}'


@pytest.mark.asyncio
@respx.mock
async def test_fetch_ids_200_status() -> None:
    mock = respx.get(TEST_URL).mock(
        return_value=Response(status_code=200, text="[1, 2, 3, 4]")
    )

    client = httpx.AsyncClient(base_url=HN_BASE_URL)
    ids = await fetch_ids(client)

    assert mock.called
    assert mock.call_count == 1
    assert ids == [1, 2, 3, 4]

    await client.aclose()


@pytest.mark.asyncio
@respx.mock
async def test_fetch_ids_bad_status() -> None:
    mock = respx.get(TEST_URL).mock(return_value=Response(status_code=404))

    client = httpx.AsyncClient(base_url=HN_BASE_URL)

    with pytest.raises(httpx.HTTPStatusError):
        _ = await fetch_ids(client)

    assert mock.called
    assert mock.call_count == 1

    await client.aclose()


@pytest.mark.asyncio
@respx.mock
async def test_fetch_story() -> None:
    test_story = {
        "by": "dhouston",
        "descendants": 71,
        "id": 8863,
        "kids": [
            9224,
            8917,
            8952,
            8958,
            8884,
            8887,
            8869,
            8873,
            8940,
            8908,
            9005,
            9671,
            9067,
            9055,
            8865,
            8881,
            8872,
            8955,
            10403,
            8903,
            8928,
            9125,
            8998,
            8901,
            8902,
            8907,
            8894,
            8870,
            8878,
            8980,
            8934,
            8943,
            8876,
        ],
        "score": 104,
        "time": 1175714200,
        "title": "My YC app: Dropbox - Throw away your USB drive",
        "type": "story",
        "url": "http://www.getdropbox.com/u/2/screencast.html",
    }

    mock = respx.get(f'{HN_BASE_URL}item/{test_story["id"]}.json').mock(
        return_value=Response(status_code=200, json=test_story)
    )

    client = httpx.AsyncClient(base_url=HN_BASE_URL)
    story = await fetch_story(client, 8863)

    assert mock.called
    assert mock.call_count == 1
    assert story.id == test_story['id']
    assert story.by == test_story['by']

    await client.aclose()
