from fastapi import APIRouter

router = APIRouter()


@router.get('/check')
async def user_film_rating():
    return True
