# When to use objects... Objects are used for things that have both data and behavior i.e...


import random


class Batter:
    def __init__(self, name, height, weight, battingAvg):
        self.name = name
        self.height = height
        self.weight = weight
        self.battingAvg = battingAvg

    def __repr__(self):
        return "<Batter {}>".format(self.name)

    def atBat(self):
        return random.randrange(0, 100) < self.battingAvg * 100

    def takeAtBats(self, atBats):
        hits = 0
        for i in range(atBats):
            if self.atBat():
                hits += 1
        average = hits/atBats
        print("{} had {} hits in {} at-bats, for a {} average".format(self.name, hits, atBats, average))

trout = Batter("Mike Trout", 74, 235, .301)
