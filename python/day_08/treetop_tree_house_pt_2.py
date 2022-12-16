
rows = []

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip('\n')
        rows.append(list(map(int,rawLine)))


width = height = len(rows)

scenicScore = 0
maxScenicScore = 0

def isInside(i,j):
    return i >= 0 and i < width and j >= 0 and j < height

def calcScenicScoreFromPosition(initialPosition):
    scenicScores = [0,0,0,0]
    (initX,initY) = initialPosition
    initialTreeHeight = rows[initY][initX]
    
    ### Calc to left
    idx = initX - 1
    while isInside(idx,initY) and rows[initY][idx] < initialTreeHeight:
        scenicScores[0] += 1
        idx -= 1
    if isInside(idx, initY):
        scenicScores[0] += 1
        
    ### Calc to right
    idx = initX + 1
    while isInside(idx,initY) and rows[initY][idx] < initialTreeHeight:
        scenicScores[1] += 1
        idx += 1
    if isInside(idx, initY):
        scenicScores[1] += 1
        
    ### Calc to bottom
    idx = initY + 1
    while isInside(initX,idx) and rows[idx][initX] < initialTreeHeight:
        scenicScores[2] += 1
        idx += 1
    if isInside(initX, idx):
        scenicScores[2] += 1
        
    ### Calc to bottom
    idx = initY - 1
    while isInside(initX,idx) and rows[idx][initX] < initialTreeHeight:
        scenicScores[3] += 1
        idx -= 1
    if isInside(initX, idx):
        scenicScores[3] += 1
        
    return scenicScores[0] * scenicScores[1] * scenicScores[2] * scenicScores[3]
    
### For each tree calc
for i in range(width):
    for j in range(height):
        
        currentPosition = (i,j)
        scenicScore = calcScenicScoreFromPosition(currentPosition)
        
        if scenicScore > maxScenicScore:
            maxScenicScore = scenicScore

print(maxScenicScore)