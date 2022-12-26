import aiohttp
import uvicorn as uvicorn
from aiokafka import AIOKafkaProducer
from api.v1 import rating_api, user_event_api, health_check
from db import mongodb, kafka
from fastapi import FastAPI, Request, Response
from fastapi.responses import ORJSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from settings.config import settings
from http import HTTPStatus

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    mongodb.mongo = AsyncIOMotorClient('mongodb://db-mongo:27017')
    kafka.producer = AIOKafkaProducer(bootstrap_servers=[f'{settings.kafka_host}:{settings.kafka_port}'])
    await kafka.producer.start()


@app.on_event('shutdown')
async def shutdown():
    await kafka.producer.stop()
    await mongodb.mongo.stop()


app.include_router(rating_api.router, prefix='/api/v1/events/rating', tags=['rating_event'])
app.include_router(user_event_api.router, prefix='/api/v1/films/user-event', tags=['user_events'])
app.include_router(health_check.router, prefix='/api/v1/health', tags=['health_check'])



# Проверяет Auth сервис. Обращается по адресу.
@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    if "api/openapi" in request.url.path or "health" in request.url.path:
        response = await call_next(request)
        return response
    headers = request.headers
    params = request.query_params
    auth_url = 'http://auth:5000/v1/auth/usercheck'
    auth_check = await check_user(auth_url, headers, params)

    if auth_check.status == HTTPStatus.OK:
        response = await call_next(request)
        return response
    return Response(status_code=HTTPStatus.UNAUTHORIZED)


async def check_user(url, headers, params):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url, params=params) as response:
            return response


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000
    )
