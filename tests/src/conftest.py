import json

import httpx
import pytest_asyncio
from httpx import AsyncClient


@pytest_asyncio.fixture
async def api_client() -> AsyncClient:
    async with httpx.AsyncClient(
            base_url="http://api:8000",
            headers={"Content-Type": "application/json"},
    ) as client:
        yield client


@pytest_asyncio.fixture
async def auth_client() -> AsyncClient:
    async with httpx.AsyncClient(
            base_url="http://auth:5000",
            headers={"accept": "application/json"},
    ) as client:
        yield client


@pytest_asyncio.fixture
async def admin_tokens(auth_client):
    response = await auth_client.post('/v1/auth/login?login=admin&password=admin')
    res = json.loads(response.text)
    return res['access_token'], res['refresh_token']
