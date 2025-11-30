from scenes import *
from player import Player

# The "*" will import all public classes and variables from the scenes directory (aka folder).

# This class will create a dictionary for all scenes and return the final dict object
def makeTableOfScenes () -> dict[str, BasicScene]:
  # Explicitly calling the dictionary class. Could use {} literal instead.
  tableOfScenes : dict[str, BasicScene] = dict()

  # Below are the scenes to be loaded into the dictionary
  # Every key is assigned an instance of a scene class.
  tableOfScenes["intro"] = Intro()
  tableOfScenes["dev end"] = DevEnd()

  return tableOfScenes

# Adding a function to call the Player class in case we need to set specific attributes.
def makePlayerObject ():
  newPlayerObject = Player()
  return newPlayerObject

# These variables should not be modified.
scenes = makeTableOfScenes()
player = makePlayerObject()

# These variables should be re-assigned as needed
currentScene = scenes["intro"] # Load first scene of the game

# This is an infinite loop. Should break loop when the "game over" string is given
while True:
  # Top of the loop will execute the currently loaded Scene.

  # nextScene is a string that represents the next scene.
  nextScene = currentScene.runScene(player) # runScene should return a string

  # At some point We need to provide the "game over" to exit the loop
  if nextScene == "game over":
    break

  # Load next scene using nextScene string
  currentScene = scenes[nextScene]

# end of loop
print("See you next time!")