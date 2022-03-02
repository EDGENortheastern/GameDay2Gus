import math
import random

# Sets initial flags
gameOver = False
guessX = [-1]
guessY = [-1]
printThis = False
enemyTotal = 1
shipTarget = [0,0]

#X is height, Y is width
#Prints Grid
def printPlainGrid(gX, gY):
  # Set Global Flag
  printThis = False
  # Top Border
  for y in range(gY):
    print("****", end="")
  print("*")
  #Cycle Columns
  for x in range(gX):
    #Cycle Rows
    for y in range(gY):
      print("| ",end="")
      #Cycle Guesses
      for i in range(len(guessX)):
        #Checks if any guesses equal the current cell being viewed. Changes Flag
        if(guessX[i] == x and guessY[i] == y):
          printThis = True
      #Prints Fired Shot if Guess is Made. Else Prints X
      if printThis == True:
        print("0",end="")
        printThis = False
      else:
        print("X",end="")
      print(" ",end="")
    print("|")
  #Prints Lower Border
  for x in range(gY):
    print("****", end="")
  print("*")

#Appends X and Y to the list of Guesses only when [X,Y] is present within guessX,guessY
def appendXY(aX, aY):
  #print(guessX)
  #print(guessY)
  appCoor = True
  for i in range(len(guessX)):
    if(guessX[i] == aX and guessY[i] == aY):
      appCoor = False
  if (appCoor == True):
    guessX.append(aX)
    guessY.append(aY)
  return appCoor
    

#Checks for hit in all guesses and returns true when true
#OBSOLETE
  """
def checkHit():
  if enemyTotal == 0:
    return True
  for i in range(len(guessX)):
    for x in range(len(enemyX)):
      for y in range(len(enemyY)):
        if(guessX[i] == enemyX[x] and guessY[i] == enemyY[y]):
          print("Hit! Ship sunk!")
          enemyTotal -= 1
          return False

  return False
  """
    
#Obtain size of grid.
print("Lets play Battleship. First choose the size of your grid!")
gridX = int(input("What is grid height: "))
gridY = int(input("What is grid width: "))


#Initialize enemy ships. 
enemyTotal = 1
enemyTotal = int(input("Please enter the total number of enemy ships: "))
enemyX = []
enemyY = []
for i in range(enemyTotal):
  enemyX.append(random.randint(0,gridX-1))
  enemyY.append(random.randint(0,gridY-1))
  #print(enemyX)
  #print(enemyY)
  


#Initialize Grid
printPlainGrid(gridX,gridY)

#starting loop
while gameOver != True:
  #Coor of next shot
  appendCheck = True
  shotX = int(input("Row of Shot: "))-1
  shotY = int(input("Column of Shot: "))-1
  appendCheck = appendXY(shotX,shotY)
  if appendCheck == False:
    continue
  #print(guessX)
  #print(guessY)
  #Print Grid
  printPlainGrid(gridX,gridY)
  #Check for Victory Condition.
  for i in range(len(guessX)):
    for x in range(len(enemyX)):
      for y in range(len(enemyY)):
        if(guessX[i] == enemyX[x] and guessY[i] == enemyY[y]):
          print("Hit! Ship sunk!")
          enemyTotal -= 1
          continue
  if enemyTotal <= 0:
    gameOver = True
  