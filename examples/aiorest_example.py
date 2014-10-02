import asyncio
import aiohttp
import aiorest


# define a simple request handler
# which accept no arguments
# and responds with json
def hello(request):
    return {'hello': 'world'}


loop = asyncio.get_event_loop()
server = aiorest.RESTServer(hostname='127.0.0.1',
                            loop=loop)

# configure routes
server.add_url('GET', '/', hello)
# create server
srv = loop.run_until_complete(loop.create_server(
    server.make_handler, '127.0.0.1', 8080))

loop.run_forever()