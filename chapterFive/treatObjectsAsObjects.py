# When to use objects... Objects are used for things that have both data and
# behavior i.e...


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
        print("{} had {} hits in {} at-bats, for a {} average".format(
            self.name, hits, atBats, average))


trout = Batter("Mike Trout", 74, 235, .301)

# when only working with data, better to use a list, set, dictionary...

rainfall = [10, 11, 11, 15]

# when only working with behavior, better to use a simple function...


def addOne(n):
    return n + 1

# use built in data-structures and methods until there is an explicit need to
# define a new one

# Start with built in data-structures

import math

square = [(1,1), (1,2), (2,2), (2,1)]


def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter

# should a class be used to encapsulate polygons? Would this be valuable?

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)

class Polygon:
    # def __init__(self):
    #     self.vertices = []

    def __init__(self, points=None):
        points = points if points else []
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter

# the object oriented version is not shorted here, but is easier to understand
# short code is not always better... prioritize readability over extreme conciseness

#"Don't use an object just because you can, but don't hesitate to create a class
# when you need a class"
