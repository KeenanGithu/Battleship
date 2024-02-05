#takes in 3 parameters
#spaces is the amount of space a boat takes up
#line_count is the horizontal line a boat's starting position is on (the y/number in this case)
#the letter is the vertical line a boat's starting position is on (the x/letter in this case)
def direction_setup(spaces, line_count, letter):
  global direction
  #veteran mode doesn't have carrier, so there's no 4 spaces
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
#refills the direction list for next cycle 
def direction_reset():
  global direction
  direction = []
  direction.append('up')
  direction.append('down')
  direction.append('right')
  direction.append('left')
