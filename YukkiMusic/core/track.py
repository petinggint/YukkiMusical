import asyncio
import os
import re
from dataclasses import dataclass

from yt_dlp import YoutubeDL

from config import YTDOWNLOADER, cookies
from YukkiMusic.utils.database import is_on_off
from YukkiMusic.utils.decorators import asyncify

from .enum import SourceType

__all__ = ["Track"]


@dataclass
class Track:
    title: str
    link: str
    duration: int  # duration in seconds
    streamtype: SourceType
    video: bool
    track_id: str
    thumb: str

    is_live: bool | None = None
    file_path: str | None = None

    def __post_init__(self):
        if (
            not self.duration and self.is_live is None
        ):  # WHEN is_live is not None it means no need to check it
            if self.streamtype in [
                SourceType.APPLE,
                SourceType.RESSO,
                SourceType.SPOTIFY,
                SourceType.YOUTUBE,
            ]: # this all platform rely on YouTube
                self.is_live = True

    async def __call__(self):
        return self.file_path or await self.download()

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def is_youtube_stream(self) -> bool:
        return "youtube.com" in self.download_url or "youtu.be" in self.download_url

    async def download(
        self,
    ):
        raise NotImplementedError("This method should be overridden by the platform.")