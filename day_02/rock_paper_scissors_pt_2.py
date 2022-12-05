
totalScore = 0

scoreForOutcome = {
  "X": 0,
  "Y": 3,
  "Z": 6
}
scoreForMyChoice = {
  "A": 1,
  "B": 2,
  "C": 3
}
# A - rock, B - paper, C - scissors
def calcMyChoice(enemyCh,expOutcome):
  def evalOutcomeLose(enemyCh):
    if enemyCh == "A":
      return "C"
    elif enemyCh == "B":
      return "A"
    elif enemyCh == "C":
      return "B"
    
  def evalOutcomeDraw(enemyCh):
    if enemyCh == "A":
      return "A"
    elif enemyCh == "B":
      return "B"
    elif enemyCh == "C":
      return "C"
      
  def evalOutcomeWin(enemyCh):
    if enemyCh == "A":
      return "B"
    elif enemyCh == "B":
      return "C"
    elif enemyCh == "C":
      return "A"
  myChoice = {
  "X": evalOutcomeLose(enemyCh),
  "Y": evalOutcomeDraw(enemyCh),
  "Z": evalOutcomeWin(enemyCh)
  }
  return myChoice[expOutcome]

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip()

        roundChoices = rawLine.split(" ")
        enemyChoice = roundChoices[0]
        expectedOutcome = roundChoices[1]
        
        myChoice = calcMyChoice(enemyChoice,expectedOutcome)
        
        totalScore += scoreForMyChoice[myChoice] + scoreForOutcome[expectedOutcome]
       

print(totalScore)


