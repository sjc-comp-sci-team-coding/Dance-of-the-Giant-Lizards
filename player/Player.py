class Player:
  _name = ""

  def __init__(self):
    # Todo: define constructor
    pass

# Sets the player's name. Called by Intro scene
  def setName(self, playerName : str):
    self._name = playerName

# Used to retrieve player's name.
  def getName(self):
    return self._name