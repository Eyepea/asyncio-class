#!/usr/bin/env python3

import aiohttp
import sys
import asyncio

@asyncio.coroutine
def curl(url):
    response = yield from aiohttp.request('GET', url)
    print(repr(response))

    chunk = yield from response.content.read()
    print('Downloaded: %s' % len(chunk))

    response.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(curl(sys.argv[1]))