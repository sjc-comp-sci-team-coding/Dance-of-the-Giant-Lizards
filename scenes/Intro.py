from .BasicScene import BasicScene
# importing the BasicScene class to extend Intro.

# This class should introduce the player to the game and get the player's character name.
class Intro (BasicScene):
  def __init__ (self):
    super().__init__()
    # The above is to call the __init__ constructor from the parent BasicScene class.

# This is where the game logic will take place.
# Note: this overrides the implementation in the BasicScene parent class
  def runScene (self, player):

    # Sample code.
    # This code will prompt user to input a desired name and set it into Player object
    playerName = input("Please input your name: ") # should return a string
    player.setName(playerName)

    # This is to demonstrate that the player's name has been set.
    print(player.getName() + " has joined the game!")

    return "dev end" # Next scene to be called.