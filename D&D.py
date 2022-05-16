from argparse import ArgumentParser
import sys
import re
import random
import time

class Player():
    """Showing the player’s information, the player's name, the player’s weapon and their uniquely spells for running the game. 
    Using regex to look up player's strgenth, dexterity, intelligence, wisdom, charisma,and constitution while player's health is 
    default value
    
    Attributes:
        plyaer_health (int) : default amount of player's health amount
        player_strength (int) : player's strength
        player_intelligence (int) : player's intelligence
        player_wisdom (int) : player's wisdom
        player_charisma (int) : player's charisma 
        player_constitution (int) : player's constituation 
        
    """
    def __init__(self, player_name, weapon, spell, filepath):
        """Setting up attributes for the Player() and using filehandle to open the upload file. Also include useing regex to look up player's 
        character statistics in strgenth, dexterity, intelligence, wisdom, charisma,and constitution.
    
        Args:
            player_name (str): the name of the player
            weapon (str): player can pick a weapon to attack monster, weapon can be bow, dagger, sword, or staff
            spell (str): player's sepll that can heal team members, or cause damage by using postion spell or fire spell when a group of players ecounter monster
            filepath (str): a string of filepath for opening file and store player's statistics to variables
            
        Side effects: 
            Open the filepath and store player's strgenth, dexterity, intelligence, wisdom, charisma, constitution, spell, weapon as variables that can
        passing around classes for use
        """
        self.player_name = player_name
        self.player_health = 150
        expr = r'''\d+'''
        with open(filepath, 'r', encoding="utf-8") as f:
            line = f.readlines()
            self.player_strength = int(re.search(expr, line[0]).group(0))
            self.player_dexterity = int(re.search(expr, line[1]).group(0))
            self.player_intelligence = int(re.search(expr, line[2]).group(0))
            self.player_wisdom = int(re.search(expr, line[3]).group(0))
            self.player_charisma = int(re.search(expr, line[4]).group(0))
            self.player_constitution = int(re.search(expr, line[5]).group(0))
        self.weapon= weapon
        self.spell= spell
        

class Monster:
    """Including monster's information of each type of monster's health and attack damage. 
    
    Attributes:
        monster_health (int) : the default value of monster's health
        monster_att_damage (int) : the default value of monster's attack damage
        
    """
    def __init__(self,monster_health = 150, monster_att_damage = 15):
        """Set up Monster's default value of health and attack damage 
        Args:
            monster_health (int, optional): Monster's health. Defaults to 150.
            monster_att_damage (int, optional): Monster's attack damage. Defaults to 15.
        """
        self.monster_health = monster_health
        self.monster_att_damage = monster_att_damage
    def monster_attack(self, player):
        """A calculation that calculate player's current health amount after monster take the damage to the player
        Args:
            player: the current player who aginst to the monster
        
        Side effects:
            Return current player's health amount and display death status if the player's health is euqal or less than 0, and display
            player's death 
        """
        
        player.player_health -= self.monster_att_damage
        print(f"{player.player_health}")
        if player.player_health <= 0:
            print(f"{player} died.")  
class Witch(Monster):
    """Subclass of Monster()
    Attributes: 
        monster_health (int) : the default value of monster's health
        monster_att_damage (int) : the default value of monster's attack damage
    
    """
    def __init__(self, monster_health = 130, monster_att_damage = 17):
        """Set up witch's attributes in its health and attack damage
        Args:
            monster_health (int, optional): Witch's health. Defaults to 130.
            monster_att_damage (int, optional): Wtich's attack damage. Defaults to 17.
        """
        self.monster_name = "Witch"
        self.monster_health = monster_health
        self.monster_att_damage = monster_att_damage
    def monster_attack(self, player):
        """A calculation that calculate current player's health after taking damage from Witch
        Args:
            player (str): the current player's name who agsinst to the Witch
            
        Side effects:
            Return player's current health after witch take damage action to player and if the player's health is 0 or negative, 
        display player died
        
        """
        player.player_health -= self.monster_att_damage
        print(f"Player health is now {player.player_health}.")
        if player.player_health <= 0:
            print(f"{player} died.")  
