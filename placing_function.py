#NOTE: this file is NOT required to run Battleship, this is simply a note-taking file. battleship.py is the only file needed for Battleship

#boat_placer takes in length of boats (described in dictionary in Battleship.py), the direction they're pointing (from start position), the line (1-7),
#the column (A-G), and placing_dictionary (bot_list, player_list, or vet_list are ALL inputs (and dictionaries))
def boat_placer(length, direction, line, column, placing_dict):
  #checks if the line is a string, changes it to one if not (used for dictionary indexing)
  if isinstance(line, str) == False:
    line = str(line)
  #gets the index of the column (example: D = 3)
  column = letters.index(column)
  #runs for the entire length of the boat, placing a '0' to represent a boat
  for i in range(boat_length[length]):
    #adds one each time if the direction is set to the right
    if direction == 'right':
      placing_dict[line][column] = '0'
      column += 1
    #subtracts one each time if the direction is set to the left
    if direction == 'left':
      placing_dict[line][column] = '0'
      column -= 1
    #makes the line variable an integer, adds one to it, before converting back into a string
    if direction == 'down':
      placing_dict[line][column] = '0'
      line = int(line)
      line += 1
      line = str(line)
    #makes the line variable an integer, subtracts one from it, before converting back into a string
    if direction == 'up':
      placing_dict[line][column] = '0'
      line = int(line)
      line -= 1
      line = str(line)
  #print statement adds space between player selections, making it easier to read
  print()
