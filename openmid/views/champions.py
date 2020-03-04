from django.http import JsonResponse
from django.core.serializers import serialize

from openmid.models import Summoner
from openmid.services import riot_ingest_service
from openmid.enums.league_constants import (
    Region, Tier, Division
)

def index(request):
    summoner_data = _crawl()
    s = summoner_data[0]

    print(s)

    summoner = Summoner.objects.create(
        summoner_id=s['id'],
        account_id=s['accountId'],
        puuid=s['puuid'],
        name=s['name'],
        profile_icon_id=s['profileIconId'],
        summoner_level=s['summonerLevel'],
        revision_date=s['revisionDate'],
    )

    return JsonResponse(s)


def _crawl():
    match_data = riot_ingest_service.fetch_ranked_matches(Region.KR, Tier.GRANDMASTER, Division.I)

    # get initial list of summoner Ids.
    summoner_ids = [match['summonerId'] for match in match_data]

    # api calls in a loop, yikes.
    # TODO: make this async
    summoners = []
    for summonerId in summoner_ids[0:1]:
        summoner = riot_ingest_service.fetch_summoners(Region.KR, summonerId)
        summoners.append(summoner)

    return summoners