class Dragon(Monster):
    """Subclass of Monster()
    Attributes: 
        monster_health (int) : the default value of monster's health
        monster_att_damage (int) : the default value of monster's attack damage
    """
    def __init__(self, monster_health = 140, monster_att_damage = 20):
        """Set up dragon's attributes in its health and attack damage
        Args:
            monster_health (int, optional): Dragon's amount of health. Defaults to 140.
            monster_att_damage (int, optional): Dragon's attack damage. Defaults to 20.
        """
        self.monster_name = "Dragon"
        self.monster_health = monster_health
        self.monster_att_damage = monster_att_damage
    def monster_attack(self, player):
        """A calculation that calculate current player's health after taking damage from Dragon
        Args:
            player (str): the current player's name who agsinst to the Dragon
        
        Side effects: 
            Return player's current health after witch take damage action to player, and if the player's health is 0 or negative, 
        display player died
        """
        player.player_health -= self.monster_att_damage
        print(f"Player health is now {player.player_health}.")
        if player.player_health <= 0:
            print(f"{player} died.")  
def dice_roll(player_lst):
    """This method assigns players a number from 1-20 and organizes the players based on the number they were given
    Args:
        player_lst (list): A list of player objects
    Side Effects: 
        prints out "player name has rolled a #"
    Returns:
        sorted_dict (dictionary): player objects are the index and the number is the value"""
    min = 1
    max = 20
    player_roll = {}
    for player in player_lst:
        roll= random.randint(min, max)
        player_roll[player] = roll
        print(f"{player.player_name} has rolled a {roll}")
    sorted_dict = sorted(player_roll.items(), key = lambda num: num[1], reverse=True)
    return sorted_dict
class items_or_weapons:
    """The parent class of sword, dagger, staff, and bow. Is meant to simulate a fantasy weapon by giving it base damage and abilities
    Attributes:
        base_damage(int): represents the amount of damage done by the weapon
        range (int): represents the range of the weapon
        name (str): the name of the weapon"""
    def __init__(self, name = None, base_damage = 25, range = 10):
        """Assigns the attributes of the items and weapons class
        Args:
            base_damage(int): represents the amount of damage done by the weapon
            range (int): represents the range of the weapon
            name (str): the name of the weapon"""
        self.base_damage = base_damage
        self.range = range
        self.name = name
    def equip(self):
        """Prints out a statment that equips the weapon
        Side Effects:
            Prints out a statement which names the player and their weapon"""
        print (f"{self.player} has recieved a {self.name}")
    def ability(self):
        """Prints out a statment that represents the ability of the weapon
        Side Effects:
            Prints out a statement which names the player and their weapon"""
        print(f"This {self.name} is able to do {self.base_damage}. It has a range of {range}")
    def item_damage(self, monster):
        """Calculates the amount of damage an item is able to do to a monster
        Args:   
            monster (monster obj): Either a witch or a dragon class instantiation
        Returns:
            monster_health (int): a numerical representation of the monster's health"""
        monster.monster_health = monster.monster_health - self.base_damage
        return monster.monster_health
    def __str__(self):
        """An init method which prints out a statement representation of the item/weapon
        Side effects:
            Prints out a str representation of the item/weapon"""
        print (f"{self.name}: damage{self.base_damage} range:{self.range}")
class sword(items_or_weapons):
    """A child class of items_or_weapons A simulation of a sword.
    Args:
        items_or_weapons(class): the parent class of sword."""
    def __init__(self):
        """Assigns the attributes of the sword class. Calls the init method of the items_or_weapons class.
        """    
        super().__init__()
        self.name = "sword"
class bow(items_or_weapons):
    """A child class of items_or_weapons A simulation of a bow.
    Args:
        items_or_weapons(class): the parent class of bow."""
    def __init__(self): 
        """Assigns the attributes of the bow class. Calls the init method of the items_or_weapons class.
        """       
        super().__init__()
        self.name = "bow"
