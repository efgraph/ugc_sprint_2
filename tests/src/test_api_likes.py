import json

import pytest


@pytest.mark.asyncio
async def test_add_like(api_client, admin_tokens):
    response = await api_client.post(f"/api/v1/films/user-event/like?jwt={admin_tokens[0]}",
                                     json={
                                         "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
                                         "film_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
                                         "like": True
                                     })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_likes(api_client, admin_tokens):
    response = await  api_client.get(
        f"/api/v1/films/user-event/likes?jwt={admin_tokens[0]}&film_id=3fa85f64-5717-4562-b3fc-2c963f66afa2")
    result = json.loads(response.text)
    assert len(result) == 1


@pytest.mark.asyncio
async def test_delete_like(api_client, admin_tokens):
    response = await api_client.post(f"/api/v1/films/user-event/like?jwt={admin_tokens[0]}",
                                     json={
                                         "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
                                         "film_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
                                         "like": False
                                     })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_check_if_empty(api_client, admin_tokens):
    response = await  api_client.get(
        f"/api/v1/films/user-event/likes?jwt={admin_tokens[0]}&film_id=3fa85f64-5717-4562-b3fc-2c963f66afa2")
    result = json.loads(response.text)
    assert len(result) == 0
