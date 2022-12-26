from typing import List, Optional

from fastapi import APIRouter, Depends

from models.user_events import UserComment, UserFilmLike, Bookmark
from services.user_event_service import UserEventService, get_user_event_service

router = APIRouter()


@router.post("/comment")
async def user_comment(data: UserComment,
                       comment_post: UserEventService = Depends(get_user_event_service)):
    """
    Комментарий пользователя к фильму. Обязательные поля
    - **user_id**: UUID пользователя
    - **film_id**: UUID фильма
    - **comment**: Текст комментария
    """
    user_comment = await comment_post.post_comment(data)
    return user_comment


@router.get("/comment", response_model=Optional[UserComment])
async def user_comment(user_id, film_id, comment_get: UserEventService = Depends(get_user_event_service)):
    """
        Комментарий пользователя к фильму. Обязательные поля
        - **user_id**: UUID пользователя
        - **film_id**: UUID фильма
        """
    comment = await comment_get.get_comment(user_id, film_id)
    return comment


@router.delete("/comment")
async def user_comment(user_id, film_id, comment_get: UserEventService = Depends(get_user_event_service)):
    """
            Удаление комментария пользователя к фильму. Обязательные поля
            - **user_id**: UUID пользователя
            - **film_id**: UUID фильма
            """
    try:
        await comment_get.delete_comment(user_id, film_id)
        return "ok"
    except Exception as e:
        return "not ok"


@router.get("/likes", response_model=List[UserFilmLike])
async def get_user_like(film_id, get_like: UserEventService = Depends(get_user_event_service)):
    """
    Список лайков. Общий.
    - **film_id**: UUID фильма
    """
    get_user_like = await get_like.get_like_list(film_id)
    return get_user_like


@router.post("/like")
async def user_like(data: UserFilmLike,
                    like_post: UserEventService = Depends(get_user_event_service)):
    """
    Обновление лайка пользователя к фильму. Обязательные поля
    - **user_id**: UUID пользователя
    - **film_id**: UUID фильма
    - **like**: Bool значение. False или True
    """
    user_like = await like_post.post_like(data)
    return user_like


@router.post("/bookmark")
async def user_bookmark(data: Bookmark,
                        service: UserEventService = Depends(get_user_event_service)):
    """
    Закладка пользователя к фильму. Обязательные поля
    - **user_id**: UUID пользователя
    - **film_id**: UUID фильма
    """
    result = await service.post_bookmark(data)
    return result


@router.get("/is_bookmarked")
async def is_user_bookmarked(user_id, film_id, service: UserEventService = Depends(get_user_event_service)):
    """
    Существует ли закладка пользователя к фильму. Обязательные поля
    - **user_id**: UUID пользователя
    - **film_id**: UUID фильма
    """
    is_bookmarked = await service.is_bookmarked(Bookmark(user_id=user_id, film_id=film_id))
    return is_bookmarked


@router.delete("/bookmark")
async def user_comment(user_id, film_id, service: UserEventService = Depends(get_user_event_service)):
    """
        Удаление закладки пользователя к фильму. Обязательные поля
        - **user_id**: UUID пользователя
        - **film_id**: UUID фильма
        """
    result = await service.delete_bookmark(Bookmark(user_id=user_id, film_id=film_id))
    return result
