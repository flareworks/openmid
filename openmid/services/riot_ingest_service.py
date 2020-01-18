import requests
from enum import Enum

# Move to settings / environment variable. This dev API key expires after 24 hours.
RIOT_API_KEY = "RGAPI-7033ed72-f9a3-435f-96b1-019367567f41"
QUEUE = "RANKED_SOLO_5x5"

class Region(Enum):
    KR = 'KR'
    NA = 'NA1'
    EU = 'EUW1'

class Tier(Enum):
    CHALLENGER = 'CHALLENGER'
    GRANDMASTER = 'GRANDMASTER'
    MASTER = 'MASTER'
    DIAMOND = 'DIAMOND'
    PLATINUM = 'PLATINUM'
    GOLD = 'GOLD'

class Division(Enum):
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'

class RiotIngestService():

    @staticmethod
    def fetchRankedMatches(region: Region, tier: Tier, division: Division):
        endpoint = f'lol/league-exp/v4/entries/{QUEUE}/{tier.value}/{division.value}'
        return RiotIngestService._fetch(region.value, endpoint)

    @staticmethod
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
