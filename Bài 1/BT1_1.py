import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
#read
    def read(self):
        x, y = map(int, input().split())
        self.__x = x
        self.__y = y
#print
    def print(self):
        print(f"({self.__x}, {self.__y})")
#move
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
#distance
    def distance(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)
#distance to Point
    def distanceTo(self, other):
        return math.sqrt((self.__x - other.getX()) ** 2 + (self.__y - other.getY()) ** 2)
