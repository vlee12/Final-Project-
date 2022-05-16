# Final-Project-
A repository of the final project for INST326.

Project:D&D Game 
The only file that is needed to run the program is the D&D.py where it contains all the code to the Dungeons and Dragons game. 

How to run the program: 
From the command line, type “python D&D.py” and the filepath containing custom player attributes like player_strength, player_dexterity, etc to run the program. If the file name of the text file is “DND.txt” then the user would type “python D&D.py DND.txt” in the command line to run the program.
The text file must be in this specific format: 
Player strength:20
Player dexterity:10
Player intelligence:17
Player wisdom:10
Player charisma:10
Player constitution:10

The values of each player attribute can vary but the order of the player attributes must be the same and there should not be a space in between the colon and the value. If the player decides not to use custom values, the game can still be played with the default values of each player attribute. 

Once the command line argument is entered, a welcome message will be displayed. Then it will ask the player’s name and what weapons and spells they want. This will repeat for every player that is playing. Then the program will randomly roll a dice and assign it to a player, whoever rolls the highest will get to choose what to do or where to go next. This will repeat until a monster is encountered in which the player will have the choice to use their weapon or magic to fight the monster until either the player’s health reaches 0 or the monster’s health reaches 0. If the player successfully beats the monster, they will continue onto their path until the game is over. If the player’s health decreases to less than 0, they are considered dead. This game is all about creating your own adventure, choosing the right path, and making the correct choices. In the end, there is no winner or loser, rather it will just display where the player ended up based on their decisions throughout the game. After the user has played through one path, they also have the option of playing the game again and making different choices and seeing how that changes their outcome.

Attribution:
Ana Peshku: dice_roll function, items_or_weapons class, sword class, bow class, dagger class, staff class, spells_and_curses class, potion class, healing_spell class, poison_spell class, fire_spell class, damage function
Dialo Diop: start function, end function 
Victoria Lee: Plot class, main function, Argument Parser class
Yaqi Xu: Player class, Monster class(Witch class, Dragon class)

