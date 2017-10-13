import requests

from .consts import API_URL
from .request import headers
from .channel import Channel


class Server:
    def __init__(self, id):
        self.id = id
        self.url = f'{API_URL}/guilds/{id}'

    def channels(self, token):
        r = requests.get(self.url + '/channels', headers=headers(token))
        r.raise_for_status()
        return [Channel(c['id'], c['name'], c['type']) for c in r.json()]


    def create_channel(self, token, name, channel_type='voice'):
        if channel_type == 'voice':
            c_type = 2
        elif channel_type == 'text':
            c_type = 0
            name = name.replace(' ', '-')
        else:
            raise TypeError('channel_type must be voice or text')

        r = requests.post(
            self.url + '/channels',
            json={'name': name,
                  'type': c_type},
            headers=headers(token))
        r.raise_for_status()