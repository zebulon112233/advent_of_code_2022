from math import ceil

def drawPositions():
    ropePieces = [ropeHead] + ropeTails
    for i in reversed(range(5)):
        s = ""
        for j in range(6):
            charToPrint = " . "
            for piece in ropePieces:
                if piece.position["x"] == j and piece.position["y"] == i:
                    charToPrint = piece.name
                    break
            s += charToPrint
        print(s)
    print("------------------------------------------")


class Tail:
    def __init__(self,name):
        self.name = name
        self.tail = None
        self.position = {"x": 0, "y" : 0}
        self.visitedPositions = [(self.position["x"],self.position["y"])]

    def attachTail(self,tail):
        self.tail = tail
    
    def alignTail(self):
        if self.tail.shouldMove(self.position):
            tailPosition = self.tail.calcNewPosition(self.position)
            self.tail.moveTo(tailPosition)
    
    
    def moveTo(self, position):
        self.position["x"], self.position["y"] = position
        self.visitedPositions.append(position)
        if self.tail:
            self.alignTail()

    def shouldMove(self,headPosition):
        tailX, tailY = self.position["x"], self.position["y"]
        headX, headY = headPosition["x"], headPosition["y"]
        dx , dy = tailX - headX, tailY - headY
        
        return not (abs(dx) <= 1 and abs(dy) <=1)

    def calcNewPosition(self, headPosition):
        if headPosition["x"] > self.position["x"]:
            newX = ceil((self.position["x"] + headPosition["x"]) / 2)
        else:
            newX = (self.position["x"] + headPosition["x"]) // 2
        if headPosition["y"] > self.position["y"]:
            newY = ceil((self.position["y"] + headPosition["y"]) / 2)
        else:
            newY = (self.position["y"] + headPosition["y"]) // 2
       
        return newX, newY
    
class Head:
    def __init__(self, name):
        self.name = name
        self.position = {"x": 0, "y" : 0}
        self.tail = None
    
    def alignTail(self):
        if self.tail.shouldMove(self.position):
            tailPosition = self.tail.calcNewPosition(self.position)
            self.tail.moveTo(tailPosition)
        
    def attachTail(self,tail):
        self.tail = tail
     
    def move(self,direction,amount):
        def moveUp():
            self.position["y"] += 1
        def moveDown():
            self.position["y"] -= 1
        def moveLeft():
            self.position["x"] -= 1
        def moveRight():
            self.position["x"] += 1
            
        moveInDirection = {
                "U": moveUp,
                "D": moveDown,
                "L": moveLeft,
                "R": moveRight
        }
        for _ in range(1, amount + 1):
            moveInDirection[direction]()
            self.alignTail()
           # drawPositions()

        
ropeTails = [Tail(str(i)) for i in range(1, 9 + 1)]
ropeHead = Head("H")
ropeHead.attachTail(ropeTails[0])

for (tailBefore, tailAfter) in zip(ropeTails, ropeTails[1:]):
    tailBefore.attachTail(tailAfter)

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip('\n')
        direction = rawLine.split(" ")[0]
        amount = rawLine.split(" ")[1]
        
        ropeHead.move(direction, int(amount))
        

print(len(set(ropeTails[-1].visitedPositions)))