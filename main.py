import asyncio
import httpx
from ochi import fetch_ids, fetch_stories
from ochi.constants import BASE_URL


async def main() -> None:
    async with httpx.AsyncClient(base_url=BASE_URL) as c:
        ids = await fetch_ids(c)
        stories = await fetch_stories(c, ids)

        for story in stories:
            print(story)


if __name__ == '__main__':
    asyncio.run(main())
