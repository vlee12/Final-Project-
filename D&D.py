from argparse import ArgumentParser
import sys
import re
<<<<<<< HEAD

=======
import random
import time
>>>>>>> 004c1d47bf3ae0a9712a574a02c894efcf03fda5
"""Information need: 
Our program will be a choose your own adventure game based on D&D. 
In order for the program to function, the players will initially have to create a character which they will use to play throughout the game. 
This means that the code will need a filepath to a character sheet file or a string input from the player saying that they want to use the default player statistics. 
The character statistics will be stored in a list in the player class, with numerical limitations running from 1-10. 
The players will also have to input their decisions throughout the game and choose a weapon. 
The weapon class needs the str information from which weapon a player will choose. 
The spells and curses class has a very similar information need to the weapon class, but instead players will be choosing which spells they want to use, or if they want to use spells at all. 
The plot class needs a str of what decision will make for each method. 
The start function’s information need is based on the questions the players answer in the very beginning of the game. 
All of this information will be provided to the code through parameters."""



class Player:
    """ Summary: Showing the player’s information, the players’s characstic and their uniquely spells 
    
        Attributes:
            player (str): name of the player
            player_health (int): player's amount of health 
            player_ability (str) : palyer's ability information 
    """
    def __init__(self,player,player_health = None,player_strength = 25, player_dex_dexterity = 8,\
                player_constituiton =10 , player_intelligence = 16, player_wisdom = 10, \
                player_charisma = 10):
        self.player = player
        self.player_health = player_health
        self.player_strength = player_strength
        self.player_dex_dexterity = player_dex_dexterity
        self.player_intelligence = player_intelligence
        self.player_wisdom = player_wisdom
        self.player_charisma = player_charisma
        
        print("For the game, do you want to input the plyaer's information or upload a file to read?")
        choice = input("If you want to make an input, enter 1.\n"
                        "If you want to upload a file, enter 2")
        
        self.player = []
        if choice == "1":
            number_of_players = input("The minimum player require for the game is 1 player,\n"\
                                        "the upper limit is 4 players.\n"\
                                        "How many players you want to have for the game?\n")
            number_of_players = int(number_of_players)
            
            while number_of_players not in range (1,5):
                    number_of_players = input("The minimum player require for the game is 1 player,\n"\
                                        "the upper limit is 4 players.\n"\
                                        "How many players you want to have for the game?\n")
            for player in range(number_of_players):
                name = input("Please enter your player name")
                self.player.append(name)
                        
        elif choice == "2":
            
            filepath = input("Please enter your file name")
            file_read(filepath)
            
     
        
    def file_read(filepath):
        """ Summary: read the text file in encoding UTF-8 to store player's information (ex. strength(int), defense(int)) and pass around classes. Using 
            regular expression to pick up player's information

<<<<<<< HEAD
            Args:
                filepath (str): path to a text file containing player's information
            
            Side effects: 
                Store player's ability and health into two variables for running the game
=======
        Args:
            filepath (str): path to a text file containing player's information
            
        Side effects: 
            Store player's ability and health into two variables for running the game
>>>>>>> 004c1d47bf3ae0a9712a574a02c894efcf03fda5
                
        """
        
        with open (filepath,"r",encoding="utf-8") as f:
            expr = r ''' regex '''
        
            if re.search(expr,player):
                match = re.search(expr,player)
            
                # match function may need to update to correct one
                self.player_health = match.player_health
                self.player_strength = match.player_strength
                self.player_dex_dexterity = match.player_dex_dexterity
                self.player_intelligence = match.player_intelligence
                self.player_wisdom = match.player_wisdom
                self.player_charisma = match.player_charisma
                self.player.append(name)
            else:
                raise ValueError("Invalid input!")
            
            
            
            
