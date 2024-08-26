from enum import Enum

class Snake:
    def __init__(self):
        self.alive = True        
        self.tail = self.createTail()
        self.direction = Direction.NORTH
        
    def createTail(self):
        head = Body(1,1)
        b1 = Body(1,2, head)
        tail = Body(1,3, b1)
        return tail
    
    def tick(self):
        self.move(self.direction)
    
    def move(self, direction):
        if (direction == Direction.EAST):
            head = self.head()
            newHead = Body(head.x + 1, head.y)
            head.setHead(newHead)
            self.tail = self.tail.head

        if (direction == Direction.WEST):
            head = self.head()
            newHead = Body(head.x - 1, head.y)
            head.setHead(newHead)
            self.tail = self.tail.head
        
        if (direction == Direction.NORTH):
            head = self.head()
            newHead = Body(head.x, head.y - 1)
            head.setHead(newHead)
            self.tail = self.tail.head

        if (direction == Direction.SOUTH):
            head = self.head()
            newHead = Body(head.x, head.y + 1)
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

