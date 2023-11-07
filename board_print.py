#NOTE: this file is NOT required to run Battleship, this is simply a note-taking file. battleship.py is the only file needed for Battleship

#board_print takes in board as a parameter, with board being a dictionary representing a player's board
def board_print(board):
  #pr_line and pr_letter are used temporarily to print each item in the dictionary's lists
  pr_line = 0
  pr_letter = 0

  #using items in board['1'] may seem useless, but it makes board_print work with the Veteran Mode board
  for items in board['1']:
    #goes to each line within the dictionary, starting at 1
    pr_line += 1
    #makes it a string
    pr_line = str(pr_line)
    #see 9
    for items in board['1']:
      #prints each letter as it's passed through (example: board['3'][0] would print line 3's first position, which is A)
      print(board[pr_line][pr_letter],  end=' ')
      #delays printing to make it look cooler
      time.sleep(0.02)
      #adds 1 to pr_letter for each loop
      pr_letter += 1
    #sets pr_letter to 0 to repeat the loop, also makes pr_line an integer to be added to
    print()
    pr_letter = 0
    pr_line = int(pr_line)