class Monster:
    """ Summary: Displaying monster's information in health amount and attack ability
    
        Attributes:
            monster_health (int): monster's amount of health 
            monster_ability (str): monster's ability information 
            monster_att_damage (int): monster's attrack damage per action
            
    """
    def __init__(self,monster_health = 150, monster_att_damage = 15):
        self.monster_health = monster_health
        self.monster_att_damage = monster_att_damage
        
    def monster_attack(self,player,current_health):
        #has the attribute of the health
        """Perform the monster actions after the player’s move, how monster gives attack after
            players attack to monster. When playe's health reach to 0, the player die.

            Args:
                current_health (int): player's current health amount after attacked by players
            
            Side effects:
                The changed amount of health amount of the player.
                
            Return （int）: 
                The player's remaining health amount by monster's damage attack 
            
            Raises: 
                Give the player a description of how much damage the monster does to them, and what kind of 
                ability the monster used
             
        """
        Player.player_health -= self.monster_att_damage
        print("Your helath decreased for .")
        if player.player_health <= 0:
            print(f"{player} died.")
            
        return player.player_health
        
        
class Witch(Monster):
    """ Summary: Subclass of Monster, displaying withch's information as one kind of monster in health amount and ability

    Args:
        Monster (str): a type of monster that can attack to players when they choose a bad path in D&D game
    
    """
    def __init__(self,player, witch_health = 130,witch_att_damage = 17):
        self.witch_health = witch_health
        self.witch_att_damage = witch_att_damaged
   
    def monster_attack(witch_name,player, current_helath):
        """Perform the monster actions after the player’s move, how monster gives attack after
            players attack to monster. Witch will die when its health amount reaches to 0

            Args:
                monster (str): the name of the witch
                player: the name of player
                current_health (int): player's current health amount after attacked by the monster
            
            Side effects:
                The changed amount of health amount of the witch, and the attack caused by the witch 
                according to its ability
                
            Return （int）: 
                The amount of attack by the witch
            
            Raises: 
                Give the player a description of how much damage the witch does to them
             
        """
        Player.player_health -= self.witch_att_damaged
        
        return self.player_health
    
class Dragon(Monster):
    """Summary: Subclass of Monster, displaying dragon's information as one kind of monster 
    in health amount and ability. Dragon will die when its health amount reaches to 0

    Args:
        Monster (str): a type of monster that can attack to players when players choose path in D&D game
        and need to have a battle with the dragon
    """
    def __init__(self,drgaon_health = 140,dragon_att_damage = 20):
        self.drgaon_health = drgaon_health
        self.dragon_att_damage = dragon_att_damage
        
    def monster_attack(self,player,current_health):
        """Perform the dragon actions after the player’s move, how dragon gives attack after
            players attack to dragon

            Args:
                monster (str): the name of the dragon
                current_health (int): current health amount after attacked by players
            
            Side effects:
                The changed amount of health amount of the dragon, and the attack caused by the dragon 
                according to its ability
                
            Return （int）: 
                The amount of attack by the dragon to players
            
            Raises: 
                Give the player a description of how much damage the dragon does to them
             
<<<<<<< HEAD
        """
        Player.player_health -= self.dragon_att_damaged
        return self.player_health
=======
            """
        player_obj -= self.dragon_att_damaged
        return player_obj
>>>>>>> 004c1d47bf3ae0a9712a574a02c894efcf03fda5
        
class items_or_weapons:
	"""Summary: Players are allowed one of 4 weapons when starting the game in order to be able to do damage. 
    The weapons are represented below as one of 4 methods. Also includes a damage method which calls one of the
    weapons when the player is fighting and calculates the amount of damage done to a monster based on the player’s health.
    
    Important Comment: we were also considering combining all of the weapon methods into one giant method and just creating
    different items_or_weapons objects for each player.
    
	Attributes: 
        base_damage(int): Baseline amount of damage
    """
        
    def __init__(self, name = None, base_damage = 25, range = 10):
        self.base_damage = base_damage
        self.range = range
        self.name = name 
    def equip(self):
        print (f"{self.player} has recieved a {self.name}")
    def ability(self):
        print(f"This {self.name} is able to do {self.base_damage}. It has a range of {range}")
    def damage(self, monster):
        monster.monster_health = monster.monster_health - self.base_damage
        return monster.monster_health
    def __str__(self):
        print (f"{self.name}: damage{self.base_damage} range:{self.range}")

class sword(items_or_weapons):
	#"""Summary: Simulates a sword in game which players can use against monsters.
	#Args (player obj): player which receives the sword
	#Side effects: prints out a sword-specific statement when the player uses it. 
	#Returns(int): the amount of damage which this weapon is able to do."""
    def __init__(self):    
        super().__init__()
        if player.player_strength > 10:
            self.base_damage += 10
        self.name = "sword"
