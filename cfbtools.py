import pandas as pd
from configparser import ConfigParser
import requests 
import json
from pandas.io.json import json_normalize


config = ConfigParser()
config.read('configs/cfb.ini')
cfb_key = config.get('main', 'cfb_key')


def get_team_info(conference=None):
    '''
    , classification=None
        Returns a DataFrame containing color, logo, and mascot info
        about each team in the queried params

        conference (optional) = queries by conference
    '''
    base_url = 'https://api.collegefootballdata.com/teams/fbs'
    payload = {}


    if conference is not None:
        payload['conference'] = conference
    
    headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {cfb_key}'
    }

    r = requests.get(base_url, params=payload, headers=headers)
    if r.status_code == 200:
        df = pd.DataFrame(r.json())
        filtered_df = df[['id', 'school', 'abbreviation', 'conference']]
        return filtered_df
    
    else:
        raise Exception('Request failed with status code: '+str(r.status_code))
    

def get_conference_list():
    '''
        Returns a DataFrame containing a list of conferences and their full
        names
    '''
    base_url = 'https://api.collegefootballdata.com/conferences'
    payload = {}
    
    headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {cfb_key}'
    }
    
    r = requests.get(base_url, params=payload, headers=headers)
    if r.status_code == 200:
        return pd.DataFrame(r.json())
    else:
        raise Exception('Request failed with status code: '+str(r.status_code))
    






