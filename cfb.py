import pandas as pd
from configparser import ConfigParser
import requests 
import json
from pandas.io.json import json_normalize


config = ConfigParser()
config.read('configs/cfb.ini')
cfb_key = config.get('main', 'cfb_key')



base_url = 'https://api.collegefootballdata.com/teams/fbs'
params = {'year': 2023}


headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {cfb_key}'
}

response = requests.get(base_url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Request failed with status code:', response.status_code)