class bow(items_or_weapons):
	"""Summary: Simulates archery equipment in game which players can use against monsters.
	Args (player obj): player which receives the bow
	Side effects: prints out an archery-specific statement when the player uses it. 
    Returns(int): the amount of damage which this weapon is able to do."""
    def __init__(self):    
        super().__init__()
        if player.player_wisdom > 9:
            self.base_damage = 30
            self.range = 20
        self.name = "bow"
class dagger(items_or_weapons):
	"""Summary: Simulates a dagger in game which players can use against monsters. 
	Args (player obj): player which receives the dagger
	Side effects: prints out a dagger-specific statement when the player uses it. 
	Returns(int): the amount of damage which this weapon is able to do."""
    def __init__(self):
        super().__init__()
        if player.player_dexterity > 11:
            self.base_damage += 10
        self.name = "dagger"
class staff(items_or_weapons): 
    """Summary: Simulates a staff in game
    Args (player obj): player which receives the staff
    Side effects: prints out a staff-specific statement when the player uses it. 
    Returns(int): the amount of damage which this weapon is able to do.
    """
    def __init__(self):
        super().__init__()
        if player.player_wisdom > 8:
            self.base_damage += 5
        self.name = "staff"
class spells_and_curses:
    """Summary: Simulates different types of spells/curses that the player can use. There are a variety of spells which could be used.  
	Attributes: 
    spell_stats(int): baseline spell statistics which are applicable for every spell listed.
    """
    
    def __init__(self, name = None, spell_stats = 20):
        self.spell_stats = spell_stats
        self.name = name
    def spell_message(self, player):
        print (f"{player} is able to use this {self.name}")
    def spell_use(self):
        print (f"{self.name} has the ability to do {self.spell_stats} damage")
    def spell_message(self):
        print (f"{self.name} has the ability to do {self.spell_stats} amount of damage")
    def spell_damage(self, monster):
        monster.monster_health = monster.monster_health - self.base_damage
        return monster.monster_health
class potion(spells_and_curses):
    """Summary: This spell is meant to simulate a potion. Players use this versatile spell for a variety of reasons. 
    Args:
        player(player object): The player which owns the potion.
    Returns
    spell_damage(int): the amount of damage that the item is able to do.""" 
    def __init__(self):
        super().__init__()
        self.name = "potion"
class healing_spell(spells_and_curses): 
    """Summary: A healing spell which allows you to heal one of your teammates.
    Args(Player, target_player):	
        Player(player object): player that owns the spell
        target_player(player_object): player which is going to get healed. 
        Returns(int): the amount that you would heal another player"""
    def __init__(self):
        super().__init__(self)  
        self.name = "Healing spell"
    def heal(self, player):
        player.health = self.spell_stats + player.health
        return player.health
class poison_spell(spells_and_curses):
    """Summary: A spell which is supposed to simulate poison. 
        Args(Player): 
        player(player obj) -The player that owns the spell.
        Returns(int): The amount of damage done. Calculated by adding the player statistics plus base damage of spell."""
    def __init__(self):
        super().__init__() 
        self.name = "posion spell"
    def wait_damage(self, monster):
        print ("This spell does damager over time")
        conditional = self.spell_stats
        while conditional > 0:
            monster.monster_health -= 5
            time.sleep(5)
            conditional -= 5
            print (f"{monster.monster_health}")   
        return monster.monster_health
