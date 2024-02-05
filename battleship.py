import random
import time

#customizations that can be added to the game
options_list = {
    'AutoBoat': False,
    'AutoPlace': False,
    'Rapid Fire': False,
    'Hard Mode': False,
    'Veteran Mode': False,
    'War Mode': False,
    'Boat Overlap': False,
    'Go Back': False
}

#used for placing boats on boards
boat_length = {
  'Carrier': 5,
  'Battleship': 4,
  'Cruiser': 3,
  'Submarine': 3,
  'Destroyer': 2
}

#lists for boats
boat_list_robot = ['Carrier','Battleship','Cruiser','Submarine','Destroyer']
boat_list_player =['Carrier','Battleship','Cruiser','Submarine','Destroyer']
#direction the boats will point
direction = ['right','left','up','down']

#player and bot boards
bot_list = {
  '1': ['A','B','C','D','E','F','G'],
  '2': ['A','B','C','D','E','F','G'],
  '3': ['A','B','C','D','E','F','G'],
  '4': ['A','B','C','D','E','F','G'],
  '5': ['A','B','C','D','E','F','G'],
  '6': ['A','B','C','D','E','F','G'],
  '7': ['A','B','C','D','E','F','G']
}
vet_list = {
  '1': ['A','B','C','D','E'],
  '2': ['A','B','C','D','E'],
  '3': ['A','B','C','D','E'],
  '4': ['A','B','C','D','E'],
  '5': ['A','B','C','D','E']
}
player_list = {
  '1': ['A','B','C','D','E','F','G'],
  '2': ['A','B','C','D','E','F','G'],
  '3': ['A','B','C','D','E','F','G'],
  '4': ['A','B','C','D','E','F','G'],
  '5': ['A','B','C','D','E','F','G'],
  '6': ['A','B','C','D','E','F','G'],
  '7': ['A','B','C','D','E','F','G']
}
#miss board for the actual game
player_miss_board = {
    '1': ['O','O','O','O','O','O','O'],
    '2': ['O','O','O','O','O','O','O'],
    '3': ['O','O','O','O','O','O','O'],
    '4': ['O','O','O','O','O','O','O'],
    '5': ['O','O','O','O','O','O','O'],
    '6': ['O','O','O','O','O','O','O'],
    '7': ['O','O','O','O','O','O','O']
}
helpful_board = {
  '1': ['A1','B1','C1','D1','E1','F1','G1'],
  '2': ['A2','B2','C2','D2','E2','F2','G2'],
  '3': ['A3','B3','C3','D3','E3','F3','G3'],
  '4': ['A4','B4','C4','D4','E4','F4','G4'],
  '5': ['A5','B5','C5','D5','E5','F5','G5'],
  '6': ['A6','B6','C6','D6','E6','F6','G6'],
  '7': ['A7','B7','C7','D7','E7','F7','G7']
}
extra_board = {
  '1': ['A','B','C','D','E','F','G'],
  '2': ['A','B','C','D','E','F','G'],
  '3': ['A','B','C','D','E','F','G'],
  '4': ['A','B','C','D','E','F','G'],
  '5': ['A','B','C','D','E','F','G'],
  '6': ['A','B','C','D','E','F','G'],
  '7': ['A','B','C','D','E','F','G']
}
#list of lines and positions to pick from
lines = ['1','2','3','4','5','6','7']
letters = ['A','B','C','D','E','F','G']
#variable for looping
boats = 5

#function to check if someone got hit (only called within)(explained more in hit_check_AND_win_check.py)
def hit_check(firing_line, firing_column, hit_list, miss_list, aim_board, miss_board):
    firing_number = letters.index(firing_column)
    firing_line = str(firing_line)
    if aim_board[firing_line][firing_number] == '0':
        if aim_board == player_list or aim_board == vet_list:
            print("We've Been Hit!")
        else:
            print("Direct Hit!")
        aim_board[firing_line][firing_number] = 'X'
        if miss_board == None:
          pass
        else:
          miss_board[firing_line][firing_number] = 'X'
          hit_list.append(str(firing_column) + str(firing_line))
    else:
        if aim_board == player_list or aim_board == vet_list:
            print("They missed!")
        else:
            print("Misfire!")
        if miss_board == None:
          pass
        else:
          miss_board[firing_line][firing_number] = 'M'
          miss_list.append(str(firing_column) + str(firing_line))

