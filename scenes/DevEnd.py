from .BasicScene import BasicScene

# This class is to test functionality of other scenes. Only use for development.
class DevEnd(BasicScene):
  def __init__ (self):
    super().__init__()
    # This doesen't do anything at the moment. It's just here for completeness.

  # The runScene method should always return a string that will load the next scene
  # Additionally, this method should always be called with the player object in main.py
  def runScene (self, player):
    # Test message
    print("We reached the ending scene meow-ster!")

    # This will end the game.
    return "game over"
