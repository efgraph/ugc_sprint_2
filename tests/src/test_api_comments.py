import json

import pytest


@pytest.mark.asyncio
async def test_add_comment(api_client, admin_tokens):
    response = await api_client.post(f"/api/v1/films/user-event/comment?jwt={admin_tokens[0]}",
                                     json={
                                         "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
                                         "film_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
                                         "comment": "Hello"
                                     })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_comment(api_client, admin_tokens):
    response = await api_client.get(
        f"/api/v1/films/user-event/comment?jwt={admin_tokens[0]}&film_id=3fa85f64-5717-4562-b3fc-2c963f66afa2&user_id=3fa85f64-5717-4562-b3fc-2c963f66afa2")
    result = json.loads(response.text)
    assert result["comment"] == "Hello"


@pytest.mark.asyncio
async def test_update_comment(api_client, admin_tokens):
    response = await api_client.post(f"/api/v1/films/user-event/comment?jwt={admin_tokens[0]}",
                                     json={
                                         "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
                                         "film_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
                                         "comment": "Hello World"
                                     })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_updated_comment(api_client, admin_tokens):
    response = await api_client.get(
        f"/api/v1/films/user-event/comment?jwt={admin_tokens[0]}&film_id=3fa85f64-5717-4562-b3fc-2c963f66afa2&user_id=3fa85f64-5717-4562-b3fc-2c963f66afa2")
    result = json.loads(response.text)
    assert result["comment"] == "Hello World"


@pytest.mark.asyncio
async def test_delete_comment(api_client, admin_tokens):
    response = await api_client.delete(
        f"/api/v1/films/user-event/comment?jwt={admin_tokens[0]}&film_id=3fa85f64-5717-4562-b3fc-2c963f66afa2&user_id=3fa85f64-5717-4562-b3fc-2c963f66afa2")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_comment_deleted(api_client, admin_tokens):
    response = await api_client.get(
        f"/api/v1/films/user-event/comment?jwt={admin_tokens[0]}&film_id=3fa85f64-5717-4562-b3fc-2c963f66afa2&user_id=3fa85f64-5717-4562-b3fc-2c963f66afa2")
    assert response.text == 'null'
