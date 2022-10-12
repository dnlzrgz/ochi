import asyncio

import asyncclick as click
import httpx
from rich import print as rprint

from ochi.constants import HN_BASE_URL, HN_CATEGORIES
from ochi.fetch import fetch_ids, fetch_stories


@click.command()
@click.option(
    '-m',
    '--max',
    type=int,
    default=500,
    help='Max number of stories.',
    show_default=True,
)
@click.option(
    '-c',
    '--category',
    type=click.Choice(
        ['top', 'new', 'best', 'ask', 'show', 'job'], case_sensitive=False
    ),
    default='top',
    help='Category.',
    show_default=True,
)
@click.option(
    '--order-by',
    type=click.Choice(['id', 'score', 'date'], case_sensitive=False),
    default='id',
    help='Order stories by their id, score or date.',
    show_default=True,
)
@click.option(
    '--reverse',
    type=bool,
    is_flag=True,
    default=False,
    help='Reverse order.',
    show_default=True,
)
async def cli(max: int, category: str, order_by: str, reverse: bool) -> None:
    stories = []
    client = httpx.AsyncClient(base_url=HN_BASE_URL)

    try:
        ids = await fetch_ids(client, HN_CATEGORIES[category])
        ids.sort(reverse=True)

        stories = await fetch_stories(client, ids[:max])

        if order_by == 'id':
            stories.sort(key=lambda s: s.id, reverse=reverse)
        elif order_by == 'score':
            stories.sort(key=lambda s: s.score, reverse=reverse)
        elif order_by == 'date':
            stories.sort(key=lambda s: s.time, reverse=reverse)

    except httpx.HTTPStatusError as err:
        rprint(
            f"Error response {err.response.status_code} while fetching {err.request.url}"
        )

    except httpx.RequestError as err:
        rprint(
            f'A request error happened while fetching stories from {err.request.url}: {err}'
        )
    else:
        for story in stories:
            rprint(story.pretty_str())
    finally:
        await client.aclose()


def run():
    asyncio.run(cli())
