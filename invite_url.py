import channelbot
import config

PERMISSIONS = 0x10
PERMISSION_URL = f'{channelbot.BASE_URL}/oauth2/authorize?client_id={config.CLIENT_ID}&scope=bot&permissions={PERMISSIONS}'
print(PERMISSION_URL)