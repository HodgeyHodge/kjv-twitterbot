import random
import configparser
from dataclasses import dataclass
import tweepy


class Config():
    def __init__(self, path='Twitterbot/config/config.cfg'):
        config = configparser.ConfigParser()
        config.read(path)
        
        icons = [i.split(',') for i in config['assets']['icons'].split()]
        self.icons = [Icon(i[0], int(i[1]), int(i[2])) for i in icons]
        
        self.fonts = config['assets']['fonts'].split()

        colour = dict(config['colour'])
        self.dark = int(colour['dark'])
        self.light = int(colour['light'])

        api_keys = dict(config['apikeys'])
        auth = tweepy.OAuthHandler(api_keys['consumer_key'], api_keys['consumer_secret'])
        auth.set_access_token(api_keys['access_key'], api_keys['access_secret'])
        self.api_context = tweepy.API(auth)

@dataclass
class Icon:
    Filename: str
    Width: int
    Height: int