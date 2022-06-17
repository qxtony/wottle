<h1 align="center" name="name">Wottle</h1>
<p align="center">
    <em>
        Asynchronous library for getting the weather forecast in the desired city.
    </em>
</p>

<p align="center">
    <a href="https://github.com/qxtony/wottle/issues">
        <img src="https://img.shields.io/github/issues/qxtony/wottle" alt="Issues">
    </a>
    <a href="https://pypi.org/project/wottle/">
        <img src="https://img.shields.io/pypi/v/wottle?colorB=brightgreen" alt="Package version">
    </a>
    <a href="https://github.com/qxtony/wottle/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/qxtony/wottle.svg" alt="License">
    </a>
</p>

## Installation

Stable version:

```bash
pip install -U wottle
```
## Quickstart

The first program to get a weather forecast:
```python
from asyncio import run
from wottle import Wottle


async def main():
    city = Wottle("token") # You can get on: https://openweathermap.org/api.
    weather = await city.get_weather("Москва")

    print(weather)


if __name__ == "__main__":
    run(main())
```