class fire_spell(spells_and_curses):
    """Summary: Fire spell, allows you to deal fire magical damage to enemies.
    Args(Player): 
        player- the player who owns the spell. 
    Returns(int): The amount of damage done. Calculated by adding player statistics plus base damage."""
    def __init__(self):
        super().__init__() 
        self.name = "fire spell"
<<<<<<< HEAD
        
def damage(player_lst, monster):
=======
def damage(player_lst, monster, spells_dict, weapon_dict):
>>>>>>> 004c1d47bf3ae0a9712a574a02c894efcf03fda5
    """Summary: Using the players' weapon (damage stats) to hurt the monster until the monster's health is empty or the players are dead
    Args(int, int): player_weapon is an integer value which represents the amount of damage a player can do. monster_health- an integer 
    value which represents how much health the monster has left.
    Returns(int): the monster’s health after being attacked by the player.
    """
    print (f"You have approached this monster, please make a role to see who will attack first")
    damage_dict = dice_roll(player_lst)
    player_count = 0
    for player in player_lst:
        if monster.monster_health > 0 & damage_dict[player_count].health > 0:
            question=input(f"{damage_dict[player_count]}, would you like to attack? (y/n)")
            while question != "y" or "n":
                print ("invalid input please enter another option")
                question=input(f"{damage_dict[player_count]}, would you like to attack? (y/n)")
            if question == "y":
                question2 = input("Would you like to use your weapon or magic?")
                while question2 != "weapon" or "magic":
                    print ("invalid input please enter another option")
                    question2 = input("Would you like to use your weapon or magic?")
                if question2 == "weapon":
                    damage_dict[player_count].spell.damage(monster)
                elif question2 == "magic":
<<<<<<< HEAD
                    if player.spell == "heal":
=======
                    if spell_dict.get(damage_dict[player_count]) == "healing_spell":
>>>>>>> 004c1d47bf3ae0a9712a574a02c894efcf03fda5
                        heal_player = input("Which player would you like to heal?")
                        player.healing_spell.heal(heal_player)
                    damage_dict[player_count].spell.spell_damage(monster)
                print (f"Your turn is now over, it's the {monster}'s turn to attack")
                monster.monster_attack()
            elif question == "n":
                print (f"It's the {monster}'s turn to attack")
                monster.monster_attack()
            player_count += 1
        elif monster.monster_health == 0:
            print ("Success! you have killed the monster")
        elif damage_dict[player_count].health == 0:
            print (f"{damage_dict[player_count].health} has died. Rest in peace")
            del(damage_dict[player_count])
