

scoreForMyChoice = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

def calcScoreForOutcome(myCh,enemyCh):

  def evalOutcomeRock(enemyCh):
    if enemyCh == "A":
      return 3
    elif enemyCh == "B":
      return 0
    elif enemyCh == "C":
      return 6
    
  def evalOutcomePaper(enemyCh):
    if enemyCh == "A":
      return 6
    elif enemyCh == "B":
      return 3
    elif enemyCh == "C":
      return 0
      
  def evalOutcomeScissors(enemyCh):
    if enemyCh == "A":
      return 0
    elif enemyCh == "B":
      return 6
    elif enemyCh == "C":
      return 3
  scoreForOutcome = {
  "X": evalOutcomeRock(enemyCh),
  "Y": evalOutcomePaper(enemyCh),
  "Z": evalOutcomeScissors(enemyCh)
  }
  return scoreForOutcome[myCh]

totalScore = 0

with open('input.txt') as f:
    while line := f.readline():
        rawLine = line.strip()

        roundChoices = rawLine.split(" ")
        enemyChoice = roundChoices[0]
        myChoice = roundChoices[1]

        
        totalScore += scoreForMyChoice[myChoice] + calcScoreForOutcome(myChoice,enemyChoice)

print(totalScore)


