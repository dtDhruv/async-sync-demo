from httpx import AsyncClient
import time
import asyncio

cities = [
    "Mumbai",
    "New York",
    "London",
    "Paris",
    "Tokyo",
    "Dubai",
    "Singapore",
    "Hong Kong",
    "Rome",
    "Barcelona",
    "Sydney",
    "Los Angeles",
    "Moscow",
    "Berlin",
    "Toronto",
    "Bangkok",
    "Istanbul",
    "Beijing",
    "San Francisco",
    "Cairo",
]


async def get_weather(city: str, async_client: AsyncClient):
    r = await async_client.get(f"https://wttr.in/{city}?format=j1")
    weather = r.json()
    temperature = weather["current_condition"][0]["temp_C"]
    print(f"The current temperature in {city} is {temperature}°C")


async def main():
    tasks = []
    start = time.time()
    async with AsyncClient() as async_client:
        for city in cities:
            tasks.append(get_weather(city, async_client))
        await asyncio.gather(*tasks)
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