class dagger(items_or_weapons):
    """A child class of items_or_weapons A simulation of a dagger.
    Args:
        items_or_weapons(class): the parent class of dagger."""
    def __init__(self):
        """Assigns the attributes of the dagger class. Calls the init method of the items_or_weapons class.
        """    
        super().__init__()
        self.name = "dagger"
class staff(items_or_weapons):
    """A child class of items_or_weapons A simulation of a staff
    Args:
        items_or_weapons(class): the parent class of staff"""
    def __init__(self):
        """Assigns the attributes of the staff class. Calls the init method of the items_or_weapons class.
        """    
        super().__init__()
        self.name = "staff"
class spells_and_curses:
    """The parent class of potion, healing_spell, posion_spell, fire_spell. Is meant to simulate a fantasy spell by giving it base damage and abilities
    Attributes:
        spell_stats(int): represents the amount of damage done by the spell
        name (str): the name of the spell"""
    def __init__(self, name = None, spell_stats = 20):
        """Assigns the attributes to the spells_and_curses class
            Attributes:
                spell_stats(int): amount of damage a spell can do 
                name(str): represents the name of a string"""
        self.spell_stats = spell_stats
        self.name = name
    def spell_message(self, player):
        """Prints out the name of the player and their spell name
        Args:
            player(player obj): A player which recieves the spell object
        Side effects:
            prints out a statement about the player being able to use a spell"""
        print (f"{player} is able to use this {self.name}")
    def spell_use(self):
        """Prints out the name of the player and their spell name
        Side effects:
            prints out a statement about the player and their spell damage"""
        print (f"{self.name} has the ability to do {self.spell_stats} damage")
    def spell_damage(self, monster):
        """Calcuates the amount of monster health left after a player uses one of their spells
        Returns:
            monster.monster_health(int): an attribute of the monster which represents its health"""
        monster.monster_health = monster.monster_health - self.spell_stats
        return monster.monster_health
class potion(spells_and_curses):
    """The child class of spells_and_curses. Is meant to simulate a potion
        Attributes:
            spell_stats(int): represents the amount of damage done by the spell
            name (str): the name of the spell"""
    def __init__(self):
        """Assigns the attributes of the potion class. Calls the init method of the spells_and_curses class.
        """    
        super().__init__()
        self.name = "potion"
class healing_spell(spells_and_curses):
    """The child class of spells_and_curses. Is meant to simulate a potion
        Attributes:
            spell_stats(int): represents the amount of damage done by the spell
            name (str): the name of the spell"""
    def __init__(self):
        """Assigns the attributes of the potion class. Calls the init method of the spells_and_curses class.
        """ 
        super().__init__(self)  
        self.name = "Healing spell"
    def heal(self, player):
        """Increases a player's health based on the integer value of spell_stats
        Args:
            player(player_obj): the player which will get healed
        Returns:
            player.health (int): an attribute of player which represents their health"""
        player.health = self.spell_stats + player.health
        return player.health
class poison_spell(spells_and_curses):
    """The child class of spells_and_curses. Is meant to simulate a potion
        Attributes:
            spell_stats(int): represents the amount of damage done by the spell
            name (str): the name of the spell"""
    def __init__(self):
        """Assigns the attributes of the potion class. Calls the init method of the spells_and_curses class."""    
        super().__init__()
        self.name = "posion spell"
    def wait_damage(self, monster):
        """The damage of the posion class. Prints out a damage message and subtracts from the monster's health every 5 second
        Side effects:   
            prints out a message about the spell samage
        Returns:
            monter.monster_health(int): an attribute of the monster class which represents it's health."""
        print ("This spell does damager over time")
        conditional = self.spell_stats
        while conditional > 0:
            monster.monster_health -= 5
            time.sleep(5)
            conditional -= 5
            print (f"{monster.monster_health}")  
        return monster.monster_health
class fire_spell(spells_and_curses):
    """The child class of spells_and_curses. Is meant to simulate a potion
        Attributes:
            spell_stats(int): represents the amount of damage done by the spell
            name (str): the name of the spell"""
    def __init__(self):
        """Assigns the attributes of the potion class. Calls the init method of the spells_and_curses class."""
        super().__init__()
        self.name = "fire spell"
