
directories = []
currentDirectories = []
currentPathParts = []
currentDirectory = {}

def isCommand(line):
    return line[0] == '$'

def getCurrentPath():
    return currentPathParts[0] + "/".join(currentPathParts[1:])

def createDirectory(dir):
       return {"path": dir["path"], "size": dir["size"]}
 
def listFiles():
    return

def isCurrentDirectoryIn(dirs):
    if not dirs:
        return False
    dirNames = map(lambda x : x["path"], dirs)
    
    if currentDirectory["path"] not in dirNames:
        return False
    
    return True

def changeDirectory(command):
    dirName = command[2]
    
    handleCurrentDirectory()


    if dirName == "..":
        currentPathParts.pop()
        directories.append(currentDirectories.pop())
    else:
        currentPathParts.append(dirName)
        
        ### Initialize new directory
        currentDirectory["path"] = getCurrentPath()
        currentDirectory["size"] = 0
    

def processDirectoryContent(line):
    lineParts = line.split(" ")
    if lineParts[0] != "dir":
        fileSize = lineParts[0]
        currentDirectory["size"] += int(fileSize)
        
def addCurrentDirectorySizeTo(dirs):
    for dir in dirs:
            dir["size"] += currentDirectory["size"]

def handleCurrentDirectory():
    if currentDirectory and not isCurrentDirectoryIn(directories):
        
        currentDirectories.append(createDirectory(currentDirectory)) 
        
        addCurrentDirectorySizeTo(currentDirectories[:-1])
    
with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip('\n')
        
        if isCommand(rawLine):
            command = rawLine.split(" ")
            commandName = command[1]

            if commandName == "cd":
                changeDirectory(command)
            else:
                listFiles()
        else:
            processDirectoryContent(rawLine)


handleCurrentDirectory()

    

allDirectories = currentDirectories + directories
sizeUpperLimit = 100000
directoriesWithinLimit = list(filter(lambda x : x["size"] <= sizeUpperLimit, allDirectories ))
totalSize = sum(map(lambda x: x["size"], directoriesWithinLimit))
print(totalSize)