from enum import Enum

class Snake:
    def __init__(self):
        self.alive = True        
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
        return tail
    
    def tick(self):
        self.move(self.direction)
        
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
    
    def move(self, direction):
        head = self.head()
        x, y = self.nextMove(direction)
        
        newHead = Body(x,y)
        head.setHead(newHead)
        
        self.tail = self.tail.head
        self.direction = direction
    
    def head(self):
        body = self.tail
        while body != None:
            if (body.head == None):
                return body
            body = body.head
            
        return self.tail
            
    
    def feed(self):
        self.length += 1
        
class Body:
    def __init__(self, x: int, y: int, head = None):
        self.x = x
        self.y = y        
        self.head: Body = head
        
    def setHead(self, head):
        self.head = head
    
class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

