from game import Game
from player import Player
from typing import List, Dict 

class TicTacToe(Game):
   """ 
   Extends Game class to create TicTacToe game.
   """
   game_board = list() # intentionally using flexible typing
   player_token: Dict[str, str]


   def __init__(self, players: List[Player], token_one = "X", token_two = "O"):
      super().__init__(players)
      self.player_token = dict()
      self.game_board = [None, None, None, None, None, None, None, None, None]
      self.player_token[players[0].name] = token_one
      if token_two == token_one:
         if token_one == "O":
            token_two == "X"
         else:
            token_two == "O"
      self.player_token[players[1].name] = token_two


   def display_board(self):

      print("_____________")      
      
      for i in range(len(self.game_board)):
         if i == 3 or i == 6:
            print("| \n")
         if self.game_board[i] == None:
            print("| {} ".format(i + 1), end='')
         else:
            print("| {} ".format(self.game_board[i]), end='')

      print("|\n_____________")      
  

   def play_turn(self, space: int, player: str):
      if self.game_board[space - 1] != None:
         return False
      token = self.player_token[player]
      self.game_board[space - 1] = token

      if space in [1, 2, 3] : 
         self.game_over = all([i == token for i in self.game_board[:3]])         
      elif space in [4, 5, 6]:
         self.game_over = all([i == token for i in self.game_board[3:7]])
      else:
         self.game_over = all([i == token for i in self.game_board[7:]])
         
      
      if space in [1, 4, 7]:
         self.game_over = all([i == token for i in self.game_board[::3]])
      elif space in [2, 5, 8]:
         self.game_over = all([i == token for i in self.game_board[1::3]])
      else:
         self.game_over = all([i == token for i in self.game_board[2::3]])
      
      if space in [1, 5, 9]:
         self.game_over = all([i == token for i in self.game_board[::4]])
      if space in [3, 5, 7]:
         self.game_over = all([i == token for i in self.game_board[2:-1:2]])

      if not None in self.game_board:
         self.game_over = True
      if self.game_over:
         self.game_count += 1

      return True
      
   
   def reset_game(self):
      self.game_board = [None for i in range(len(self.game_board))]

      self.game_over = False