#function to check if someone wins (only called within game) (explained more in hit_check_AND_win_check.py)
def win_check(list_check):
    unit = 0
    win = 0
    while unit < 7:
        unit += 1
        unit = str(unit)
        if '0' in list_check[unit]:
            win += 1
            break
        else:
            unit = int(unit)
    if win == 0:
      if list_check == bot_list:
        print('You Win!')
      if list_check == player_list or list_check == vet_list:
        print('You Lost.')
      global Game
      Game = False
    
def direction_setup(spaces, line_count, letter):
  global direction
  if options_list['Veteran Mode'] == True:
    if spaces == 4:
      if line_count < 4:
        direction.remove('up')
      if line_count > 2:
        direction.remove('down')
      if letters.index(letter) >= 2:
        direction.remove('right')
      if letters.index(letter) <= 2:
        direction.remove('left')
    if spaces == 3:
      if line_count < 3:
        direction.remove('up')
      if line_count > 3:
        direction.remove('down')
      if letters.index(letter) >= 3:
        direction.remove('right')
      if letters.index(letter) <= 1:
        direction.remove('left')
    if spaces == 2:
      if line_count < 2:
        direction.remove('up')
      if line_count > 4:
        direction.remove('down')
      if letters.index(letter) >= 4:
        direction.remove('right')
      if letters.index(letter) <= 0:
        direction.remove('left')
  else:
    if spaces == 5:
      if line_count < 5:
        direction.remove('up')
      if line_count > 3:
        direction.remove('down')
      if letters.index(letter) >= 3:
        direction.remove('right')
      if letters.index(letter) <= 3:
        direction.remove('left')

    if spaces == 4:
      if line_count < 4:
        direction.remove('up')
      if line_count > 4:
        direction.remove('down')
      if letters.index(letter) >= 4:
        direction.remove('right')
      if letters.index(letter) <= 2:
        direction.remove('left')

    if spaces == 3:
      if line_count < 3:
        direction.remove('up')
      if line_count > 5:
        direction.remove('down')
      if letters.index(letter) >= 5:
        direction.remove('right')
      if letters.index(letter) <= 1:
        direction.remove('left')

    if spaces == 2:
      if line_count < 2:
        direction.remove('up')
      if line_count > 6:
        direction.remove('down')
      if letters.index(letter) >= 6:
        direction.remove('right')
      if letters.index(letter) <= 0:
        direction.remove('left')
def direction_reset():
  global direction
  direction = []
  direction.append('up')
  direction.append('down')
  direction.append('right')
  direction.append('left')
#places the boats for both BoatBot and the player (explained better in placing_function.py)
def boat_placer(length, direction, line, column, placing_dict, overlap, backup_list):
  if isinstance(line, str) == False:
    line = str(line)
  column = letters.index(column)
  instance_count = 0
  global extra_board
  for i in range(boat_length[length]):
    if placing_dict[line][column] == '0' and overlap == False:
      if backup_list.count(length) < 1:
        backup_list.append(length)
      if backup_list != boat_list_robot:
        print('Error: please reBoat.')
        backup_list.append(length)
      for i in range(instance_count):
        if direction == 'right':
          column -= 1
          placing_dict[line][column] = extra_board[line][column]
        if direction == 'left':
          column += 1
          placing_dict[line][column] = extra_board[line][column]
        if direction == 'down':
          line = int(line)
          line -= 1
          line = str(line)
          placing_dict[line][column] = extra_board[line][column]
        if direction == 'up':
          line = int(line)
          line += 1
          line = str(line)
          placing_dict[line][column] = extra_board[line][column]
      break
    if direction == 'right':
      placing_dict[line][column] = '0'
      column += 1
    if direction == 'left':
      placing_dict[line][column] = '0'
      column -= 1
    if direction == 'down':
      placing_dict[line][column] = '0'
      line = int(line)
      line += 1
      line = str(line)
    if direction == 'up':
      placing_dict[line][column] = '0'
      line = int(line)
      line -= 1
      line = str(line)
    instance_count += 1
  print()
