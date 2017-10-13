import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://discordapp.com/api'


def run(token, servers_ids):
    for server_id in servers_ids:
        server_url = f'{BASE_URL}/v6/guilds/{server_id}'
        channel_url = server_url + '/channels'
        r = requests.get(channel_url, headers=headers(token))
        print(r.json())

def headers(token):
    return {'Authorization': 'Bot ' + token}