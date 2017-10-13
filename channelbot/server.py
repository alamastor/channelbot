import requests


class Server:
    def __init__(self, token, url):
        self.token = token
        self.url = url

    @property
    def channels(self):
        r = requests.get(self.url + '/channels', headers=self.__headers__)
        return r.json()

    def create_channel(self, name, channel_type='voice'):
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
            headers=self.__headers__)
        print(r.json())

    @property
    def __headers__(self):
        return {'Authorization': 'Bot ' + self.token}