#prints the board (explained more in board_print.py)
def board_print(board):
  pr_line = 0
  pr_letter = 0

  for items in board['1']:
    pr_line += 1
    pr_line = str(pr_line)
    for items in board['1']:
      print(board[pr_line][pr_letter],  end=' ')
      time.sleep(0.02)
      pr_letter += 1
    print()
    pr_letter = 0
    pr_line = int(pr_line)
#options menu to change certain variables about the game. explained in print statements below
def options_menu():
  menu = True
  print()
  print("AutoBoat: Chooses the boats randomly for you.")
  print("Rapid Fire: Allows you to shoot multiple shells per round.")
  print("AutoPlace: Places the boats randomly for you (enables AutoBoat as well).")
  print("Boat Overlap: Allow boats to overlap each other.")
  print()
  print("Difficulty options: ")
  print("Hard Mode: Robot uses double fire per round.")
  print("Veteran Mode: Boat placement is randomized and board size is 5x5 (carrier is removed).")
  print("War Mode: Veteran rules apply, but robot now uses triple fire per round. Good luck.")
  print("Go Back")
  print()
  #goes through options_list dictionary and changes certain variables to true depending on input
  while menu == True:
    options = input("Choose what you want to enable (caps sensitive): ")
    if options in options_list:
        if options == 'Go Back':
          break
        if options == 'AutoPlace':
          options_list['AutoBoat'] = True
        if options == 'War Mode':
          options_list['Veteran Mode'] = True
        options_list[options] = not options_list[options]
        options = True
    else:
        print("Option not in list")
        print()

#lists for boat positions and misfire positions (robot only uses misfire positions for simplicity)
boat_positions_robot = []
boat_positions_player = []
player_misfire = []
player_hit = []
robot_misfire = []

#Greeting
print("Welcome to Battleship. This game will put you up against a randomized machine.")
print("Before we set out, we need to get out ships sorted.")

#Options Menu Prompt
settings = input("Would you like to open the options menu? (y/n): ")
if settings == 'y' or settings == 'yes':
  options_menu()
if settings == 'n' or settings == 'no':
  print()
print("boatBot is choosing...")
time.sleep(1)

#boat picker for boatBot
while boats > -1:
  
  #chooses a random boat, line, and column for boatBot
  boat_robot = random.choice(boat_list_robot)
  line_choice_robot = random.choice(lines)
  letter_choice_robot = random.choice(letters)
  #loops if a carrier is placed in the middle (too big for board)
  if line_choice_robot == '4':
    if letter_choice_robot == 'D':
      if boat_robot == 'carrier':
        continue
  #saves the start point of the boat to a list
  boat_position_robot = str(letter_choice_robot) + str(line_choice_robot)
  boat_positions_robot.append(boat_position_robot)

  #checks for overlap on start positions
  if boat_positions_robot.count(boat_position_robot) == 2:
    boat_positions_robot.remove(boat_position_robot)
    boats =+ 1
    continue

  #Chooses the direction the boats will go in
  #Makes sure the boats don't go off the board
  line_robot = int(line_choice_robot)
  space_count = boat_length[boat_robot]
  #dir_robo is used to keep everything slightly more organized
  dir_robo = letter_choice_robot

  #sets up direction options
  direction_setup(space_count, line_robot, dir_robo)

  #randomly selects the direction
  direction_boat_robot = random.choice(direction)
  #takes the column index from letters list and assigns it to boat_number
  boat_number = letters.index(letter_choice_robot)

  #adds all the directions originally removed from the direction list (general cleanup basically)
  direction_reset()
  #removes the boat from the list
  boat_list_robot.remove(boat_robot)

  #Places the boat on the board
  boat_placer(boat_robot, direction_boat_robot, line_choice_robot, letter_choice_robot, bot_list, options_list['Boat Overlap'], boat_list_robot)

  #Subtracts 1 from boats to properly loop
  boats = boats - 1
  #Double checks if the boat list is empty
  if boat_list_robot == []:
    break
  else:
    continue

#Player Boat Pick (sets boats back to 5 for loop, slight delay so everything doesn't just pop in)
boats = 5
print()
time.sleep(1)

