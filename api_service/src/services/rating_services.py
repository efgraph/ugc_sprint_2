from functools import lru_cache

from aiokafka import AIOKafkaProducer
from db.kafka import get_kafka
from fastapi import Depends
from models.rating import UserFilmRating

from settings.config import settings


class RatingEventService:
    def __init__(self, storage: AIOKafkaProducer):
        self.storage = storage

    async def post_event(self, rating: UserFilmRating):
        await self.storage.send_and_wait(topic=settings.kafka_topic,
                                         key=f'{rating.user_id}+{rating.film_id}'.encode(),
                                         value=rating.json().encode())
        return {'message': 'ok'}


@lru_cache()
def get_rating_event_service(
        storage: AIOKafkaProducer = Depends(get_kafka)
) -> RatingEventService:
    return RatingEventService(storage)
