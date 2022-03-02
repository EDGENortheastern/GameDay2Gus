import math

def baseOutput():
  print("************")
  for x in range(3):
    print(" X | X | X ")
  print("************")

#Handles printing of board
def introPrint(coorX, coorY,shotsFired):
  # Prints Initial Border
  for l in range(coorY):
    print("****", end="")
  print("*")
  # Cycles Rows
  for x in range(coorX):
    # Cycles Columns
    for y in range(coorY):
      # Cycles shots fired
      for z in shotsFired:
        testingInt = char(x) + char(y)
        print(testingInt)
        

        """""
        if int(z%10) == y+1 and int(z-(z%10)/10) == x+1:
          print("| 0 ",end="")
        else:
          # Prints Empty Rows
          print("| X ",end="") 
    print("|")
        """
  # Prints Ending Border
  for x in range(coorY):
    print("****", end="")
  print("*")
    
# Receives initial Grid size
gridSize = int(input("What is the grid size: "))
gridY = int(gridSize%10)
gridX = int(( gridSize - gridY ) / 10)
# Receives Target Ship Location
shipLocation = int(input("What is the ship location: "))
shotsFired = []


#Initialize Game
gameOver = False
while gameOver == False:
  #Starts Fire Coordinate Check
  fireLocation = int(input("What is the fire location: "))
  # Checks if successful. Ends Game.
  if fireLocation == shipLocation:
    print("Hit! You sunk the Battleship!")
    gameOver = True
  # Appends shot to listing, prior removal prevents doubles.
  try:
    shotsFired.remove(fireLocation)
  except ValueError:
    shotsFired.append(fireLocation)
  # Prints Current Board
  introPrint(gridY,gridX,shotsFired)
  
  
