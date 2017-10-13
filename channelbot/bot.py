from .server import Server

BASE_URL = 'https://discordapp.com/api'


def run(token, servers_ids):
    for server_id in servers_ids:
        server = Server(token, f'{BASE_URL}/v6/guilds/{server_id}')
        server.create_channel('hi al')
