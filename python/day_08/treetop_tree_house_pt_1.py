
rows = []
visibleTreePositions = []

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip('\n')
        rows.append(list(map(int,rawLine)))


width = height = len(rows)
edgeTreesCount = width * 2 + height* 2 - 4

def getNextHighestTreeData(currentPosition, highestTreePosition):
    (i,j) = currentPosition
    (m,n) = highestTreePosition
    
    currentTreeHeight = rows[i][j]
    highestTreeHeight = rows[m][n]
    
    if currentTreeHeight > highestTreeHeight:
        highestTreeHeight = currentTreeHeight
        highestTreePosition = currentPosition
        visibleTreePositions.append(highestTreePosition)
    
    return highestTreeHeight, highestTreePosition

for i in range(1, height - 1):
    highestTreeHeight = rows[i][0]
    highestTreePosition = (i,0)
    
    for j in range(1, width - 1):
        
        currentPosition = (i,j)
        highestTreeHeight, highestTreePosition = getNextHighestTreeData(currentPosition, highestTreePosition)
        
        if highestTreeHeight == 9:
            break
    
    highestTreePositionFromThisSide = highestTreePosition

    highestTreeHeight = rows[i][-1]
    highestTreePosition = (i, width -1)
    
    for j in reversed(range(highestTreePositionFromThisSide[1] + 1, width - 1)):

        currentPosition = (i,j)
        highestTreeHeight, highestTreePosition = getNextHighestTreeData(currentPosition, highestTreePosition)
        
        if highestTreeHeight == 9:
            break

    
for j in range(1, width - 1):        
    highestTreeHeight = rows[0][j]   
    highestTreePosition = (0,j)      
    for i in range(1, height - 1):   

        currentPosition = (i,j)
        highestTreeHeight, highestTreePosition = getNextHighestTreeData(currentPosition, highestTreePosition)

        if highestTreeHeight == 9:
            break
    highestTreePositionFromThisSide = highestTreePosition

    highestTreeHeight = rows[-1][j]           
    highestTreePosition = (height -1 , j)
    
    for i in reversed(range(highestTreePositionFromThisSide[0] + 1, height - 1)): #
        
        currentPosition = (i,j)
        highestTreeHeight, highestTreePosition = getNextHighestTreeData(currentPosition, highestTreePosition)
    
        if highestTreeHeight == 9:
            break
        
visibleTreeCount = len(set(visibleTreePositions)) + edgeTreesCount
print(visibleTreeCount)