def start(filepath):
    """ Begins the game Dungeons and Dragons. Allows player to choose weapon and spell that they desire

    Args:
        filepath (string): 
        This is the string of a filepath which is used to open the file and 
        store the player's statistics to variables

    Returns:
        player_return: 
        This returns the information that the player accquired. 
        Such as their weapon choice and the specific spell that they choose. 
    """
    num = int(input("Welcome to D&D, how many players do you want in your party"))
    player_lst= [None] * num
    player_return = []
    player_sword = sword()
    player_bow = bow()
    player_dagger = dagger()
    player_staff = staff()
    player_potion = potion()
    player_healing =  healing_spell()
    player_fire = fire_spell()
    player_poison = poison_spell()
    for i in player_lst:
        player_name = input("Input your player's name: ")
        weapon = input("Choose your player's weapon (sword, bow, staff, dagger)")
        spell = input("Choose your player's spell (potion, healing_spell, fire_spell, posion_spell")
        if weapon == "sword" and spell == "potion":
            player = Player(player_name, player_sword, player_potion, filepath)
        elif weapon == "sword" and spell == "healing_spell":
            player = Player(player_name, player_sword, player_healing, filepath)
        elif weapon == "sword" and spell == "fire_spell":
            player = Player(player_name, player_sword, player_fire, filepath)
        elif weapon == "sword" and spell == "posion_spell":
            player = Player(player_name, player_sword, player_poison, filepath)
        if weapon == "bow" and spell == "potion":
            player = Player(player_name, player_bow, player_potion, filepath)
        elif weapon == "bow" and spell == "healing_spell":
            player = Player(player_name, player_bow, player_healing, filepath)
        elif weapon == "bow" and spell == "fire_spell":
            player = Player(player_name, player_bow, player_fire, filepath)
        elif weapon == "bow" and spell == "posion_spell":
            player = Player(player_name, player_bow, player_poison, filepath)
        if weapon == "dagger" and spell == "potion":
            player = Player(player_name, player_dagger, player_potion, filepath)
        elif weapon == "dagger" and spell == "healing_spell":
            player = Player(player_name, player_dagger, player_healing, filepath)
        elif weapon == "dagger" and spell == "fire_spell":
            player = Player(player_name, player_dagger, player_fire, filepath)
        elif weapon == "dagger" and spell == "posion_spell":
            player = Player(player_name, player_dagger, player_poison, filepath)
        if weapon == "staff" and spell == "potion":
            player = Player(player_name, player_staff, player_potion, filepath)
        elif weapon == "staff" and spell == "healing_spell":
            player = Player(player_name, player_staff, player_healing, filepath)
        elif weapon == "staff" and spell == "fire_spell":
            player = Player(player_name, player_staff, player_fire, filepath)
        elif weapon == "staff" and spell == "posion_spell":
            player = Player(player_name, player_staff, player_poison, filepath)
        player_return.append(player)
    return player_return
    
def damage(player_lst, monster):
    """Simulates a fight scene between a player and a monster
    Args:
        player_lst(lst): A list of player objects
        monster(monster_obj): An object which is supposed to represent a fantasy creature that the player
        fights agains
    Side effects:
        Prints out player prompts, asking th player if they would want to attack and with what type of damage
        they would like to attack with. Also prints out which player is attacking."""
    print (f"You have approached this monster, please make a role to see who will attack first")
    damage_dict = dice_roll(player_lst)
    player_count = 0
    count = damage_dict[0]
    while monster.monster_health > 0 and count[0].player_health:
        question=input(f"{count[0].player_name}, would you like to attack? (y/n)")
        if question == "y":
            question2 = input("Would you like to use your weapon or magic?")
            if question2 == "weapon":
                count[0].weapon.item_damage(monster)
            elif question2 == "magic":
                if count[0].spell == "healing_spell":
                    heal_player = input("Which player would you like to heal?")
                    damage_dict[player_count].spell.heal(heal_player)
                else:
                    count[0].spell.spell_damage(monster)
                print (f"Monster health is now {monster.monster_health}")
            print (f"Your turn is now over, it's the {monster.monster_name}'s turn to attack")
            monster.monster_attack(count[0])
        elif question == "n":
            print (f"It's the {monster.monster_name}'s turn to attack")
            monster.monster_attack(count[0])
            player_count += 1
    if monster.monster_health == 0:
        print ("Success! you have killed the monster")
    if count[0].player_health == 0:
        print (f"{count[0].player_health} has died. Rest in peace")
    player_count += 1
