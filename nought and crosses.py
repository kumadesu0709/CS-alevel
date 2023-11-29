import random
class Board:
    def __init__(self):
        self._data = ['   '] * 9

    def display(self):
        print(f'{self._data[0]}|{self._data[1]}|{self._data[2]}            0  |  1  |  2  ')
        print("------------          --------------- ")
        print(f'{self._data[3]}|{self._data[4]}|{self._data[5]}            3  |  4  |  5  ')
        print("------------          --------------- ")
        print(f'{self._data[6]}|{self._data[7]}|{self._data[8]}            6  |  7  |  8  ')
    
    def is_valid(self, x):
        if self._data[int(x)] == " x " or self._data[int(x)] == " o ":
            return False
        else:
            return True

    def set_cell(self, x, marker):
        self._data[int(x)] = marker

    def is_full(self):
        is_full = 0
        for i in range (0,9):
            if self._data[i] != "   ":
                is_full += 1
        if is_full == 9:
            return True
        else:
            return False
        
    def someone_wins(self):
        win = False
        if self._data[0] == self._data[1] == self._data[2]:
            if self._data[0] != "   ":
                win = True
        if self._data[3] == self._data[4] == self._data[5]:
            if self._data[3] != "   ":
                win = True
        if self._data[6] == self._data[7] == self._data[8]:
            if self._data[6] != "   ":
                win = True
        if self._data[0] == self._data[3] == self._data[6]:
            if self._data[0] != "   ":
                win = True
        if self._data[1] == self._data[4] == self._data[7]:
            if self._data[1] != "   ":
                win = True
        if self._data[2] == self._data[5] == self._data[8]:
            if self._data[2] != "   ":
                win = True
        if self._data[0] == self._data[4] == self._data[8]:
            if self._data[0] != "   ":
                win = True
        if self._data[2] == self._data[4] == self._data[6]:
            if self._data[2] != "   ":
                win = True
        return win
    
    def who_wins(self):
        if self.someone_wins() == True:
            winner = ""
            if self._data[0] == self._data[1] == self._data[2]:
                if self._data[0] == " x ":
                    winner = "player x"
                else:
                    winner = "player o"
            if self._data[3] == self._data[4] == self._data[5]:
                if self._data[3] == " x ":
                    winner = "player x"
                else:
                    winner = "player o"
            if self._data[6] == self._data[7] == self._data[8]:
                if self._data[6] == " x ":
                    winner = "player x"
                else:
                    winner = "player o"
            if self._data[0] == self._data[3] == self._data[6]:
                if self._data[0] == " x ":
                    winner = "player x"
                else:
                    winner = "player o"
            if self._data[1] == self._data[4] == self._data[7]:
                if self._data[1] == " x ":
                    winner = "player x"
                else:
                    winner = "player o"
            if self._data[2] == self._data[5] == self._data[8]:
                if self._data[2] == " x ":
                    winner = "player x"
                else:
                    winner = "player o"
            if self._data[0] == self._data[4] == self._data[8]:
                if self._data[0] == " x ":
                    winner = "player x"
                else:
                    winner = "player o!"
            if self._data[2] == self._data[4] == self._data[6]:
                if self._data[2] == " x ":
                    winner = "player x"
                else:
                    winner = "player o"
            return winner

board = Board()
player = input("Do you want to be the one playing noughts or the one playing crosses?:")
if player == "o":
    while board.someone_wins() == False and board.is_full() == False:
        board.display()
        position = input("Please type in which position you want to place your marker in")
        while board.is_valid(position) == False:
            print("Your position is invalid")
            position = input("Please type in a valid location:")
        board.set_cell(position, " o ")
        if board.someone_wins() == True:
            break
        x = random.randint(0,8)
        while board.is_valid(x) == False:
            x = random.randint(0,8)
        board.set_cell(x," x ")
        if board.someone_wins() == True:
            break
    if board.is_full() == True:
        print("It's a tie!")
    board.display()
    board.who_wins()
