import channelbot
import config
import channel_names
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

channelbot.run(config.BOT_TOKEN, config.SERVERS, channel_names.NAMES)