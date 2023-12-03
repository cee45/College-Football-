from configparser import ConfigParser

config = ConfigParser()
config.read('configs/cfb.ini')
cfb_key = config.get('main', 'cfb_key')

print(cfb_key)