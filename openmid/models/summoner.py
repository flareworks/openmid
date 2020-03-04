from django.db import models

# https://developer.riotgames.com/apis#summoner-v4/GET_getByAccountId
class Summoner(models.Model):

        profile_icon_id = models.BigIntegerField()
        name = models.CharField(max_length=16)
        puuid = models.CharField(max_length=78)
        summoner_level = models.BigIntegerField()
        revision_date = models.BigIntegerField() # Date summoner was last modified specified as epoch milliseconds.
        summoner_id = models.CharField(max_length=63) # alias `id`
        account_id = models.CharField(max_length=56)