class Plot:
    """Keep track of the player’s choice and location of the player on the plot."""
    def choices(filepath):
        """Asks the player with the highest dice roll value which path they want to choose and the actions that result from it according to their location.

        Args:
            filepath (str): path to the text file containing the player attribute values

        Raises:
            ValueError: Invalid input from the user
            
        Side effect:
            print messages based on the player's decision and location.
            
        """
        player_lst = start(filepath)        
        highest_roll = dice_roll(player_lst)
        first_location = None
        top_player = highest_roll[0]
        print(f'{top_player[0].player_name} you rolled the highest, you get to choose the path.')
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
        highest_roll = dice_roll(player_lst)
        top_player = highest_roll[0]
        print(f'{top_player[0].player_name} you rolled the highest, you get to choose the path.')
        second_location = None
        if first_location == 'forest':
            second_decision = input('Would you like to fight or flee the Dragon?')
            if second_decision == 'fight':
                dragon = Dragon()
                damage(player_lst, dragon)
                second_location = 'lost'
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
                print(f'You have received {item}.')
                second_location = 'NPC'
                print('Your next location is a NPC encounter.')
            elif second_decision == 'pass':
                second_location = 'witch'
                print('Your next location is a witch encounter.')
            else:
                raise ValueError('Invalid input')
        highest_roll = dice_roll(player_lst)
        top_player = highest_roll[0]
        print(f'{top_player[0].player_name} you rolled the highest, you get to choose the path.')    
        third_decision = None
        third_location = None
        if second_location == 'NPC':
            third_decision = input('Would you like to ignore or help the NPC?')
            if third_decision == 'help':
                npc_decision = input("Hi, I'm Gunner. Would you like to get a random item or fight the monster?")
                if npc_decision == 'random item':
                    list_of_items = ['sword', 'bow', 'dagger', 'staff']
                    rand_item = random.choice(list_of_items)
                    print(f'You have received {rand_item}.')
                elif npc_decision == 'fight the monster':
                    witch_monster= Witch()
                    damage(player_lst, witch_monster)
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
            third_decision = input('Would you like to run or fight the witch?')
            if third_decision == 'fight':
                witch = Witch()
                damage(player_lst, witch)
                third_location = 'curse'
                print('You will get cursed.')
            elif third_decision == 'run':
                third_location = 'starvation'
                print('Sorry, there is nowhere to go anymore.')
            else:
                raise ValueError('Invalid input')
        elif second_location == 'lost':
            third_location = 'starvation'
            print('Sorry, there is nowhere to go anymore.')
        print('Your party has died of starvation') if third_location == 'starvation' else print('You have been cursed, better luck next time!') if third_location == 'curse' else print('You have obtained magic!')

def end():
    """ outputs the ending player statistics and whether or not they made good 
        decisions throughout the game
    Args:
    player(str): amount of players being chosen/dice roll
    
    Returns:
     the ending player statistics
   """
    player_lst = 'Dungeon Master'
    game = 'Dungeons and Dragons!'
    print(f"Thank you,{player_lst} for playing and exploring {game}")
    
def main(filepath):
    """Open and read the file.
    
    Args:
    filepath(str): path to the text file which includes the player's character of choice.
    
    Side effect:
    Opens and reads the text file """

    Plot.choices(filepath)
    end()
    
def parse_args(arglist):
    """Process command line arguments.
    
    Args:
    arglist(list of str): arguments from the command line
    
    Returns:
    namespace: the parsed arguments, as a namespace."""   
    
    parser = ArgumentParser()
    parser.add_argument('filepath',  help = 'path to player text file')
    return parser.parse_args(arglist)
        
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)