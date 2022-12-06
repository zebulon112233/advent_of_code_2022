

with open('input.txt') as f:
        dataStream = f.readline().strip('\n')
        
        dataStreamLength = len(dataStream)
        windowLength = 4
        hasFoundMarker = False
        idx = 0
        while not hasFoundMarker and idx < dataStreamLength:
            
            currentWindow = []
            for i in range(windowLength):
                currentWindow.append(dataStream[idx+i])
                
            hasDuplicateItems = len(set(currentWindow)) != windowLength
            
            if hasDuplicateItems:
                idx += 1
            else:
                hasFoundMarker = True

markerPosition = idx + windowLength   
print(markerPosition)



        
