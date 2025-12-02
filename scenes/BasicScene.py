import os
from .Options import Options
from player import Player
import time
class BasicScene:
  _defaultTimeDelay = 0.05

  def __init__ (self, defaultTimeDelay : float = 0.05):
    self._defaultTimeDelay = defaultTimeDelay

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

    # Build a message string to pass onto the renderMessage method after formatting.
    messageString = f"{optionsObj.getMessage()}\n\n"
    self.renderMessage(messageString, False)

  # This part is responsible for rendering the options including the time delay.
    optionList = optionsObj.getAllOptions()
    for i in range(len(optionList)):
      optionString = f"{i + 1} - {optionList[i]}\n\n"
      self.renderMessage(optionString, False)
      time.sleep(optionsObj.getTimeDelay())


  # This method should render a block of text and have a prompt to allow the player time to read
  # By default the time delay is 0.05 seconds. The Options class is also default 0.05 seconds.
  # To override the default, provide the time delay in the Options instance.
  # Also we can initiate the Scene with a new default using super().__init__(time) in the child class.
  def renderMessage(self, message : Options | str, isSingleMessage : bool = True):
    timeDelay = self._defaultTimeDelay
    # This is if an instance of Options is provided.
    if isinstance(message, Options):
      timeDelay = message.getTimeDelay()
      isSingleMessage = message.getIsSingleMessage()
      message = message.getMessage()

    # Warning: At this point of the exectution, message should be type string!

    # This allows the characters to print as if typed.
    for character in message:
      # sep and end are explicitly set to empty strings to allow single consecutive char printing
      # flush forces the output to render. This prevents the chars from being delayed in the buffer.
      print(character, sep='', end='', flush=True)
      time.sleep(timeDelay)

    # Added for messages that do not need the prompt.
    if isSingleMessage:
      input("\nPress enter to continue...")