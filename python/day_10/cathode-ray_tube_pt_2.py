
### Note: I know this is not DRY (and it really bothers me) but now I want to progress rather than making cosmetics

cycleCount = 0
registerValue = 1

spriteStartPosition = 0
spriteLength = 3
charsToPrintInLine = ""

def isSpriteInThisPosition(crtAbsolutePosition):
    crtRelPosition = crtAbsolutePosition % 40
    spriteEndPosition = spriteStartPosition + spriteLength  - 1
    return crtRelPosition >= spriteStartPosition and crtRelPosition <= spriteEndPosition

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip('\n')
        
        command = rawLine.split(" ")[0]
        
        if command == "noop":

            if isSpriteInThisPosition(cycleCount):
                charsToPrintInLine += "#"
            else:
                charsToPrintInLine += "."

            cycleCount += 1
            
            if cycleCount % 40 == 0:
                print(charsToPrintInLine)
                charsToPrintInLine = ""
         
        else:
           
            for _ in range(2):
                if isSpriteInThisPosition(cycleCount):
                    charsToPrintInLine += "#"
                else:
                    charsToPrintInLine += "."
                    
                cycleCount += 1
                if cycleCount % 40 == 0:
                    print(charsToPrintInLine)
                    charsToPrintInLine = ""

            registerValue += int(rawLine.split(" ")[1])
            spriteStartPosition = registerValue - 1
            
            
            
print(cycleCount)