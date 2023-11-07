#NOTE: this file is NOT required to run Battleship, this is simply a note-taking file. battleship.py is the only file needed for Battleship
#NOTE: some of the dictionaries are described as lists, this was an oversight while programming and my mistake
#The variables below are "lists" that are actually dictionaries
#aim_board
#miss_board
#vet_list
#list_check
#bot_list
#player_list

#hit_check takes a firing_line (which is 1-7), a firing_column (A-G), a hit_list (only used for ease of reading, boatBot has this as None),
#a miss_list(used by player and boatBot, however, boatBot doesn't use this in Veteran Mode), the aim_board (either the players board or boatBot's board),
#and a miss_board(only used by the player, boatBot has this set to None)
def hit_check(firing_line, firing_column, hit_list, miss_list, aim_board, miss_board):
    #gets the position of A-G on the letters list (example: D = 3)
    firing_number = letters.index(firing_column)
    #turns the firing_line into a string for dictionary index
    firing_line = str(firing_line)
    #checks if the position in a list inside of a board (or dictionary) is '0', which is a boat
    if aim_board[firing_line][firing_number] == '0':
        #if the board being aimed at is the player's, prints the below statement
        if aim_board == player_list or aim_board == vet_list:
            print("We've Been Hit!")
        else:
            #prints if the board aimed at is boatBot's
            print("Direct Hit!")
        #sets the position where '0' was to an 'X'
        aim_board[firing_line][firing_number] = 'X'
        #checks if the miss_board is defined
        if miss_board == None:
          pass
        else:
          #only for player
          #sets the hit position to an 'X' on the Hit-Miss board
          miss_board[firing_line][firing_number] = 'X'
          #adds the position to the hit_list to be printed later
          hit_list.append(str(firing_column) + str(firing_line))
    #if the position doesn't have a boat on it
    else:
        #prints statement below if the board aimed at is the player's
        if aim_board == player_list or aim_board == vet_list:
            print("They missed!")
        else:
            #prints the statement below if the board belongs to boatBot
            print("Misfire!")
        #see 29
        if miss_board == None:
          pass
        else:
          #sets miss_board's position to 0
          #NOTE: miss_board is a dictionary with 7 lists, each with 7 O's
          miss_board[firing_line][firing_number] = 0
          miss_list.append(str(firing_column) + str(firing_line))


#win_check takes a player board (described as bot_list, vet_list, or player_list) as a parameter
def win_check(list_check):
    #unit is used to iterate through each item in the dictionary
    unit = 0
    #win is a variable that is added to when a boat is detected. if win is still 0 by the end, the player has lost or won
    win = 0
    #unit is increased by 1 each loop until it reaches 7, when it stops
    while unit < 7:
        unit += 1
        #turns unit into a string so it can be used as a dictionary index
        unit = str(unit)
        #'0' is considered a boat, any detected on the board will mean the game continues
        if '0' in list_check[unit]:
            #win is increased by 1 if a '0' is found, therefore continuing the game
            win += 1
            break
        else:
            unit = int(unit)
    #after the while loop above, the win variable is checked to see if its unchanged
    if win == 0:
      #prints depending on which board (dictionary) was called as list_check
      if list_check == bot_list:
        print('You Win!')
      if list_check == player_list or list_check == vet_list:
        print('You Lost.')
      #accesses the Game variable and makes it False
      global Game
      Game = False

#examples of hit_check and win_check
#NOTE: example below is on Veteran Mode
hit_check(robot_fire_li, robot_fire_le, None, None, vet_list, None)

win_check(player_list)