#Sets the board up for Veteran Difficulty (if enabled)
if options_list['Veteran Mode'] == True:
  print("New Board: ")
  print()
  board_print(vet_list)
  boat_list_player.remove('Carrier')
  lines.remove('6')
  lines.remove('7')
  letters.remove('F')
  letters.remove('G')
  print()

#boat choices for player
while boat_list_player != []:
  print()
  if options_list['AutoBoat'] == False:
    print(boat_list_player)
  #Chooses random boat when AutoBoat is True
  #Automatic Selection (AutoBoat is enabled when AutoPlace is enabled)
  if options_list['AutoBoat'] == True:
    #delay so there's less of a mess
    time.sleep(0.5)
    boat_player_choice = random.choice(boat_list_player)
  #Manual Selection
  else:
    boat_player_choice = input("Type in a boat from the list above (caps sensitive): ")
    #if it's in the list
    if boat_list_player.count(boat_player_choice) == 1:
      #confirmation
      confirmation_boat = input("You chose " + str(boat_player_choice) + ". Are you sure? (yes / no): ")
      if confirmation_boat == 'yes':
        boat_list_player.remove(boat_player_choice)
        print()
      elif confirmation_boat == 'no':
        boats = boats + 1
        print()
        continue
      #continues if input isnt yes or no
      else:
        print("Continuing...")
        print()
    #prints if something not in the boat list is put in
    else:
      print("Not an option.")
      print()
      boats = boats + 1
      continue
  #Automatic Selection for boat position
  if options_list['AutoPlace'] == True:
    #Automatic position selection for Veteran Mode
    if options_list['Veteran Mode'] == True:
      line_choice_player = random.choice(lines)
      letter_choice_player = random.choice(letters)
    #Automatic selection for normal mode
    else:
      #same as boatBot selection
      line_choice_player = random.choice(lines)
      letter_choice_player = random.choice(letters)
      #exception in case D4 ends up assigned to the Carrier
      if line_choice_player == '4':
        if letter_choice_player == 'D':
          if boat_player_choice == 'Carrier':
            print("Selecting...")
            continue
    #puts the horizontal and vertical position into one variable
    boat_position_player = str(letter_choice_player) + str(line_choice_player)
    boat_positions_player.append(boat_position_player)
    #checks for overlap on start positions
    if boat_positions_player.count(boat_position_player) == 2:
      boat_positions_player.remove(boat_position_player)
      boats =+ 1
      continue
    line_choice_player = int(line_choice_player)
    #Prints the boat and it's position
    
  else:
    #manual selection
    board_print(helpful_board)
    print()
    line_choice_player = input("Choose the line you want to put the boat on (1-7): ")
    #checks if the number is in the lines list and loops if it isn't (breaks when a valid number is inputted)
    if lines.count(line_choice_player) == 0:
      while lines.count(line_choice_player) == 0:
        line_choice_player = input("Enter a line number from 1 to 7: ")
        if lines.count(line_choice_player) == 0:
          print()
          continue
        else:
          print()
          break
    #makes line_choice_player an integer
    line_choice_player = int(line_choice_player)
    #prompts the user for the row they want to put their boat in A-G
    print()
    letter_choice_player = input("Type in the row you want to put the boat in (A-G): ")
    #position invalid message (board is too small for certain position)
    if letter_choice_player == "D":
      if line_choice_player == 4:
        if boat_player_choice == 'Carrier':
          invalid_position = input("Invalid position. Would you like to move it to a random space? (y/n): ")
          #if yes, randomly assigns the boat position
          if invalid_position == 'y':
            print()
            letters.remove(letter_choice_player)
            letter_choice_player = random.choice(letters)
            line_choice_player = random.choice(lines)
          #if no, reloops the boat selection
          if invalid_position == 'n':
            print("Restarting.")
            boat_list_player.append(boat_player_choice)
            boats = boats + 1
            continue
    #if the input is not a valid letter, then loops until it is
    if letters.count(letter_choice_player) == 0:
      while letters.count(letter_choice_player) == 0:
        letter_choice_player = input("Enter a letter from A to G: ")
        if letters.count(letter_choice_player) == 0:
          print()
          continue
        else:
          print()
          break
    #puts the letter and number inputs together to get the position
    #and adds it to a list
    boat_position_player = str(letter_choice_player) + str(line_choice_player)
    boat_positions_player.append(boat_position_player)
    #checks for overlap on start positions
    if boat_positions_player.count(boat_position_player) == 2:
      #restarts if two boats' start positions overlap
      print()
      print("Boat overlaps with another. Resetting.")
      boat_positions_player.remove(boat_position_player)
      boat_list_player.append(boat_player_choice)
      boats = boats + 1
      continue
    #prints the position of the boat and what type it is
    print("Position of " + str(boat_player_choice) + ": " + str(boat_position_player) + ".")
    #Chooses the direction the boats will go in
    #Makes sure the boats don't go off the board
  line_player = int(line_choice_player)
  space_count = boat_length[boat_player_choice]
  dir_play = letter_choice_player
  #sets up direction choices
  direction_setup(space_count, line_player, dir_play)

  #automatic selection
  if options_list['AutoPlace'] == True:
    direction_player = random.choice(direction)

  #manual selection
  else:
    print(direction)
    print()
    direction_player = input("Choose a direction from the list above: ")
    #randomizes direction if it isn't in the list
    if direction.count(direction_player) == 0:
      print("Direction is not in the list. Randomizing...")
      direction_player = random.choice(direction)
      print()

  #adds missing directions back to list
  direction_reset()

  #places the boats on the board
  if options_list['Veteran Mode'] == True:
    boat_placer(boat_player_choice, direction_player, line_choice_player, letter_choice_player, vet_list, options_list['Boat Overlap'], boat_list_player)
  else:
    boat_placer(boat_player_choice, direction_player, line_choice_player, letter_choice_player, player_list, options_list['Boat Overlap'], boat_list_player)
  if boat_list_player.count(boat_player_choice) >= 2:
    boat_list_player.remove(boat_player_choice)
    boats = boats + 1
    continue

  #removes the boat from the boat list
  if boat_list_player.count(boat_player_choice) == 1:
    boat_list_player.remove(boat_player_choice)
    boats = boats - 1
  if options_list['AutoBoat'] == True:
    print("AutoBoat: " + str(boat_player_choice))
  else:
    print("Boat Choice: " + str(boat_player_choice))
  print(str(boat_player_choice) + " position: " + str(boat_position_player))
  print("Direction: " + direction_player)
  #prints the board if AutoPlace is False
  if options_list['AutoPlace'] == False:
    board_print(player_list)
