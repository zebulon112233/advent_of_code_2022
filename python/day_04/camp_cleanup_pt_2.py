

overlapCount = 0

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip()

        pairs = rawLine.split(",")
        firstElfSections = pairs[0].split("-")
        secondElfSections = pairs[1].split("-")
        
        if int(firstElfSections[1]) >= int(secondElfSections[0]) and int(firstElfSections[0]) <= int(secondElfSections[1]):
            overlapCount += 1
        
        
print(overlapCount)

        
