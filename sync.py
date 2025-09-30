import httpx
import time

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


def get_weather(city: str):
    r = httpx.get(f"https://wttr.in/{city}?format=j1")
    weather = r.json()
    temperature = weather["current_condition"][0]["temp_C"]
    print(f"The current temperature in {city} is {temperature}°C")


def main():
    start = time.time()
    for city in cities:
        get_weather(city)
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()
