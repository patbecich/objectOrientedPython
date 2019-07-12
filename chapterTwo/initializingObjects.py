
import math


class Point:
    'Represents a point in two-dimensional geometric coordinates'

    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point, The x and y coordinates can
        be specified. If they are not, the point defaults to the origin'''
        # declare default values with "=" passed into arguments... x=0,y=0
        # this way there will not be an error if we fail to pass in starting
        # position
        self.move(x, y)

    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y

    def reset(self):
        'Reset the point back the origin: 0, 0'
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """ Calculate the distance from this point to a second
        point passed as a parameter. This function uses the
        pythagorean theorem, and returns a float."""
        return math.sqrt((self.x - other_point.x)**2 +
                         (self.y - other_point.y)**2)


# constructing a point

point = Point(3, 5)
print(point.x, point.y)
