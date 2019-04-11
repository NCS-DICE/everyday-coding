from player import Player 
from tictactoe import TicTacToe

print("Welcome to Tic Tac Toe!")
play = input("Would you like to play? (Y/n)")
if play.lower() == "n":
   exit()
players = list()
tokens = list()

print("Starting your session! I just need a little info first.")

for i in range(1, 3):
   name = input("Player {}, please give me your name.".format(i))
   age = int(input("Okay! Thanks! How old are you? "))
   token = input("Please enter your game token or none for default. ")
   if token == "":
      tokens.append(None)
   else:
      while token in tokens:
         print("I'm sorry, that's the same as Player One.")
         token = input("Please enter a different character: ")
      tokens.append(token)
   
   player = Player(name, age)
   players.append(player)

game = TicTacToe(players, tokens[0], tokens[1])

play_again = True
while play_again:
   game.reset_game()
   turn = 1
   while not game.game_over:
      game.display_board()
      bad_guess = True
      while bad_guess:
         id = 0
         if turn % 2 == 0:
            id = 1
         print("{}'s Turn!".format(players[id].name))
         c = input("Please enter a space you'd like to place your token. ")
         if game.play_turn(int(c), players[id].name):
            print("Good Play! ")
            bad_guess = False 
            turn += 1
   game.display_board()
   game.display_stats()
   a = input("Would you like to play again? (Y/n) ")
   
   if a.lower() == "n":
      play_again = False 

print("Thanks for playing!")

   

