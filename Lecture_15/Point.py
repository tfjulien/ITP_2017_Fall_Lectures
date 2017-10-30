import math


class Point:
    print('something')
    const = 'asdasd'


    def __init__(self, x, y):
        print('creating new point')
        self.x = x
        self.y = y

    # def distance(self, point2=Point(0, 0)):
    #     diff_x = self.x - point2.x
    #     diff_y = self.y - point2.y
    #     return ((diff_x) ** 2 + (diff_y) ** 2) ** (1 / 2)

    def translate(self, tx, ty):
        self.x += tx
        self.y += ty
        return True

    def scale(self, sx, sy):
        self.x *= sx
        self.y *= sy

    def rotation(self, radians):
        new_x = self.x * math.cos(radians) + self.y * math.sin(radians)
        new_y = -self.x * math.sin(radians) + self.y * math.cos(radians)
        self.x = new_x
        self.y = new_y

    def __str__(self):
        return 'x: {}, y: {}'.format(self.x, self.y)

    def __add__(self, other):
        tx = self.x + other.x
        ty = self.y + other.y
        return Point(tx, ty)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


    @staticmethod
    def distance_between_points(pa, pb):
        return pa.distance(pb)


if __name__ == '__main__':
    pointA = Point(1, 0)
    pointB = Point(0, 1)
    pointC = pointA + pointB
    pointA += pointC
    print(pointA)
    print(pointC)