import httpx

from app.config.config import settings


async def get_user(token: str):
    api_url = settings.validate_token_url
    async with httpx.AsyncClient() as client:
        response = await client.post(api_url, headers={"x-token": token})
        return response.json()