class Plot:
    """Keep track of the player's choice and location of the player on the plot/map.
    
    Attributes:
    player (str): players that are playing 
    """
    def first_choice(player_lst):
        """ Asks the player with the highest dice roll value which path they want to choose.
        
        Returns:
        str: player's decision
        
        Side effect:
        prints the next location and what is present at that location (monster, weapon, etc)"""
        
        highest_roll = dice_roll(player_lst)
        print(f'{highest_roll[0]} you rolled the highest, you get to choose the path.')
        decision = input('What path do you want to choose? Forest, Country, City')
        if decision == 'Forest':
            first_location = 'forest'
            print('Your first location is a Dragon Encounter.')
        elif decision == 'Country':
            first_location = 'country'
            print('Your first location is water encounter.')
        elif decision == 'City':
            first_location = 'city'
            print('Your first location is an item encounter.') 
        else:
            raise ValueError('Invalid input')
        return first_location      
    def second_choice(player_lst, first_location, weapon_dict):
        """ Asks the players which path they want to choose.
        
        Args:
        first_location(str): location of the previous round
        
        Returns:
        str: player's decision
        
        Side effect:
        prints the next location and what is present at that location (monster, weapon, etc)"""
        
        highest_roll = dice_roll(player_lst)
        print(f'{highest_roll[0]} you rolled the highest, you get to choose the path.')
        if first_location == 'forest':
            second_decision = input('Would you like to fight or flee the Dragon?')
            if second_decision == 'fight':
                damage(Dragon)
                seocnd_location = 'lost'
                print('Your next location is the middle of nowhere.')
            elif second_decision == 'flee':
                second_location = 'NPC'
                print('Your next location is a NPC encounter.')
            else:
                raise ValueError('Invalid input')
        if first_location == 'country':
            second_decision = input('Would you like to sail or stay on land?')
            if second_decision == 'sail':
                second_location = 'lost'
                print('You have landed in the middle of nowhere.')
            elif second_decision == 'stay':
                second_location = 'witch'
                print('Your next location is a witch encounter.')
            else:
                raise ValueError('Invalid input')
        if first_location == 'city':
            second_decision = input('Would you like to take the item or pass?')
            if second_decision == 'take the item':
                item = input('Please choose an item: sword, bow, dagger, staff')
                weapon_dict[player] = item
                second_location = 'NPC'
                print('Your next location is a NPC encounter.')
            elif second_decision == 'pass':
                second_location = 'witch'
                print('Your next location is a witch encounter.')
            else:
                raise ValueError('Invalid input')
        return second_location
        
    def third_choice(player_lst, second_location, weapon_dict):
        """Asks the player their third and final choice.
        
        Args:
        player(str): player with highest dice roll
        previous location(str): location of the previous round
        
        Returns:
        str: player's decision
        
        Side effect:
        prints the ending destination for the current player"""
        
        highest_roll = dice_roll(player_lst)
        print(f'{highest_roll[0]} you rolled the highest, you get to choose the path.')    
        if second_location == 'NPC':
            third_decision = input('Would you like to ignore or help the NPC?')
            if third_decision == 'help':
                npc_decision = input("Hi, I'm Gunner. Would you like to get a random item or fight the monster?")
                if npc_decision == 'random item':
                    list_of_items = ['sword', 'bow', 'dagger', 'staff']
                    rand_item = random.choice(list_of_items)
                    weapon_dict[player] = rand_item
                elif npc_decision == 'fight the monster':
                    Witch()
                else:
                    raise ValueError('Invalid input')    
                third_location = 'get magic'
                print('Your final action will be getting a reward.')
            elif third_decision == 'ignore':
                third_location = 'curse'
                print('You will get cursed.')
            else:
                raise ValueError('Invalid input')
        elif second_location == 'witch':
            third_location = input('Would you like to run or fight the witch?')
            if third_decision == 'fight':
                Witch()
                third_location = 'curse'
                print('You will get cursed.')
            elif third_decision == 'run':
                third_location = 'get magic'
                print('Your final action will be getting a reward.')
            else: 
                raise ValueError('Invalid input') 
        elif second_location == 'lost':
            third_location = 'starvation'
            print('Sorry, there is nowhere to go anymore.')
        return third_location 
    
    def final_location(third_location):
        """Prints the final location and end result of the game.
        
        Args:
        third_location(str): end location as a result of previous decision
        
        Side effect:
        prints the result of the game
        """

        print('Your party has died of starvation') if third_location == 'starvation' else print('You have been cursed, you lost!') if third_location == 'curse' else print('You have obtained magic!')

def start(player):
    """ Players have the opportunity to choose information, roll a dice and 
    based on the roll they get to choose what weapon they want
    
    Args:
    player(str): amount of players being chosen/dice roll
    
    Returns: 
    Returns the highest dice for a player
    
    Side Effects:
    Prints how many pkayers that are wanted to play in that round
    
    """
<<<<<<< HEAD
    
