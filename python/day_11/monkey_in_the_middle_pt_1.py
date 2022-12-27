def readNextLine():
    line = f.readline()
    return line.strip('\n')

def readMonkeyData(firstLine):
    def readID(fromLine):
        return int(fromLine.split(" ")[-1][0])

    def readItems():
        itemsStrList = readNextLine().split("items: ")[-1].split(", ")
        items = list(map(int, itemsStrList))
        return items

    def readOperation():
        operationData = readNextLine().split(" ")
        operator = operationData[-2]
        value = operationData[-1]
        
        def operation(old):
            if operator == "+":
                if value.isnumeric():
                    new = old + int(value)
                else:
                    new = old + old
                    
            elif operator == "*":
                if value.isnumeric():
                    new = old * int(value)
                else:
                    new = old * old
            return new 
            
        return operation
    
    def readTest():
        modulo = int(readNextLine().split(" ")[-1])
        throwToWhenTrue = int(readNextLine().split(" ")[-1])
        throwToWhenFalse = int(readNextLine().split(" ")[-1])
        return {"modulo": modulo, "throwToWhenTrue" : throwToWhenTrue, "throwToWhenFalse": throwToWhenFalse}
 
    ID = readID(firstLine)
    items = readItems()
    operation = readOperation()
    test = readTest()

    readNextLine() # read empty line
    
    return ID, items, operation, test

def find(pred, iterable):
  
  return next(filter(pred, iterable), None)

class Monkey():
    
    collection = []
    
    def __init__(self,data):
        (ID, items, operation, test) = data
        self.ID = ID
        self.items = items
        self.operation = operation
        self.test = test
        self.allMonkeys = None
        self.inspectItemCount = 0
        
    def __str__(self):
        return f'Monkey ID: {self.ID}, items: {self.items}'
    
    def setAllMonkeys(self,monkeys):
        self.allMonkeys = monkeys
        
    def reduceWorryLevel(self, worryLevel):
        return worryLevel // 3
    
    def whereToThrowItem(self,worryLevel):
        if worryLevel % self.test["modulo"] == 0:
            return self.test["throwToWhenTrue"]
        else:
            return self.test["throwToWhenFalse"]
        
    def inspectItem(self):
        self.inspectItemCount += 1
        currentItemWorryLevel = self.items.pop(0)
        currentItemWorryLevel = self.operation(currentItemWorryLevel)
        currentItemWorryLevel = self.reduceWorryLevel(currentItemWorryLevel)
        monkeyID = self.whereToThrowItem(currentItemWorryLevel)
        self.throwItemToMonkey(currentItemWorryLevel,monkeyID)
        
    def throwItemToMonkey(self,item, monkeyID):
        receiverMonkey = find(lambda monkey: monkey.ID == monkeyID, Monkey.collection)
        receiverMonkey.items.append(item)
    
    def takeTurn(self):
        while self.items:
            self.inspectItem()
            
        

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip('\n')

        monkey = Monkey(readMonkeyData(rawLine))
        Monkey.collection.append(monkey)

def takeRound():
    for monkey in Monkey.collection:
        #print(monkey.items)
        monkey.takeTurn()
        
        
totalRounds = 20

def printInspectItemCounts():
    inspectItemCountList = []

    for monkey in Monkey.collection:
        print(monkey)
        inspectItemCountList.append(monkey.inspectItemCount)

    print(inspectItemCountList)
    
for _ in range(totalRounds):
    takeRound()
    printInspectItemCounts()
    
inspectItemCountList = []

for monkey in Monkey.collection:

    inspectItemCountList.append(monkey.inspectItemCount)
    
mostActive, secondMostActive = sorted(inspectItemCountList)[-2:]
monkeyBusinessLevel = mostActive * secondMostActive
print(monkeyBusinessLevel)
