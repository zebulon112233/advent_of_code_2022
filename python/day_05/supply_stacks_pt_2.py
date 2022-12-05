

isReadingBoxes = True
numberOfStacks = 9
stacks = [[] for i in range(numberOfStacks)]

def readBoxesFromLine(line):
    lineArr = line.split(" ")
    emptySpaceCount = 0
    readBoxesCount = 0
    
    for elem in lineArr:
        if elem == "":
            emptySpaceCount += 1
        else:
            stacks[readBoxesCount + emptySpaceCount // 4].append(elem)
            readBoxesCount += 1
def readCommand(line):
    lineArr = line.split(" ")
    return [int(str) for str in lineArr if str.isnumeric()]
    
def reverseStacks():
    for stack in stacks:
        stack.reverse()
        
def readNextLine(f):
    line = f.readline()
    return line.strip()

def executeCommand(command):
    numberOfCrates, fromStack, toStack = command
    cratesBeingMoved = []
    for _ in range(numberOfCrates):
        currentCrate = stacks[fromStack -1].pop()
        cratesBeingMoved.append(currentCrate)
    for _ in range(numberOfCrates):
        currentCrate = cratesBeingMoved.pop()
        stacks[toStack -1].append(currentCrate)
        
with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip('\n')
        isFinishedWithReadingBoxes = len(rawLine) > 1 and rawLine[1] == '1'
        
        if(isFinishedWithReadingBoxes):
            isReadingBoxes = False
            reverseStacks()
            rawLine = readNextLine(f)
            rawLine = readNextLine(f)
            # for stack in stacks:
            #     print(stack)

        if isReadingBoxes:
            readBoxesFromLine(rawLine)
        else:
            command = readCommand(rawLine)
            executeCommand(command)

topCrates = [stack.pop() for stack in stacks if len(stack) > 0]
messageToElves = ''.join([crate[1] for crate in topCrates])
print(messageToElves)


        
