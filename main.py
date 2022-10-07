import asyncio

import asyncclick as click
import httpx
from rich import print as rprint

from ochi import HN_BASE_URL, fetch_ids, fetch_stories


@click.command()
@click.option('--max', type=int, default=500, help='Max number of stories.')
async def main(max: int) -> None:
    client = httpx.AsyncClient(base_url=HN_BASE_URL)
    stories = []

    try:
        ids = await fetch_ids(client)
        stories = await fetch_stories(client, ids[:max])
    except httpx.HTTPStatusError as err:
        rprint(
            f"Error response {err.response.status_code} while fetching {err.request.url}"
        )

    except httpx.RequestError as err:
        rprint(
            f'A request error happened while fetching stories from {err.request.url}: {err}'
        )
    finally:
        await client.aclose()

    for story in stories:
        rprint(story.pretty_str())


if __name__ == '__main__':
    asyncio.run(main())
