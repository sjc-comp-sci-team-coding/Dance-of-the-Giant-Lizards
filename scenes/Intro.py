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
    storyText = f"Beep!\n\nA persistent alarm shatters the silence. A tiny hand clumsily swats at a magical alarm spell.\n\nWake up {player.getName()}! Queen Oona is going to get mad again!\n\nYou shoot out of bed, tiny wings fluttering magically levitating an equally small person. In your haste, you bonk your head against the heartwood ceiling of your tree house. The sudden pain dispersed the remaining sleep from your mind.\n\n\"Ugh, what time is it?\"\n\nYou rub your noggin when the floating spell matrix caught your eye. A single line flashed like an angry bruise: {player.getName()} don't forget to wake Godzilla to fight off...\n\nYour mind failed to register the suspiciously damaged text before it latched on to the single obvious fact: Godzilla was still asleep and you were in big trouble if Fairy Queen Oona were to find out!"

    self.renderMessage(storyText)

    self.clearScreen()
    storyText = "You quickly get dressed before making for the exit. A bag of magical coins glint in the morning sun just as you are about to bolt out the balcony. \n\n'Maybe I should stop at gramp's shop.' You think to yourself.\n\nWhat will you do?"

    option = self.makeNewOptions(["Go to gramp's mystical shop of trinkets.", "Onward towards duty and danger!"], storyText)

    self.renderOptions(option)
    userChoice = self.getUserResponse(2)

    if userChoice == 1:
        choiceOne = "You realize that you couldn't face Godzilla with nothing on your person. In tough situation's like these, gramp's always knows what to do." # unfinished shop scene

        self.renderMessage(choiceOne)

        self.clearScreen()

        choiceOne = ("\"Oh ho ho, finally came to visit good ol' gramps? Didn't know all it took was a monster threat to get more customers.\""
                     "\n\nthe familiar voice you hadn't heard in a while echoed through the crowded room of trinkets. It wasn't until you walked past the "
                     "\npile of old books stacked upon each other that you finally saw him, gramp's the shopkeeper."
                     "\n\n \"Good to see you again kid, what can I get'cha? Hmm? You don't have any coins yet!? Then why'd you come here!? hah I guess you "
                     "\nknew I couldn't let ya leave empty handed. Here, have 10 coins, now go buy something and make sure you have coins next time or else "
                     "\nyou ain't getting nothing hahaha!\"")
            #add 10 coins to player's wallet
            #output shop menu

        self.renderMessage(choiceOne)

        self.clearScreen()

        choiceOne = ("\"Come again soon!\" you hear before exiting the shop. Ok, no more distractions... Onwards to defeating Godzilla once and for all!"
                     "\n\nThough as you finally arrived, something strange began to happen...")

        self.renderMessage(choiceOne)

        self.clearScreen()

    if userChoice == 2:
        choiceTwo = (f"No! You mustn't get distracted {player.getName()}! You have to go on now before the Queen finds out, or worse, Godzilla wakes up!"
                     f"\n\nyou head into the cave Godzilla was last reported to be seen in. After confirming that the giant lizard seemed to be asleep "
                     f"\nstill, you let out a sigh of relief."
                     f"\nHowever... That feeling would not last forever...")  # possible shop

        self.renderMessage(choiceTwo)

        self.clearScreen() # Scene 1

    storyText = (f"It started as a rumble. Even as you were flying in the air, you felt as if you were shaking."
                 f"\nWas it an earthquake? A tsunami? It was hard to tell since you were inside the cave but you saw it was enough to make the ever sleeping monster awaken.")

    self.renderMessage(storyText)

    self.clearScreen()

    storyText = (f"Suddenly, you hear a vicious roar. The noise was so loud you had to cover your pointed ears."
                 f"But as you were momentarily weakened by the sound, a huge rock flew past you. Luckily it missed you then "
                 f"see Godzilla throwing and kicking around more of the rocks as he stomped his way out of the cave."
                 f"\n\nQuick! You have to think fast!")


    option = self.makeNewOptions(["Fly in front of Godzilla and try to reason with him.",
                                  "Follow Him and see where he goes",
                                  "Fall back and try to make a plan"],
                                 storyText)

    self.renderOptions(option)
    userChoice = self.getUserResponse(3)

    if userChoice == 1:
        choiceOne = ("No! You can't let him leave now! You quickly flew over to the entrance of the cave and spread your arms out as if physically trying to stop him."
                     "\n\nSurprisingly you see him stop momentarily. An audible sigh escaped your lips but just as you opened your mouth to speak"
                     "\n\nWHAM! \n\nYou were smacked and flew across the cave, landing on the wall and leaving a fairy dent on it."
                     "\nYour body slides down and you fell to the floor... \n\n\"Ugh...\"")

        self.renderMessage(choiceOne)

        self.clearScreen()

        choiceOne = (
            f"It can't end like this. . . "
            f"\n\nNo... It won't. . . "
            f"\n\n{player.getName()}. . . \n\nWake up.")

        self.renderMessage(choiceOne)

        self.clearScreen()

        #return to the first scene

    if userChoice == 2:
        choiceTwo = (
            f"You can't act rash, but you can't let him get away either."
            f"\n\nYou decide to follow Godzilla and observe his actions. Maybe... He's not so bad?"
            f"\n\nWrong... He was immediately tearing down the place. You hear the screams of frightened citizens, scrambling around to either escape or find safety."
            f"\n\nYou observe Godzilla's movements and soon you get an idea.")
        #might change or add more to later, just did this on a whim
        self.renderMessage(choiceTwo)

        self.clearScreen()

    if userChoice == 3:
        choiceThree = (
            f"You exit the cave and fly the opposite direction as Godzilla. Being near him while he was active and dangerous was not a good idea..."
            f"\n\nOn the way back to the forest, you stumble upon something shiny. You found 10 coins!!"    #add 10 coins
            f"\n\n But your luck ended there... Once you stood back up, Queen Oona was flying in front of you looking at you sternly"
            f"\n\n\"I thought I told you to defeat Godzilla once he woke up, why are you turning back now?\""
            f"\n\n\"Hah... No matter, it seems you are under prepared... Still, I cannot allow that monster to run around and terrorize the entire island... Go on now,"
            f"\n go find Godzilla and distract him to buy time for us. You will soon receive help and I am certain that you'll figure things out from there.\""
            f"\n\nBefore you could respond, Queen Oona disappeared in a second, leaving behind sparkling glitter from where she once was. you sigh and turn away, realizing "
            f"\nthat you had to face the giant lizard sooner rather than later. \n\nYou return to where Godzilla was.")
        #this is a long chunk of text... feel free to split it up if need be
        self.renderMessage(choiceThree)

        self.clearScreen()

        storyText = f"To be continued..."

        self.renderMessage(storyText)

        self.clearScreen()

    return "game over" # This should never run.
