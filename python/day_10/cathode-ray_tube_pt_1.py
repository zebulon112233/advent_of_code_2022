
cycleCount = 0
registerValue = 1
totalSignalStrength = 0

def calcSignalStrength():
    return cycleCount * registerValue

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip('\n')
        
        command = rawLine.split(" ")[0]
        
        if command == "noop":
            cycleCount += 1
            if cycleCount % 40 == 20:
                totalSignalStrength += calcSignalStrength()
         
        else:
            for _ in range(2):
                cycleCount += 1
                if cycleCount % 40 == 20:
                    totalSignalStrength += calcSignalStrength()

                    
                
            registerValue += int(rawLine.split(" ")[1])
            
            
            
            
            
print(registerValue)
print(totalSignalStrength)