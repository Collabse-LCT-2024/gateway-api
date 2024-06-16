import uuid
from typing import Annotated

from fastapi import APIRouter, Depends
from src.core.config import settings
from src.models.uploaded import UploadedEvent
from src.schemas.uploaded import UploadedEventSchema
from src.services.base import MessageServiceABC
from src.schemas.account import Account
from src.services.bearer import security_jwt


router = APIRouter()


@router.post(
    "/index",
    summary="Отправить событие о добавлении видео",
    description="Отправка события в брокер сообщений",
    tags=["События"],
)
async def send_video_event(
    uploaded_event: UploadedEventSchema,
    message_service: MessageServiceABC = Depends(),
    account: Annotated[Account, Depends(security_jwt)] = None
) -> None:
    video_id = uuid.uuid4()

    await message_service.send_message(
        topic=settings.kafka_video_processing_requests_topic,
        message=UploadedEvent(
            **uploaded_event.model_dump(),
            account_id=account.id if account else None,
            video_id=video_id
        )
    )
    await message_service.send_message(
        topic=settings.kafka_audio_processing_requests_topic,
        message=UploadedEvent(
            **uploaded_event.model_dump(),
            account_id=account.id if account else None,
            video_id=video_id
        )
    )
    await message_service.send_message(
        topic=settings.kafka_tags_processing_requests_topic,
        message=UploadedEvent(
            **uploaded_event.model_dump(),
            account_id=account.id if account else None,
            video_id=video_id
        )
    )
