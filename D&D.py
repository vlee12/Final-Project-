import sys
import random 
import time
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



class player:
    """ Summary: Showing the player’s information, the players’s characstic and their uniquely spells 
    
        Attributes:
            player_health (int): player's amount of health 
            Player_ ability (str) : palyer's ability information 
    """
        def file_read(filepath):
            """ Summary: read the text file in encoding UTF-8 to store player's information (ex. strength(int), defense(int)) and pass around classes. Using 
            regular expression to pick up player's information

            Args:
                filepath (str): path to a text file containing player's information
            
            Side effects: 
                Store player's ability and health into two variables for running the game
            """
class Monster:
    """ Summary: Displaying monster's information in health amount and attack ability
    
        Attributes:
            monster_health (int): monster's amount of health 
            monster_ability (str): monster's ability information 
            
    """
        def monster_attack(monster,current_health):
            """Perform the monster actions after the player’s move, how monster gives attack after
            players attack to monster. When monster's health reach to 0, the monster die.

            Args:
                monster (str): the name of the monster
                current_health (int): current health amount after attacked by players
            
            Side effects:
                The changed amount of health amount of the monster, and the attack caused by the monster 
                according to its ability
                
            Return （int）: 
                The amount of attack by the monster 
            
            Raises: 
                Give the player a description of how much damage the monster does to them, and what kind of 
                ability the monster used
             
            """
class Witch(Monster):
    """ Summary: Subclass of Monster, displaying withch's information as one kind of monster in health amount and ability

    Args:
        Monster (str): a type of monster that can attack to players when they choose a bad path in D&D game
    
    """
    def monster_attack(witch_name,current_helath):
            """Perform the monster actions after the player’s move, how monster gives attack after
            players attack to monster. Witch will die when its health amount reaches to 0

            Args:
                monster (str): the name of the witch
                current_health (int): current health amount after attacked by players
            
            Side effects:
                The changed amount of health amount of the witch, and the attack caused by the witch 
                according to its ability
                
            Return （int）: 
                The amount of attack by the witch
            
            Raises: 
                Give the player a description of how much damage the witch does to them
             
            """
    
class Dragon(Monster):
    """Summary: Subclass of Monster, displaying dragon's information as one kind of monster 
    in health amount and ability. Dragon will die when its health amount reaches to 0

    Args:
        Monster (str): a type of monster that can attack to players when players choose path in D&D game
        and need to have a battle with the dragon
    """
    def monster_attack(dragon_name,current_health):
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
             
            """
# " just trying to see if this works lol"
def dice_roll(player_lst):
    min = 1
    max = 20
    player_roll = {}
    for player in player_lst:
        roll= random.randint(min, max)
        player_roll[player] = roll
        print(f"{player} has rolled a {roll}")
    sorted_dict = sorted(player_roll.items(), key = lambda num: num[1], reverse=True)
    return sorted_dict
class items_or_weapons():
	"""Summary: Players are allowed one of 4 weapons when starting the game in order to be able to do damage. 
    The weapons are represented below as one of 4 methods. Also includes a damage method which calls one of the
    weapons when the player is fighting and calculates the amount of damage done to a monster based on the player’s health.
    Important Comment: we were also considering combining all of the weapon methods into one giant method and just creating
    different items_or_weapons objects for each player.
	Attributes: 
        base_damage(int): Baseline amount of damage """
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
	"""Summary: Simulates a sword in game which players can use against monsters.
	Args (player obj): player which receives the sword
	Side effects: prints out a sword-specific statement when the player uses it. 
	Returns(int): the amount of damage which this weapon is able to do."""
    def __init__(self):    
        super().__init__()
        if player.player_strength > 10:
            self.base_damage = super.base_damage + 10
        self.name = "sword"
class bow(items_or_weapons):
	"""Summary: Simulates archery equipment in game which players can use against monsters.
	Args (player obj): player which receives the bow
	Side effects: prints out an archery-specific statement when the player uses it. 
    Returns(int): the amount of damage which this weapon is able to do."""
    def __init__(self):    
        super().__init__()
        if player.player_wisdom > 9:
            self.base_damage = super.base_damage + 5
            self.range = super.range + 15
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
	Returns(int): the amount of damage which this weapon is able to do."""
    def __init__(self):
        super().__init__()
        if player.player_wisdom > 8:
            self.base_damage += 5
        self.name = "staff"
class spells_and_curses:
	"""Summary: Simulates different types of spells/curses that the player can use. There are a variety of spells which could be used.  
	Attributes: 
        spell_stats(int): baseline spell statistics which are applicable for every spell listed. """
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
def damage(player_lst, monster):
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
                    if player.spell == "heal":
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
    def first_choice(highest_roll):
        """ Asks the player with the highest dice roll value which path they want to choose.
        
        Args:
        player(str): player with highest dice roll
        
        Returns:
        str: player's decision
        
        Side effect:
        prints the next location and what is present at that location (monster, weapon, etc)"""
        
    def second_choice(highest_roll, previous_location):
        """ Asks the players which path they want to choose.
        
        Args:
        player(str): player with highest dice roll
        previous location(str): location of the previous round
        
        Returns:
        str: player's decision
        
        Side effect:
        prints the next location and what is present at that location (monster, weapon, etc)"""
        
    def third_choice(highest_roll, previous_location):
        """Asks the player their third and final choice.
        
        Args:
        player(str): player with highest dice roll
        previous location(str): location of the previous round
        
        Returns:
        str: player's decision
        
        Side effect:
        prints the ending destination for the current player"""

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
    
def end(player):
    """ outputs the ending player statistics and whether or not they made good 
        decisions throughout the game
    Args:
    player(str): amount of players being chosen/dice roll
    
    Returns:
     the ending player statistics
   """
   
def main(filepath):
    """Open and read the file.
    
    Args:
    filepath(file): filepath to the text file which includes the player's character of choice.
    
    Side effect:
    reads the text file """
    
def parse_args(arglist):
    """Process command line arguments.
    
    Args:
    arglist(list of str): arguments from the command line
    
    Returns:
    namespace: the parsed arguments, as a namespace."""   
        
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)