=======
    player_lst = [x for x in range(int(player))]
    print("PLAYERLIST: ", player_lst)
    player_dict = dice_roll(player_lst)
    #return player_dict[0]
    sword = sword()
    bow  = bow()
    staff = staff()
    dagger = dagger()
    healing_spell = healing_spell()
    fire_spell = fire_spell()
    poison_spell = poison_spell()
    weapon_dict = {}
    spells_dict = {}
    for player in player_dict.keys():
           option = input("what weapon would you like to choose? Enter:sword,bow,dagger,staff")
           if option == "sword":
               weapon_dict[player] = sword
           else:
               print("bow,dagger,staff")
          
               if option == "bow":
                   weapon_dict[player] = bow
               else:
                   print("dagger,staff")
              
                   if option == "dagger":
                       weapon_dict[player] = dagger
                   else:
                       print("staff")
          
                       if option == "staff":
                           weapon_dict[player] = staff
                       else:
                           print("Return back to weapon objects")
                      
          
           spell_option = input("what spell would you like to choose? Enter: healing_spell, poison_spell, fire_spell ")
           if spell_option == "healing_spell":
               spells_dict[player] = healing_spell
           else:
               print("poison_spell, fire_spell")
              
           if spell_option == "poison_spell":
               spells_dict[player] = poison_spell
           else:
               print("fire_spell")
          
           if spell_option == "fire_spell":
               spells_dict[player] = fire_spell
           else:
               print("please choose spell")
   #return player_dict[0]
    len(player_dict)
    return spells_dict and weapon_dict

>>>>>>> 004c1d47bf3ae0a9712a574a02c894efcf03fda5
def end(player):
    """ outputs the ending player statistics and whether or not they made good 
        decisions throughout the game
    Args:
    player(str): amount of players being chosen/dice roll
    
    Returns:
     the ending player statistics
   """
def damage(player_lst, monster, spells_dict, weapon_dict):
    """Summary: Using the players' weapon (damage stats) to hurt the monster until the monster's health is empty or the players are dead
    Args(int, int): player_weapon is an integer value which represents the amount of damage a player can do. monster_health- an integer 
    value which represents how much health the monster has left.
    Returns(int): the monster’s health after being attacked by the player.
    """
    #var = start(player)
    print (f"You have approached this monster, please make a role to see who will attack first")
    damage_dict = dice_roll(player_lst)
    player_count = 0
    for player in player_lst:
        if monster.monster_health > 0 & damage_dict[player_count].health > 0:
            question=input(f"{damage_dict[player_count]}, would you like to attack? (y/n)")
            while question != "y" or "n":
                print ("invalid input please enter another option")
                question=input(f"{damage_dict[player_count]}, would you like to attack? (y/n)")
            if question == "y":
                question2 = input("Would you like to use your weapon or magic?")
                while question2 != "weapon" or "magic":
                    print ("invalid input please enter another option")
                    question2 = input("Would you like to use your weapon or magic?")
                if question2 == "weapon":
                    weapon_dict.get(damage_dict[player_count]).damage(monster)
                elif question2 == "magic":
                    if spells_dict.get(damage_dict[player_count]) == "healing_spell":
                        heal_player = input("Which player would you like to heal?")
                        healing_spell.heal(heal_player)
                    else:
                        spells_dict.get(damage_dict[player_count]).spell_damage(monster)
                print (f"Your turn is now over, it's the {monster}'s turn to attack")
                monster.monster_attack()
            elif question == "n":
                print (f"It's the {monster}'s turn to attack")
                monster.monster_attack()
            player_count += 1
        elif monster.monster_health == 0:
            print ("Success! you have killed the monster")
        elif damage_dict[player_count].health == 0:
            print (f"{damage_dict[player_count].health} has died. Rest in peace")
            del(damage_dict[player_count])
def main(filepath):
    """Open and read the file.
    
    Args:
    filepath(file): filepath to the text file which includes the player's character of choice.
    
    Side effect:
    reads the text file """
    
    start()
    game = Plot()
    game.first_choice()
    game.second_choice()
    game.third_choice()
    game.final_location()
    end()
    
def parse_args(arglist):
    """Process command line arguments.
    
    Args:
    arglist(list of str): arguments from the command line
    
    Returns:
    namespace: the parsed arguments, as a namespace."""  
    
    parser = ArgumentParser()
    parser.add_argument('filepath', help = 'path to player text file')
    return parser.parse_args(arglist) 
        
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)