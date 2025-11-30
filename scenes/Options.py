class Options:
  _optionsList : list[str] = []
  _message = ""


  def __init__ (self, optionList : list[str] = [], message : str = ""):
    # Check if the argument is a list. Will not check contents.
    self._optionsList = optionList
    self._message = message

# Adds a single option to the internal list. Option string is the contents of the option
# Example: 1. Raise a hand., 2. Yell loudly!, 3. {optionString}
# Will not stringify the optionString.
  def addOption (self, optionString : str):
    self._optionsList.append(optionString)

# Accepts a list and will use that as the options.
  def addOptions (self, optionList : list[str]):
    self._optionsList = optionList

# returns the amount of options in the list
  def getNumberOfOptions (self):
    return len(self._optionsList)

# returns a shallow copy of the options list
  def getAllOptions (self):
    return list(self._optionsList) # Shallow copy of optionsList

# returns an option by 1 index. Will treat all 0 and neg values as 0.
  def getOption(self, oneIndex : int):
    optionIndex = oneIndex - 1

    if optionIndex < 0:
      optionIndex = 0
    return self._optionsList[optionIndex]

# get the message and set the message
  def setMessage(self, message : str):
    self._message = message

  def getMessage(self):
    return self._message