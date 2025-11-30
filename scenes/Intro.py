from .BasicScene import BasicScene
from player import Player
# importing the BasicScene class to extend Intro.

# This class should introduce the player to the game and get the player's character name.
class Intro (BasicScene):
  def __init__ (self):
    super().__init__()
    # The above is to call the __init__ constructor from the parent BasicScene class.

  # This is a method specific to the Intro scene.
  def getUserName(self):
    isNameChosen = False
    name = ""

    # Get the user's name
    while not isNameChosen:
      self.clearScreen()
      name = input("Please choose your name. First name only please: ")
      print(f"\nYou have chosen: {name}!")

      option = self.makeNewOptions(["yes", "no"], "Do you like your name?")
      self.renderOptions(option)
      chosenOption = self.getUserResponse(2)

      if chosenOption == 1:
        isNameChosen = True

    return name


# This is where the game logic will take place.
# Note: this overrides the implementation in the BasicScene parent class
  def runScene (self, player : Player):
    self.clearScreen()
    # Sample code. This is subject to change.

    # This code will prompt user to input a desired name and set it into Player object
    playerName = self.getUserName()

    player.setName(playerName)

    self.clearScreen()
    storyText = f"Beep!\n\nA persistent alarm shatters the silence. A tiny hand clumsily swats at a magical alarm spell.\n\nWake up {player.getName()}! Queen Oona is going to get mad again!\n\nYou shoot out of bed, tiny wings fluttering magically levitating an equally small person. In your haste, you bonk your head against the heartwood cieling of your tree house. The sudden pain dispersed the remaining sleep from your mind.\n\n\"Ugh, what time is it?\"\n\nYou rub your noggin when the floating spell matrix caught your eye. A single line flashed like an angry bruise: {player.getName()} don't forget to wake Godzilla to fight off...\n\nYour mind failed to register the suspiciously damaged text before it latched on to the single obvious fact: Godzilla was still asleep and you were in big trouble if Fairy Queen Oona were to find out!"

    self.renderMessage(storyText)

    self.clearScreen()
    storyText = "You quickly get dressed before making for the exit. A bag of magical coins glint in the morning sun just as you are about to bolt out the balcony. \n\n'Maybe I should stop at gramp's shop.' You think to yourself.\n\nWhat will you do?"

    option = self.makeNewOptions(["Go to gramp's mystical shop of trinkets.", "Onward towards duty and danger!"], storyText)

    self.renderOptions(option)
    userChoice = self.getUserResponse(2)

    if userChoice == 1:
      return "dev end" # possible shop
    if userChoice == 2:
      return "dev end" # Scene 1

    return "game over" # This should never run.
