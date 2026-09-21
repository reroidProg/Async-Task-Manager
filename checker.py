import asyncio
import httpx

class PingChecker:
    def __init__(self) -> None:
        self.client = httpx.AsyncClient()

    async def ping(self, url) -> list:
        try:
            response = await self.client.get(url)

            data = [int(response.elapsed.total_seconds() * 1000), response.status_code]
            return data
        except httpx.ConnectTimeout:
            print("Нет доступа...")
            return []
        except httpx.UnsupportedProtocol:
            print("Неверный формат...")
            return []
        self.client.aclose()
