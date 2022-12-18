import asyncio
import os

import backoff
from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaConnectionError

from settings.config import settings


@backoff.on_exception(backoff.expo, KafkaConnectionError)
async def ping():
    consumer = AIOKafkaConsumer(
        'views',
        bootstrap_servers='{}:{}'.format(
            settings.kafka_host,
            settings.kafka_port
        ),
        group_id="test-group"
    )

    try:
        await consumer.start()
    except KafkaConnectionError as e:
        print(e)
        raise KafkaConnectionError()
    finally:
        await consumer.stop()


if __name__ == '__main__':
    asyncio.run(ping())
