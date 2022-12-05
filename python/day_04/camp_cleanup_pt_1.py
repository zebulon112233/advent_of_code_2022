

fullyContainsCount = 0

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip()

        pairs = rawLine.split(",")
        firstElfSections = pairs[0].split("-")
        secondElfSections = pairs[1].split("-")
        
        doesFirstContainSecond = int(firstElfSections[0]) <= int(secondElfSections[0])   and int(firstElfSections[1]) >= int(secondElfSections[1])
        doesSecondContainFirst = int(firstElfSections[0]) >= int(secondElfSections[0])   and int(firstElfSections[1]) <= int(secondElfSections[1])
        if doesFirstContainSecond or doesSecondContainFirst:
            fullyContainsCount += 1
        
print(fullyContainsCount)

        
