from django.http import JsonResponse
from openmid.models.summoner import Summoner
from openmid.services import riot_ingest_service
from openmid.enums.league_constants import (
    Region, Tier, Division
)

def index(request):
    summoners = _crawl()

    data = {
        'foo': 'bar'
    }
    return JsonResponse(data)


def _crawl():
    match_data = riot_ingest_service.fetch_ranked_matches(Region.KR, Tier.GRANDMASTER, Division.I)

    # get initial list of summoner Ids.
    summoner_ids = [match['summonerId'] for match in match_data]

    # api calls in a loop, yikes.
    # TODO: make this async
    summoners = []
    for summonerId in summoner_ids[0:10]:
        summoner = riot_ingest_service.fetch_summoners(Region.KR, summonerId)
        summoners.append(summoner)

    return summoners

