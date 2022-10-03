from dataclasses import dataclass
from typing import Optional


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

    def __str__(self) -> str:
        return f'[{self.type}] ↑{self.score} - {self.title} by {self.by}\n↪ {self.url}'
