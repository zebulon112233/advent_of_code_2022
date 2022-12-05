import string

lowerCasePriorities = range(1,26+1)
lowerCaseLetters = string.ascii_lowercase
lowerCasePriorOrders= list(zip(lowerCasePriorities, lowerCaseLetters))

upperCasePriorities = range(27,52+1)
upperCaseLetters = string.ascii_uppercase
upperCasePriorOrders= list(zip(upperCasePriorities, upperCaseLetters))

totalPriority = 0
lines = []
with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip()

        lines.append(rawLine)

        if len(lines) == 3:
            intersectingChars = set(lines[0]).intersection(set(lines[1])).intersection(set(lines[2]))
            print(intersectingChars)
            for char in intersectingChars:
                for elem in lowerCasePriorOrders + upperCasePriorOrders:
                    if elem[1] == char:
                        totalPriority += elem[0]
            lines.clear()

        
print(totalPriority)

        
