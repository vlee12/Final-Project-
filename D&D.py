import sys

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

class items_or_weapons:
	"""Summary: Players are allowed one of 4 weapons when starting the game in order to be able to do damage. 
    The weapons are represented below as one of 4 methods. Also includes a damage method which calls one of the
    weapons when the player is fighting and calculates the amount of damage done to a monster based on the player’s health.
    Important Comment: we were also considering combining all of the weapon methods into one giant method and just creating
    different items_or_weapons objects for each player.
	Attributes: 
        damage(int): Baseline amount of damage """
	def sword(player):
	    """Summary: Simulates a sword in game which players can use against monsters.
	    Args (player obj): player which receives the sword
	    Side effects: prints out a sword-specific statement when the player uses it. 
	    Returns(int): the amount of damage which this weapon is able to do."""
	def bow(player):
	    """Summary: Simulates archery equipment in game which players can use against monsters.
	    Args (player obj): player which receives the bow
	    Side effects: prints out an archery-specific statement when the player uses it. 
        Returns(int): the amount of damage which this weapon is able to do."""
	def dagger(player):
	    """Summary: Simulates a dagger in game which players can use against monsters. 
	    Args (player obj): player which receives the dagger
	    Side effects: prints out a dagger-specific statement when the player uses it. 
	    Returns(int): the amount of damage which this weapon is able to do."""
    def staff(player): 
	    """Summary: Simulates a staff in game
	    Args (player obj): player which receives the staff
	    Side effects: prints out a staff-specific statement when the player uses it. 
	    Returns(int): the amount of damage which this weapon is able to do."""
    def damage(player_weapon, monster_health):
        """Summary: Using the players' weapon (damage stats) to hurt the monster until the monster's health is empty or the players are dead
        Args(int, int): player_weapon is an integer value which represents the amount of damage a player can do. monster_health- an integer 
        value which represents how much health the monster has left.
        Returns(int): the monster’s health after being attacked by the player.
        """
class spells_and_curses:
	"""Summary: Simulates different types of spells/curses that the player can use. There are a variety of spells which could be used.  
	Attributes: 
        spell_stats(int): baseline spell statistics which are applicable for every spell listed. """
	def potion(Player):
        """Summary: This spell is meant to simulate a potion. Players use this versatile spell for a variety of reasons. 
        Args:
            player(player object): The player which owns the potion.
        Returns
            spell_damage(int): the amount of damage that the item is able to do.""" 
    def healing_spell(player, target_player): 
        """Summary: A healing spell which allows you to heal one of your teammates.
        Args(Player, target_player):	
	        Player(player object): player that owns the spell
	        target_player(player_object): player which is going to get healed. 
            Returns(int): the amount that you would heal another player"""
	def poison_spell(player):
        """Summary: A spell which is supposed to simulate poison. 
        Args(Player): 
        player(player obj) -The player that owns the spell.
        Returns(int): The amount of damage done. Calculated by adding the player statistics plus base damage of spell."""
    def fire_spell(Player):
        """Summary: Fire spell, allows you to deal fire magical damage to enemies.
        Args(Player): 
            player- the player who owns the spell. 
        Returns(int): The amount of damage done. Calculated by adding player statistics plus base damage."""

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