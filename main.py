import asyncio
import httpx
import asyncclick as click
from rich.console import Console
from ochi import fetch_ids, fetch_stories
from ochi.constants import BASE_URL


@click.command()
@click.option('--max', type=int, default=500, help='Max number of stories.')
async def main(max: int) -> None:
    console = Console()
    stories = []

    with console.status("[bold white]Loading stories...", spinner='point'):
        async with httpx.AsyncClient(base_url=BASE_URL) as c:
            ids = await fetch_ids(c)
            stories = await fetch_stories(c, ids[:max])

    for story in stories:
        print(story)


if __name__ == '__main__':
    asyncio.run(main())
