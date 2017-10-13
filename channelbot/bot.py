import random

from requests import HTTPError

from .server import Server


def run(token, servers_ids, channel_names):
    for server_id in servers_ids:
        try:
            server = Server(server_id)
            voice_channels = filter(lambda c: c.type == 'voice', server.channels(token))
            for c in voice_channels:
                c.rename(token, random.choice(channel_names))
        except HTTPError as e:
            print(f'Request to server {server.id} fail with code {e.response.status_code}.')
