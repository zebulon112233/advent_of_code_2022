


totalCalories = 0
topCalories = [0,0,0]

def updateTopCalories(totalCal,list):
    smallestElemest = min(list)
    if(smallestElemest < totalCal):
        idx = list.index(smallestElemest)
        list[idx] = totalCal

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip()

        if(rawLine == ""):
            updateTopCalories(totalCalories,topCalories)
            totalCalories = 0
        else:
            currentCalorie = int(rawLine)
            totalCalories += currentCalorie

updateTopCalories(totalCalories,topCalories)

print(sum(topCalories))