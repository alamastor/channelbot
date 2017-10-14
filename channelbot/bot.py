import random
import time
import logging
import asyncio

from requests import HTTPError

from .server import Server


def run(token, servers_ids, channel_names, channel_count=10, wait_seconds=30):
    servers = [Server(server_id) for server_id in servers_ids]
    while True:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            do_naming(token, servers, channel_names, channel_count))
        time.sleep(wait_seconds - (time.time() - start_time))


async def do_naming(token, servers, channel_names, channel_count):
    for server in servers:
        try:
            voice_channels = list(
                filter(lambda c: c.type == 'voice', server.channels(token)))
            loop = asyncio.get_event_loop()
            futures = []
            for c in voice_channels:
                futures.append(
                    loop.run_in_executor(None, c.rename, token,
                                         random.choice(channel_names)))
            for _ in range(channel_count - len(list(voice_channels))):
                futures.append(
                    loop.run_in_executor(None, server.create_channel, token,
                                         random.choice(channel_names)))
            for response in await asyncio.gather(*futures):
                pass
        except HTTPError as e:
            logging.error(
                f'Request to server {server.id} failed with code {e.response.status_code}.'
            )