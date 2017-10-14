import logging

import requests

from .consts import API_URL
from .request import headers


class Channel:
    def __init__(self, id, name, channel_type):
        self.id = id
        self.name = name
        self.url = f'{API_URL}/channels/{id}'
        if channel_type == 0:
            self.type = 'text'
        elif channel_type == 2:
            self.type = 'voice'
        else:
            TypeError(f'Invalid channel type: {channel_type}')

    def __repr__(self):
        return f'<Channel - id: {self.id}, name: {self.name}>, type: {self.type}'

    def rename(self, token, name):
        logging.info(f'renaming chanel {self.name} to {name}')
        r = requests.patch(
            self.url, json={'name': name}, headers=headers(token))
        r.raise_for_status()

    def delete(self, token):
        logging.info(f'deleting chanel {self.name}')
        r = requests.delete(self.url, headers=headers(token))
        r.raise_for_status()