import asyncio

import aiohttp

urls = ['http://coupang.com', 'http://google.co.kr', 'http://python.org']


async def call_url(url):
    print('Starting {}'.format(url))
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print('{} : {} bytes : {}'.format(url, len(data), data))
            return data


if __name__ == "__main__":
    futures = [call_url(url) for url in urls]
    print("call done")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
