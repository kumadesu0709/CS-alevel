#Skeleton Program for the AQA COMP1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA COMP1 Programmer Team
#developed in a Python 3.4 programming environment

import random

def SetUpGameBoard(Board, Boardsize):
  """Modifies the Board 2D list to place H and C in the centre """
  for Row in range(1, BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if (Row == (BoardSize + 1) // 2 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2 + 1):
        Board[Row][Column] = "C"
      elif (Row == (BoardSize + 1) // 2 + 1 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2):
        Board[Row][Column] = "H"
      else:
        Board[Row][Column] = " "

def ChangeBoardSize():
  """Asks the user to change the board size, if the new boardsize is in between 4 and 9, the boardsize will be changed"""
  BoardSize = int(input("Enter a board size (between 4 and 9): "))
  while not(BoardSize >= 4 and BoardSize <= 9):
    BoardSize = int(input("Enter a board size (between 4 and 9): "))
  return BoardSize

def GetHumanPlayerMove(PlayerName):
  """Asks the player where they want to place their piece, return the coordinate that the player entered"""
  print(PlayerName, "enter the coodinates of the square where you want to place your piece: ", end="")
  Coordinates = int(input())
  return Coordinates

def GetComputerPlayerMove(BoardSize):
  """Randomly generate a cooridinate, return the coordinate"""
  return random.randint(1, BoardSize) * 10 + random.randint(1, BoardSize)

def GameOver(Board, BoardSize):
  """If the board is not full (i.e. still has " "), game is not over so therefore return false. If the board is full, game is over and therefore return true."""
  for Row in range(1 , BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == " ":
        return False
  return True

def GetPlayersName():
  """Ask the player to input their name, return the player name that they returned"""
  PlayerName = input("What is your name? ")
  return PlayerName

def CheckIfMoveIsValid(Board, Move):
  """Originally MoveIsValid is False. If the position of move is a space at the moment (i.e. ' '), then MoveIsValid becomes True. MoveIsValid is then returned at the end of the function."""
  Row = Move % 10
  Column = Move // 10
  MoveIsValid = False
  if Board[Row][Column] == " ":
    MoveIsValid = True
  return MoveIsValid

def GetPlayerScore(Board, BoardSize, Piece):
  """Loop through the Board 2D list, check the total number of the piece on the board, return the total number (i.e. the score)"""
  Score = 0
  for Row in range(1, BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == Piece:
        Score = Score + 1
  return Score

def CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  """check whethere there's pieces to flip. If there is, return Ture. """
  RowCount = StartRow + RowDirection
  ColumnCount = StartColumn + ColumnDirection
  FlipStillPossible = True
  FlipFound = False
  OpponentPieceFound = False
  while RowCount <= BoardSize and RowCount >= 1 and ColumnCount >= 1 and ColumnCount <= BoardSize and FlipStillPossible and not FlipFound:
    if Board[RowCount][ColumnCount] == " ":
      FlipStillPossible = False
    elif Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      OpponentPieceFound = True
    elif Board[RowCount][ColumnCount] == Board[StartRow][StartColumn] and not OpponentPieceFound:
      FlipStillPossible = False
    else:
      FlipFound = True
    RowCount = RowCount + RowDirection
    ColumnCount = ColumnCount + ColumnDirection
  return FlipFound

def FlipOpponentPiecesInOneDirection(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  """Flip all the opponent pieces in one direction"""
  FlipFound = CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection)
  if FlipFound:
    RowCount = StartRow + RowDirection
    ColumnCount = StartColumn + ColumnDirection
    while Board[RowCount][ColumnCount] != " " and Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      if Board[RowCount][ColumnCount] == "H":
        Board[RowCount][ColumnCount] = "C"
      else:
        Board[RowCount][ColumnCount] = "H"
      RowCount = RowCount + RowDirection
      ColumnCount = ColumnCount + ColumnDirection

def MakeMove(Board, BoardSize, Move, HumanPlayersTurn):
  """Place the piece onto the right position"""
  Row = Move % 10
  Column = Move // 10
  if HumanPlayersTurn:
    Board[Row][Column] = "H"
  else:
    Board[Row][Column] = "C"
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, -1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, 1)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, -1)


def PrintLine(BoardSize):
  """Print a line that has a length that's twice as long as the boardsize"""
  print("   ", end="")
  for Count in range(1, BoardSize * 2):
    print("_", end="")
  print()

def DisplayGameBoard(Board, BoardSize):
  """Loop through each column and row in the Boad 2D list. Then, display the board"""
  print()
  print("  ", end="")
  for Column in range(1, BoardSize + 1):
    print(" ", end="")
    print(Column, end="")
  print()
  PrintLine(BoardSize)
  for Row in range(1, BoardSize + 1):
    print(Row, end="")
    print(" ", end="")
    for Column in range(1, BoardSize + 1):
      print("|", end="")
      print(Board[Row][Column], end="")
    print("|")
    PrintLine(BoardSize)
    print()

def DisplayMenu():
  """print out the menu"""
  print("(p)lay game")
  print("(e)nter name")
  print("(c)hange board size")
  print("(q)uit")
  print()

def GetMenuChoice(PlayerName):
  """Asks the player for the option, return the option that the player chose"""
  print(PlayerName, "enter the letter of your chosen option: ", end="")
  Choice = input()
  return Choice

def CreateBoard():
  """Create a 2D list named Board"""
  Board = []
  for Count in range(BoardSize + 1):
    Board.append([])
    for Count2 in range(BoardSize + 1):
      Board[Count].append("")
  return Board

def PlayGame(PlayerName, BoardSize):
  """set up a board, start allowing the player to play against the computer, end the game once the board is full, print out the result at the end."""
  Board = CreateBoard()
  SetUpGameBoard(Board, BoardSize)
  HumanPlayersTurn = False
  while not GameOver(Board, BoardSize):
    HumanPlayersTurn = not HumanPlayersTurn
    DisplayGameBoard(Board, BoardSize)
    MoveIsValid = False
    while not MoveIsValid:
      if HumanPlayersTurn:
        Move = GetHumanPlayerMove(PlayerName)
      else:
        Move = GetComputerPlayerMove(BoardSize)
      MoveIsValid = CheckIfMoveIsValid(Board, Move)
    if not HumanPlayersTurn:
      print("Press the Enter key and the computer will make its move")
      input()
    MakeMove(Board, BoardSize, Move, HumanPlayersTurn)
  DisplayGameBoard(Board, BoardSize)
  HumanPlayerScore = GetPlayerScore(Board, BoardSize, "H")
  ComputerPlayerScore = GetPlayerScore(Board, BoardSize, "C")
  if HumanPlayerScore > ComputerPlayerScore:
    print("Well done", PlayerName, ", you have won the game!")
  elif HumanPlayerScore == ComputerPlayerScore:
    print("That was a draw!")
  else:
    print("The computer has won the game!")
  print()


random.seed()
BoardSize = 6
PlayerName = ""
Choice = ""
while Choice != "q":
  DisplayMenu()
  Choice = GetMenuChoice(PlayerName)
  if Choice == "p":
    PlayGame(PlayerName, BoardSize)
  elif Choice == "e":
    PlayerName = GetPlayersName()
  elif Choice == "c":
    BoardSize = ChangeBoardSize()
