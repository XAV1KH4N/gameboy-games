from enum import Enum

class Snake:
    def __init__(self):
        self.tail = self.createTail()
        self.direction = Direction.EAST
        self.nextCoord = self.createMap()
    
    def createMap(self):
        return {
            Direction.NORTH: lambda x, y : (x, y - 1),
            Direction.EAST: lambda x,y : (x + 1, y), 
            Direction.SOUTH: lambda x,y : (x, y + 1), 
            Direction.WEST: lambda x,y : (x - 1, y)
        }
    
    def createTail(self):
        head = Body(1,1)
        body = Body(1,2, head)
        tail = Body(1,3, body)
        tail1 = Body(1,4, tail)
        tail2 = Body(1,5, tail1)
        tail3 = Body(1,6, tail2)
        return tail3
        
    def isCoordsTaken(self, x, y):
        body = self.tail
        while body != None:
            if (self.isBodyTaken(body, x, y)):
                return True
            body = body.head
        return False
    
    def isBodyTaken(self, body, x, y):
        return body.x == x and body.y == y 
        
    def nextMove(self, direction):
        f = self.nextCoord[direction]
        head = self.head()
        return f(head.x, head.y)
    
    def move(self, direction, feed):
        head = self.head()
        x, y = self.nextMove(direction)
        
        newHead = Body(x,y)
        head.setHead(newHead)
        
        if not feed: self.tail = self.tail.head
        self.direction = direction
        return x, y
    
    def head(self):
        body = self.tail
        while body != None:
            if (body.head == None):
                return body
            body = body.head
            
        return self.tail    
        
class Body:
    def __init__(self, x: int, y: int, head = None):
        self.x = x
        self.y = y        
        self.head: Body = head
        
    def setHead(self, head):
        self.head = head
        
    def size(self):
        size = 1
        body = self
        while body != None:
            body = body.head
            size += 1
        return size
    
class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def isCoordsMatch(self, x, y):
        return x == self.x and y == self.y
    
class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

