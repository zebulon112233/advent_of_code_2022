


totalCalories = 0
maxCalories = 0

def updateTopCalories(totalCal,maxCal):
    if maxCal < totalCal:
        maxCal = totalCal
    return maxCal

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip()

        if(rawLine == ""):
            maxCalories = updateTopCalories(totalCalories,maxCalories)
            totalCalories = 0
        else:
            currentCalorie = int(rawLine)
            totalCalories += currentCalorie

maxCalories = updateTopCalories(totalCalories,maxCalories)

print(maxCalories)
        