#checks if the list is empty or not
  if boat_list_player == []:
    break
  else:
    continue
  print()
#prints either the veteran game board or the normal one
if options_list['Veteran Mode'] == True:
  board_print(vet_list)
else:
  board_print(player_list)


#Actual Game
global Game
Game = True
print()
print("Locations confirmed. Time for battle.")
while Game == True:
  #Prints if you lose
  if options_list['Veteran Mode'] == True:
  #Prints if all boats are eliminated from the player's board (Veteran Mode)
    win_check(vet_list)
  else:
    #prints if there's no more boats on the player's board (Normal Mode)
    win_check(player_list)

  #Prints if you eliminate all boats from the robot's board
  win_check(bot_list)
  #Game is changed within win_check function via global
  if Game == False:
    board_print(bot_list)
    print('Thanks For Playing!')
    break
  #Turns the player or robot gets
  Turns_player = 1
  Turns_robot = 1

  #options that change the amount of turns boatBot or the player gets
  if options_list['Hard Mode'] == True:
    Turns_robot = 2
  if options_list['War Mode'] == True:
    Turns_robot = 3
  if options_list['Rapid Fire'] == True:
    Turns_player = 3

  #player goes first
  while Turns_player > 0:
    #adds letters and lines to lists previously removed for aiming at the enemy board
    if options_list['Veteran Mode'] == True:
      letters.append('F')
      letters.append('G')
      lines.append('6')
      lines.append('7')

    #prints hit or miss list after the first round
    miss = len(player_misfire)
    hit = len(player_hit)
    if hit > 0 or miss > 0:
      print("Positions hit: " + str(player_hit))
      print("Positions missed: " + str(player_misfire))
      print()
    
    print("AWAITING YOUR COMMAND: ")
    print()
    #Asks the player where they want to fire vertically (loops until valid position)
    player_fire_li = input("Choose the line you're firing on (1-7): ")
    if lines.count(player_fire_li) == 0:
      while lines.count(player_fire_li) == 0:
        player_fire_li = input("Enter a line number from 1 to 7: ")
        if lines.count(player_fire_li) == 0:
          print()
          continue
        else:
          print()
          break
    #converts input to a integer
    player_fire_li = int(player_fire_li)
    print()

    #prompts the player to input a letter from A-G for the horizontal position (loops until valid position)
    player_fire_le = input("Choose the position you want to fire on (A-G): ")
    if letters.count(player_fire_le) == 0:
      while letters.count(player_fire_le) == 0:
        player_fire_le = input("Enter a letter from A to G: ")
        if letters.count(player_fire_le) == 0:
          print()
          continue
        else:
          print()
          break

    #puts together the horizontal and vertical position, used for checking previous hits and misses
    player_fire = str(player_fire_le) + str(player_fire_li)
    #If the position is already chosen, goes back to the start of the player's turn
    if player_misfire.count(player_fire) == 1:
      print("We've fired there before, it's dead sea.")
      print()
      continue
    if player_hit.count(player_fire) == 1:
      print("We've already hit that part.")
      print()
      continue

    #points for the miss/hit board
    miss_hit_board = letters.index(player_fire_le)

    #checks if the player hit anything
    hit_check(player_fire_li, player_fire_le, player_hit, player_misfire, bot_list, player_miss_board)

    #Subtracts 1 from the player's turn, ending it if RapidFire isn't selected
    Turns_player = Turns_player - 1
    #removes letters and numbers for the robots turn (Veteran Mode creates smaller board, throws an error if left in)
    if options_list['Veteran Mode'] == True:
      letters.remove('F')
      letters.remove('G')
      lines.remove('6')
      lines.remove('7')

  ##Robot's turn
  print("ENEMY ATTACK INBOUND!")
  print()
  time.sleep(0.5)
  while Turns_robot > 0:
    #Slowed down to have a smoother transition
    time.sleep(0.1)
    #Robot fire if they're on Veteran difficulty
    if options_list['Veteran Mode'] == True:
      #randomly chooses where it will fire
      robot_fire_li = random.choice(lines)
      robot_fire_le = random.choice(letters)

      #puts the horizontal and vertical positions into a variable, checks for previous instances in robot_misfire list
      robot_fire = str(robot_fire_li) + str(robot_fire_le)
      #checks if the robot already chose that position
      if robot_misfire.count(robot_fire) == 1:
        continue
      else:
        #adds it to the list if it didn't
        robot_misfire.append(robot_fire)

      #checks if anything was hit (misfire isn't taken as parameter, see README)
      hit_check(robot_fire_li, robot_fire_le, None, None, vet_list, None)
      #Prints the veteran board
      board_print(vet_list)

    #normal mode robot fire
    if options_list['Veteran Mode'] == False:
      #randomly chooses a position to fire on
      robot_fire_li = random.choice(lines)
      robot_fire_le = random.choice(letters)

      #puts the horizontal and vertical positions into a variable
      robot_fire = str(robot_fire_li) + str(robot_fire_le)
      #restarts the turn if the robot fired on the position already
      if robot_misfire.count(robot_fire) == 1:
        continue
      else:
        robot_misfire.append(robot_fire)
      #checks if anything was hit (misfire IS taken as parameter, see README)
      hit_check(robot_fire_li, robot_fire_le, None, robot_misfire, player_list, None)
      #prints the player's board
      board_print(player_list)
    
    #subtracts 1 from the robots turn
    Turns_robot = Turns_robot - 1
    print()
    if Turns_robot == 0:
      break
    time.sleep(0.5)
  
  #if the game is still running, prints the player's missed and hit position (README has more details)
  if Game == True:
    print("INCOMING TRANSMISSION...")
    time.sleep(0.2)
    print("PREVIOUS FIRING COORDINATES ACQUIRED.")
    time.sleep(0.1)
    print("SENDING...")
    board_print(player_miss_board)
    continue
  else:
    break
