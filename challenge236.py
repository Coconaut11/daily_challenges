import math

class Vector2f:
    def __main__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        dx = self.x - other.y
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

vertex = [Vector2f(0, -2), Vector2f(2, 1), Vector2f(-2, 1)]

class Polygon:
    def __main__(self, vertex):
        self.vertex

    def check_point(self, p):
        pass