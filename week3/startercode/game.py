from typing import Dict, List 
from player import Player
class Game:
   """
   A class for our Game object. This will be inherited from. 
   """
   game_count: int
   scores: Dict[str, int]
   game_over: bool

   def __init__(self, players: List[Player]) -> None:
      """
      The Constructor for the Game class. Initializes values and 
      the players list.
      """
      self.scores = dict()
      self.game_count = 0
      self.game_over = False
      for p in players:
         self.scores[p.name] = 0 # Initialize scoreboard to zero
   
   def show_scores(self) -> None:
      """
      Prints the scores of the game to the screen.
      """
      print("SCOREBOARD:")
      print("Games Played: {}".format(self.game_count))
      print("\nPlayer\tWins")
      for key,val in self.scores.items():
         print("{}:\t{}".format(key, val))