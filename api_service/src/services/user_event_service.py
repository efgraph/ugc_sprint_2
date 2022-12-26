from functools import lru_cache

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient

from db.mongodb import get_mongo
from models.user_events import UserComment, UserFilmLike, Bookmark


class UserEventService:
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo

    async def is_bookmarked(self, bookmark: Bookmark):
        db = self.mongo.bookmarks
        bookmark = jsonable_encoder(bookmark)
        result = await db['bookmark'].find_one(
            {"user_id": bookmark['user_id'], "film_id": bookmark["film_id"]})
        return result is not None

    async def delete_bookmark(self, bookmark: Bookmark):
        db = self.mongo.bookmarks
        bookmark = jsonable_encoder(bookmark)
        await db['bookmark'].delete_one({"user_id": bookmark['user_id'], "film_id": bookmark["film_id"]})
        return "ok"

    async def post_bookmark(self, bookmark: Bookmark):
        db = self.mongo.bookmarks
        bookmark = jsonable_encoder(bookmark)
        await db['bookmark'].replace_one(
            {"user_id": bookmark['user_id'], "film_id": bookmark["film_id"]},
            bookmark,
            upsert=True
        )
        return "ok"

    async def post_comment(self, comment: UserComment):
        db = self.mongo.comments
        comment = jsonable_encoder(comment)
        await db['comment'].replace_one(
            {"user_id": comment['user_id'], "user_id": comment["film_id"]},
            comment,
            upsert=True
        )
        return "ok"

    async def get_comment(self, user_id, film_id):
        db = self.mongo.comments
        comment = await db['comment'].find_one({"user_id": user_id, "film_id": film_id}, {'_id': False})
        return None if comment is None or jsonable_encoder(comment)['user_id'] is None else jsonable_encoder(comment)

    async def delete_comment(self, user_id, film_id):
        db = self.mongo.comments
        await db['comment'].delete_one({"user_id": user_id, "film_id": film_id})
        return "ok"

    async def get_like_list(self, film_id):
        db = self.mongo.likes
        likes = await db['like'].find({"film_id": film_id, "like": True}).to_list(100)
        return likes

    async def post_like(self, like: UserFilmLike):
        db = self.mongo.likes
        like = jsonable_encoder(like)
        await db['like'].replace_one(
            {"user_id": like['user_id']},
            like,
            upsert=True)
        return "ok"

    async def delete_like(self, like: UserFilmLike):
        db = self.mongo.likes
        like = jsonable_encoder(like)
        await db['like'].delete_one({"user_id": like['user_id']})
        return "ok"


@lru_cache()
def get_user_event_service(
        mongo: AsyncIOMotorClient = Depends(get_mongo)
) -> UserEventService:
    return UserEventService(mongo)
