from game import Game
from player import Player
from typing import List, Dict 

class TicTacToe(Game):
   """ 
   Extends Game class to create TicTacToe game.
   """
   game_board = list() # intentionally using flexible typing
   player_token: Dict[str, str]

   def __init__(self, players: List[Player], token_one = "X", token_two = "O"): # Needs to setup the game


   def display_board(self): # Needs to display the board to look a little like a tictactoe board


   def play_turn(self, space: int, player: str): # This is the main method to play a turn.
      
      
   def reset_game(self): # This is called when the game is over and the players want to play again.
      
