from asyncio import run
from wottle import Wottle


async def main():
    city = Wottle("token") # You can get on: https://openweathermap.org/api.
    weather = await city.get_weather("Москва")

    print(weather)


if __name__ == "__main__":
    run(main())