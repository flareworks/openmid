from django.db import models

# https://developer.riotgames.com/apis#summoner-v4/GET_getByAccountId
class Summoner(models.Model):

        profileIconId = models.IntegerField
        name = models.CharField(max_length=16)
        puuid = models.CharField(max_length=78)
        summonerLevel = models.IntegerField
        revisionDate = models.IntegerField # Date summoner was last modified specified as epoch milliseconds.
        summonerId = models.CharField(max_length=63) # alias `id`
        accountId = models.CharField(max_length=56)
