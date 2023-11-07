# Battleship
Battleship built in Python. Runs through the terminal or command prompt. 



# Notes About The Project

Battleship in Python is made compeletely in Python and runs in the terminal or command prompt, specifically using print statements for any sort of display.

I recently reprogrammed the entire project, due to the length of the file making it hard to read. This brought the size down from ~1600 lines to ~770 (including comments)
If any errors are found while running, please leave a comment on the main Battleship file

Battleship runs off of one .py file. Any other ones are used to explain any functions and their parameters in-depth. You are not required to download these files to play Battleship, but feel free to read them nonetheless.

If there's a more recent version of Battleship uploaded to my GitHub page, unless mentioned, it should be the best working version of the project.



# Certain Design Choices

The Board Size:
The board size was shrunk from a 10x10 to a 7x7 by accident when I designed this project in early 2022. By the time I found out, it was already too late to fix it.
I've kept it this way due to how unique it makes the game feel and to keep the length of games shorter.

Game Customization Via The Options Menu
The addition of the options menu was for unique experiences however many times you've played the game. The options menu used to lock other options. This has since been removed for variety.
- AutoPlace and AutoBoat was for people who wanted to get to the game faster and not have to set up boards.
- Rapid Fire is used for getting through the game easier or just about whatever you want to do.
- Hard Mode is for players who want a slightly harder challenge.
- Veteran Mode is for players who want to roll the dice and see if they can truly master the sea.
- War Mode, as the name implies, gives boatBot (will get to the name later) the power of a war fleet, requiring a vast amount of luck to win the War.

Each mode can be combined and changed about for fun. Combining a lot of different, however, may cause issues.

# Smaller Modifications
- Veteran Mode boatBot

If you've seen the code, you've might have noticed that when boatBot fires in Veteran Mode, the robot's misfire list isn't taken in as a parameter.
This was to give the player a chance, as both War Mode and Veteran Mode make it extremely difficult to win by itself, so it will occasionally hit the same space twice or a few more times.
If you wish to enable this, go to line 733 and make the change below:

* hit_check(robot_fire_li, robot_fire_le, None, None, vet_list, None)
* Changing 4th parameter to robot_misfire
* hit_check(robot_fire_li, robot_fire_le, None, robot_misfire, vet_list, None)
*                                                   ^

- boatBot's Name

boatBot's name was a random typo I made when reprogramming the project. I decided to keep it in as a name.
boatBot refers to the randomizer you play against. Not giving it a name didn't feel right, and I couldn't find a good one for it.
Thus, boatBot was born.

-The Miss-Hit board comment on line 762

The reason for the player having one and boatBot not having one is because... boatBot doesn't need one, it uses a list.
I found lists repetitive to look at while first developing the game part of the project, which resulted in the creation of the player_miss_board.
Despite the name, it holds both the misses AND the hits.


# Final Notes

Will This Project Continue:
I'll still work on Battleship from time to time, just less so. Some future features I plan on adding are listed below.

Future Plans For The Project:
One of the main ones I've thought about is an online connection. However, that'd require me to familiarize myself with that facet of Python, so it may take a bit.
Another one that might come sooner is a TwoPlayer mode. Due to the massive code cleanup I did, this has become more viable to add in.

Neither of these things have ETA's, but they will arrive someday.
