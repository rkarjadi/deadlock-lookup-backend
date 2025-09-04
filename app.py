import os
import json
import requests

from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")

@app.route('/get_heroes')
def get_heroes():
    url = "https://assets.deadlock-api.com/v2/heroes"
    headers = {'x-api-key': API_KEY}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        return data
    
    else:
        print(f"HTTP Error: {r.status_code}") 

@app.route('/get_player_data/<account_id>')
def get_player_data(account_id):
    url = f"https://api.deadlock-api.com/v1/players/{account_id}/steam"
    headers = {'x-api-key': API_KEY}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        return data
        
    else:
        print(f"HTTP Error: {r.status_code}")

@app.route('/get_player_hero_stats/<account_id>')
def get_player_hero_stats(account_id):
    url = "https://api.deadlock-api.com/v1/players/hero-stats"
    headers = {'x-api-key': API_KEY}
    params = {
        "account_ids": [account_id]
    }

    r = requests.get(url, headers=headers, params=params)

    if r.status_code == 200:
        data = r.json()
        return data
        
    else:
        print(f"HTTP Error: {r.status_code}")

@app.route('/get_player_match_history/<account_id>')
def get_player_match_history(account_id):
    url = f"https://api.deadlock-api.com/v1/players/{account_id}/match-history"
    headers = {'x-api-key': API_KEY}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        return data
    
    else:
        print(f"HTTP Error: {r.status_code}")

@app.route('/get_player_mmr/<account_id>')
def get_player_mmr(account_id):
    url = f"https://api.deadlock-api.com/v1/players/mmr"
    params = {
        "account_ids": account_id
    }
    r = requests.get(url, params=params)

    if r.status_code == 200:
        data = r.json()
        return data
        
    else:
        print(f"HTTP Error: {r.status_code}")     

if __name__ == '__main__':
    app.run()