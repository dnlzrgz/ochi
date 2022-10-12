from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from urllib.parse import urlparse

from ochi.constants import HN_STORY_URL


def prettify_time(time_str: int) -> str:
    now = datetime.now()

    if type(time_str) is int:
        diff = now - datetime.fromtimestamp(time_str)
    elif isinstance(time_str, datetime):
        diff = now - time_str
    elif not time_str:
        diff = now - now

    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''
    if day_diff == 0:
        if second_diff < 10:
            return 'just now'
        if second_diff < 60:
            return str(second_diff) + ' seconds ago'
        if second_diff < 120:
            return '1 minute ago'
        if second_diff < 3600:
            return str(second_diff // 60) + ' minutes ago'
        if second_diff < 7200:
            return '1 hour ago'
        if second_diff < 86400:
            return str(second_diff // 3600) + ' hours ago'

    if day_diff == 1:
        return 'Yesterday'

    if day_diff < 7:
        return str(day_diff) + ' days ago'

    if day_diff < 31:
        return str(day_diff // 7) + ' week(s) ago'

    if day_diff < 365:
        return str(day_diff // 30) + ' month(s) ago'

    return str(day_diff // 365) + ' year(s) ago'


@dataclass
class Story:
    id: int  # Item's unique id.
    by: str  # Username of item's author.
    score: int  # Item's score.
    time: int  # Creation date in Unix Time.
    title: str  # Item's title.
    type: str  # Type of story.
    descendants: Optional[int] = 0  # Total comments count
    url: Optional[str] = None  # URL of the Story.
    kids: Optional[list[int]] = None  # IDs of the item's comments.
    text: Optional[str] = None  # Ask's question content.
    parts: Optional[list[int]] = None  # Poll's options.

    def build_hn_url(self) -> None:
        if self.url is None:
            self.url = f'{HN_STORY_URL}{self.id}'

    def pretty_str(self) -> str:
        url_domain: str = ''
        if self.url:
            url_domain = urlparse(self.url).netloc
        else:
            self.build_hn_url()
            url_domain = urlparse(self.url).netloc

        pretty_id: str = f'[not bold dim white]{self.id}[/]'
        pretty_score: str = f'[bold white]↑{self.score}[/]'
        pretty_title: str = f'[not bold not italic white]"{self.title}"[/]'
        pretty_time: str = f'[not bold white]{prettify_time(self.time)}[/]'
        pretty_description: str = f'{pretty_time} by {self.by}'

        return f'[{pretty_id}] {pretty_score} {pretty_title} ([link={self.url}]{url_domain}[/link]) \n\t\t {pretty_description}'
