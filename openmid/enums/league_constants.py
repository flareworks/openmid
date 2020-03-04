from enum import Enum

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
