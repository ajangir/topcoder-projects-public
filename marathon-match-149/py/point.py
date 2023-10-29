from enum import Enum
class Point:

    def __init__(self, a: int = 0, b:int = 0):
        self.x = a
        self.y = b
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, a:int):
        self._x = int(a)
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,a:int):
        self._y = int(a)
    
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    def __lt__(self, other):
        return self.x < other.x if self.y == other.y else self.y < other.y
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    def __hash__(self) -> int:
        return hash(self.x + INF * self.y)
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Point(self.x - other.x, self.y - other.y)

dx = [1,0,0,-1]
dy = [0,1,-1,0]
INF = 999999

class cell(Enum):
    EMPTY, WATER, PLANT, SPRINKLER, PIPE = range(5)
