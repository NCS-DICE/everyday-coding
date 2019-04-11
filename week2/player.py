class Player:
   """
   This is a class to manage player data for our game app.
   
   Attributes:
   name (str): the player's name.
   age (int): the player's age.
   wins (int): number of wins the player has.
   favorite_games (Set[str]): A set of the player's favorite games.
   """
   name
   age
   wins
   favorite_games


   def __init__(self, name, age):
      """
      The constructor for Player Class. Initializes properties.

      Parameters:
      name (str): the value to assign to player's name.
      age (str): the value to assign to the player's age.
      """
      self.name = name
      self.age = age
      self.wins = 0
   

   def add_favorite_game(self, game):
      """
      Adds a value from the favorite games set.
      
      Parameters:
      game (str): The name of the game to add
      
      Returns:
      bool: True if game was added. False if not.
      """
      if game in self.favorite_games:
         return False 
      
      self.favorite_games.append(game)
      
      return True


   def rem_favorite_game(self, game):
      """
      Removes a value from the favorite games set.
      
      Parameters:
      game (str): The name of the game to remove
      
      Returns:
      bool: True if game was removed. False if not.
      """
      if game in self.favorite_games:
         self.favorite_games.remove(game)
         return True
      
      return False 



   
   