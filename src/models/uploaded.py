from src.models.base import BaseEvent


class UploadedEvent(BaseEvent):
    video_url: str | None = None
    video_desc: str | None = None