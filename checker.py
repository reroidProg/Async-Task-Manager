import asyncio
import httpx

class PingChecker:
    def __init__(self) -> None:
        self.client = httpx.AsyncClient()

    async def ping(self, url) -> list:
        try:
            response = await self.client.get(url)
            elapsed = int(response.elapsed.total_seconds() * 1000)
            status = response.status_code
            ok = status < 400
            return [url, elapsed, status, ok]
        except httpx.ConnectTimeout:
            print(f"Нет доступа к {url}...")
            return []
        except httpx.UnsupportedProtocol:
            print(f"Неверный формат URL: {url}...")
            return []
        except Exception:
            print(f"Ошибка при запросе {url}...")
            return []
