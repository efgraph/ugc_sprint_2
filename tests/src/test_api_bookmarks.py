import pytest


@pytest.mark.asyncio
async def test_add_bookmark(api_client, admin_tokens):
    response = await api_client.post(f"/api/v1/films/user-event/bookmark?jwt={admin_tokens[0]}",
                                     json={
                                         "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
                                         "film_id": "3fa85f64-5717-4562-b3fc-2c963f66afa2"
                                     })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_is_bookmarked(api_client, admin_tokens):
    response = await  api_client.get(
        f"/api/v1/films/user-event/is_bookmarked?jwt={admin_tokens[0]}&user_id=3fa85f64-5717-4562-b3fc-2c963f66afa2&film_id=3fa85f64-5717-4562-b3fc-2c963f66afa2")
    assert response.text == 'true'


@pytest.mark.asyncio
async def test_delete_bookmark(api_client, admin_tokens):
    response = await api_client.delete(f"/api/v1/films/user-event/bookmark?jwt={admin_tokens[0]}&user_id=3fa85f64-5717-4562-b3fc-2c963f66afa2&film_id=3fa85f64-5717-4562-b3fc-2c963f66afa2")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_is_not_bookmarked(api_client, admin_tokens):
    response = await  api_client.get(
        f"/api/v1/films/user-event/is_bookmarked?jwt={admin_tokens[0]}&user_id=3fa85f64-5717-4562-b3fc-2c963f66afa2&film_id=3fa85f64-5717-4562-b3fc-2c963f66afa2")
    assert response.text == 'false'
