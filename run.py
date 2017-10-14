import argparse
import logging

import channelbot
import config
import channel_names

logging.basicConfig(
    level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

parser = argparse.ArgumentParser()
parser.add_argument(
    '-f', '--frequency', type=int, default=30, help='name change frequency')
args = parser.parse_args()

channelbot.run(
    config.BOT_TOKEN,
    config.SERVERS,
    channel_names.NAMES,
    wait_seconds=args.frequency)
