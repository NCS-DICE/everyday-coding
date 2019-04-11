from typing import Dict, List 
class Game:
   """
   A class for our Game object. This will be inherited from. 
   """
   game_count: int
   players: Dict[str, int]
   game_over: bool

   def __init__(self, players: List[Player]) -> None:
      """
      The Constructor for the Game class. Initializes values and 
      the players list.
      """
      self.game_count = 0
      self.game_over = False
      for p in players:
         self.players[p.name] = 0 # Initialize scoreboard to zero
   
   def show_scores(self) -> None:
      """
      Prints the scores of the game to the screen.
      """
      print("SCOREBOARD:")
      print("\nPlayer\tWins")
      for key,val in self.players.items():
         print("{}:\t{}".format(key, val))