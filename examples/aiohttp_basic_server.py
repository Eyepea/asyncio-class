"""Basic http server with minimal setup"""
import aiohttp
import aiohttp.server

import asyncio
from urllib.parse import urlparse, parse_qsl
from aiohttp.multidict import MultiDict


class HttpRequestHandler(aiohttp.server.ServerHttpProtocol):

    @asyncio.coroutine
    def handle_request(self, message, payload):
        response = aiohttp.Response(
            self.writer, 200, http_version=message.version)
        content = "<h1>It Works!</h1>"
        bcontent = content.encode('utf-8')
        response.add_header('Content-Type', 'text/html; charset=UTF-8')
        response.add_header('Content-Length', str(len(bcontent)))
        response.send_headers()
        response.write(bcontent)
        yield from response.write_eof()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    f = loop.create_server(
        lambda: HttpRequestHandler(debug=True, keep_alive=75),
        '0.0.0.0', '8080')
    srv = loop.run_until_complete(f)
    print('serving on', srv.sockets[0].getsockname())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass