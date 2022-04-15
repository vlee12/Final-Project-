" just trying to see if this works lol"
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