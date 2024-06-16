from src.schemas.base import BaseEventSchema


class UploadedEventSchema(BaseEventSchema):
    video_url: str | None = None
    video_desc: str | None = None
