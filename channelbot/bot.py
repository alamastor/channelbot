import random
import time
import logging

from requests import HTTPError

from .server import Server


def run(token, servers_ids, channel_names, channel_count=10, wait_seconds=30):
    while True:
        start_time = time.time()
        for server_id in servers_ids:
            try:
                server = Server(server_id)
                voice_channels = list(
                    filter(lambda c: c.type == 'voice', server.channels(
                        token)))
                for c in voice_channels:
                    c.rename(token, random.choice(channel_names))
                for _ in range(channel_count - len(list(voice_channels))):
                    server.create_channel(token, random.choice(channel_names))
            except HTTPError as e:
                print(
                    f'Request to server {server.id} failed with code {e.response.status_code}.'
                )
        time.sleep(wait_seconds - (time.time() - start_time))
