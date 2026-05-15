import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        self.__x, self.__y = map(int, input().split())

    def print(self):
        print(f"({self.__x}, {self.__y})", end="")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, other=None):
        if other is None:
            return math.sqrt(self.__x ** 2 + self.__y ** 2)
        return math.sqrt((self.__x - other.getX()) ** 2 + (self.__y - other.getY()) ** 2)


class ColorPoint(Point):
    def __init__(self, *args):

        # ColorPoint()
        if len(args) == 0:
            super().__init__()
            self.color = "xanh"

        # ColorPoint(x, y, color)
        elif len(args) == 3:
            x, y, color = args
            super().__init__(x, y)
            self.color = color

        # ColorPoint(cp)
        elif len(args) == 1 and isinstance(args[0], ColorPoint):
            cp = args[0]
            super().__init__(cp.getX(), cp.getY())
            self.color = cp.color

    def read(self):
        data = input().split()
        self.setXY(int(data[0]), int(data[1]))
        self.color = data[2]

    def print(self):
        super().print()
        print(f": {self.color}")

    def setColor(self, color):
        self.color = color