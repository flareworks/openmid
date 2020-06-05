import requests
from openmid.enums.league_constants import (
    Region, Tier, Division
)

# Move to settings / environment variable. This dev API key expires after 24 hours.
# Refresh API key at https://developer.riotgames.com/
RIOT_API_KEY = "RGAPI-80210f6a-1a50-40db-9a44-ea69eed81bd4"
QUEUE = "RANKED_SOLO_5x5"


def fetch_ranked_matches(region: Region, tier: Tier, division: Division):
    endpoint = f'lol/league-exp/v4/entries/{QUEUE}/{tier.value}/{division.value}'
    return _fetch(region.value, endpoint)


def fetch_summoners(region: Region, summoner_id: str):
    # fetch by encrypted summoner ID
    endpoint = f'lol/summoner/v4/summoners/{summoner_id}'
    return _fetch(region.value, endpoint)


def _fetch(region: str, endpoint: str):
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Language": "en-US,en;q=0.9",
        "X-Riot-Token": RIOT_API_KEY,
    }
    url = f'https://{region}.api.riotgames.com/{endpoint}'

    print(f'Fetching with key: {RIOT_API_KEY}')
    print(f'url: {url}')

    r = requests.get(url, headers=headers)
    return r.json()
