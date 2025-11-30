import os
from .Options import Options
from player import Player
class BasicScene:
  def __init__ (self):
    pass
    # pass is used to avoid errors related to having an empty body in function definition.
    # Todo: fill out the BasicScene class if needed.

  def runScene(self, player : Player) -> str:
    # This method should never run. Please make sure to overwrite it.
    print("I'm the BasicScene class!")
    return "game over"
  # This method should clear the players screen of all text
  def clearScreen(self):
    # What this call does is pass a command as a string to the underlying C interperter.
    # Specifically it calls system({string command}) as if a user entered it in the shell.
    # "clear||cls" is saying: run either 'clear' or 'cls' if it exists in the shell.
    # There is still a chance this implementation will fail if 'clear' or 'cls' do not exist.
    os.system("clear||cls")

  # This method should return an integer that is <= optionsTotal but not 0.
  # This method should also handle any improper responses.
  def getUserResponse(self, optionsTotal : int):
    # For dev testing and catching edge cases.
    if optionsTotal <= 0:
      raise ValueError("Options cannot be less than 1.")

    # Repeat endlessly until the user decides to comply!
    while True:
      # Parsing a non-integer input can cause an exception.
      try:
        userInput = input("Please enter your choice: ")
        userChoice = int(userInput)

        # Need to make sure that userChoice is between 1 and optionsTotal
        if userChoice <= optionsTotal and userChoice >= 1:

          return userChoice # Only way to break the loop

        else:
          if optionsTotal == 1:
            print("You only have one choice~" )
          if optionsTotal == 2:
            print("Please choose between options 1 or 2")
          else:
            print(f"Please choose a number between 1 and {optionsTotal}!")

      # This should trigger if the input is "apple" for example.
      except Exception:
        print("Invalid choice, please try again~")

  # Alternate calling if the optionsList and message are already defined.
  def makeNewOptions(self, optionsList : list[str] = [], message : str = ""):
    return Options(optionsList, message)

  # This method should accept an instance of Options class to render text on screen.
  # optionsObj : Options is a type hint for VSCode
  def renderOptions(self, optionsObj : Options):
    print(f"{optionsObj.getMessage()}\n")

    optionList = optionsObj.getAllOptions()
    for i in range(len(optionList)):
      print(f"{i + 1} - {optionList[i]}\n")


  # This method should render a block of text and have a prompt to allow the player time to read
  def renderMessage(self, message : Options | str):
    # This is if an instance of Options is provided.
    if isinstance(message, Options):
      message = message.getMessage()

    print(f"{message}\n")
    input("Press enter to continue...")