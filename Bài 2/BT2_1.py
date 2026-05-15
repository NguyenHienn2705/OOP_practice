import math 

class Point:
    def __init__(self, x=0 , y=1):
        self.__x = x
        self.__y = y 
        
    def read(self):
        x,y = map(int , input().split())
        self.__x = x
        self.__y = y
        
    def print(self):
        print (f"({self.__x}, {self.__y})") 
    
    def move( self , dx ,dy):
        self.__x += dx
        self.__y += dy
        
    def getX(self):
        return self.__x 
    
    def getY(self):
        return self.__y
            
    def distance(self):
        return math.sqrt ( self.__x**2 + self.__y**2)
    def distanceTo(self , P):
        return math.sqrt((P.__x - self.__x)**2 + (P.__y - self.__y)**2)
    
class LineSegment: 
    def __init__ (self, *args):
        #default
        if len(args) == 0:
            self.__d1 = (8,5)
            self.__d2 = (1,0)
        #2 point
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]
        #4 ints
        elif len(args) == 4:
            x1, y1, x2, y2 = args
            self.__d1 = Point(x1, y1)
            self.__d2 = Point(x2, y2)
        #copy sau
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            s = args[0]
            self.__d1 = Point(s.__d1.getX(), s.__d1.getY())
            self.__d2 = Point(s.__d2.getX(), s.__d2.getY())
        else:
            self.__d1 = Point()
            self.__d2 = Point()
    #read
    def read(self):
        x1, y1, x2, y2 = map(int, input().split())
        self.__d1 = Point(x1, y1)
        self.__d2 = Point(x2, y2)
    #print
    def print(self):
        print (f"[({self.__d1.getX()}, {self.__d1.getY()}); ({self.__d2.getX()}, {self.__d2.getY()})]")
    #move
    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)
    #length
    def length(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()
        
        return math.sqrt(dx**2 + dy**2)
    #angle
    def angle(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()

        angle = math.degrees(math.atan2(dy, dx))
        angle = round(angle)

        if angle < 0:
            angle += 360
        return angle 

        
    