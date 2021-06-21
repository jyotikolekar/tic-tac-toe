board=["-","-","-",
       "-","-","-",
       "-","-","-"]

currentplayer="X"
gameisgoing=True
winner=None

def display_board():
       print(board[0] + " | " + board[1]+ " | " + board[2])
       print(board[3] + " | " + board[4]+ " | " + board[5])
       print(board[6] + " | " + board[7]+ " | " + board[8])


def handle_turns():
       position=int(input("Enter the position number:"))
       board[position]=currentplayer

def swap_player():
       global currentplayer
       if currentplayer=="X":
              currentplayer="O"
       elif currentplayer=="O":
              currentplayer="X"

def check_who_is_the_winner():
       global winner
       rowwinner=check_row()
       colwinner=check_col()
       diagonalwinner=check_diagonal()

       if rowwinner:
              winner=rowwinner
       elif colwinner:
              winner=colwinner
       elif diagonalwinner:
              winner=diagonalwinner

def check_row():
       global gameisgoing
       row1 = board[0] == board[1] == board[2] != "-"
       row2 = board[3] == board[4] == board[5] != "-"
       row3 = board[6] == board[7] == board[8] != "-"

       if row1 or row2 or row3:
              gameisgoing=False

       if row1:
              return board[0]# or board[1] or board[2]
       elif row2:
              return board[3]#board[4]or board[5]
       elif row3:
              return board[6] #or 7 or 8


def check_col():
       global gameisgoing
       col1 = board[0] == board[3] == board[6] != "-"
       col2 = board[1] == board[4] == board[7] != "-"
       col3 = board[2] == board[5] == board[8] != "-"

       if col1 or col2 or col3:
              gameisgoing=False

       if col1:
              return board[0]# or board[3] or board[6]
       elif col2:
              return board[1]#board[4]or board[7]
       elif col3:
              return board[2] #or 2 or 8


def check_diagonal():
       global gameisgoing
       dia1 = board[0] == board[4] == board[8] != "-"
       dia2 = board[2] == board[4] == board[6] != "-"

       if dia1 or dia2:
              gameisgoing=False

       if dia1:
              return board[0]# or board[4] or board[8]
       elif dia2:
              return board[2]#board[4]or board[6]

def check_draw():
       global gameisgoing
       if board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] != "-":
              gameisgoing=False
              print("Match is drawn")

def play_game():
       global gameisgoing
       while gameisgoing:
              display_board()

              handle_turns()

              swap_player()

              check_who_is_the_winner()

       if winner=="X":
              print("X is the winner")
       elif winner=="O":
              print("O is the winner")
play_game()

