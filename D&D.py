from argparse import ArgumentParser
import sys
import re
import random
import time
class Player():
    def __init__(self, player_name, weapon, spell, filepath):
        self.player_name = player_name
        self.player_health = 150
        expr = r'''\d+'''
        with open(filepath, 'r', encoding="utf-8") as f:
            line = f.readlines()
            self.player_strength = re.search(line[0], expr)
            self.player_dexterity = re.search(line[1], expr)
            self.player_intelligence = re.search(line[2], expr)
            self.player_wisdom = re.search(line[3], expr)
            self.player_charisma = re.search(line[4], expr)
            self.player_constitution = re.search(line[5], expr)
        self.weapon= weapon
        self.spell= spell
        

class Monster:
    def __init__(self,monster_health = 150, monster_att_damage = 15):
        self.monster_health = monster_health
        self.monster_att_damage = monster_att_damage
    def monster_attack(self, player):
        player.player_health -= self.monster_att_damage
        print(f"{player.player_health}")
        if player.player_health <= 0:
            print(f"{player} died.")  
class Witch(Monster):
    def __init__(self, monster_health = 130, monster_att_damage = 17):
        self.monster_name = "Witch"
        self.monster_health = monster_health
        self.monster_att_damage = monster_att_damage
    def monster_attack(self, player):
        player.player_health -= self.monster_att_damage
        print(f"Player health is now {player.player_health}.")
        if player.player_health <= 0:
            print(f"{player} died.")  
class Dragon(Monster):
    def __init__(self, monster_health = 140, monster_att_damage = 20):
        self.monster_name = "Dragon"
        self.monster_health = monster_health
        self.monster_att_damage = monster_att_damage
    def monster_attack(self, player):
        player.player_health -= self.monster_att_damage
        print(f"Player health is now {player.player_health}.")
        if player.player_health <= 0:
            print(f"{player} died.")  
def dice_roll(player_lst):
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
    def __init__(self, name = None, base_damage = 25, range = 10):
        self.base_damage = base_damage
        self.range = range
        self.name = name
    def equip(self):
        print (f"{self.player} has recieved a {self.name}")
    def ability(self):
        print(f"This {self.name} is able to do {self.base_damage}. It has a range of {range}")
    def item_damage(self, monster):
        monster.monster_health = monster.monster_health - self.base_damage
        return monster.monster_health
    def __str__(self):
        print (f"{self.name}: damage{self.base_damage} range:{self.range}")
class sword(items_or_weapons):
    def __init__(self):    
        super().__init__()
        self.name = "sword"
class bow(items_or_weapons):
    def __init__(self):    
        super().__init__()
        self.name = "bow"
class dagger(items_or_weapons):
    def __init__(self):
        super().__init__()
        self.name = "dagger"
class staff(items_or_weapons):
    def __init__(self):
        super().__init__()
        self.name = "staff"
class spells_and_curses:
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
        monster.monster_health = monster.monster_health - self.spell_stats
        return monster.monster_health
class potion(spells_and_curses):
    def __init__(self):
        super().__init__()
        self.name = "potion"
class healing_spell(spells_and_curses):
    def __init__(self):
        super().__init__(self)  
        self.name = "Healing spell"
    def heal(self, player):
        player.health = self.spell_stats + player.health
        return player.health
class poison_spell(spells_and_curses):
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
    def __init__(self):
        super().__init__()
        self.name = "fire spell"
def start(filepath):
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
    def choices(filepath):
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
                third_location = 'get magic'
                print('Your final action will be getting a reward.')
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
    filepath(file): filepath to the text file which includes the player's character of choice.
    
    Side effect:
    reads the text file """

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