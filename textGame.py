import random


def namepicker():
    i = 0
    while i < 1:
        username = raw_input("Enter name here: ")
        print("")
        print("Is your name " + username + "?")
        usernameconfirmation = raw_input("Type Y or N: ").upper()
        print("")
        if usernameconfirmation in ("Y", "YES"):
            i += 1
            return username
        elif usernameconfirmation in ("N", "NO"):
            print("Lets try that again")
        else:
            print("Please enter Y or N, lets try that again")


def genderpicker():
    i = 0
    while i < 1:
        print ("What is your gender?")
        usergender = raw_input("Type M or F here: ").upper()
        if usergender in ("M", "MALE"):
            usergender = "Male"
            print("You are " + usergender + "\n")
            i += 1
            return usergender
        elif usergender in ("F", "FEMALE"):
            usergender = "Female"
            print("You are " + usergender + "\n")
            i += 1
        else:
            print ("Type M for male and F for female \n")


def racepicker():
    i = 0
    while i < 1:
        print ("what is your race? Pick either Human, Elf, Orc, or Dwarf")
        userrace = raw_input("Type H, E, O, D here:").upper()
        if userrace in ("H", "HUMAN"):
            userrace = "Human"
            print("you are " + userrace + "\n")
            i += 1
            return userrace
        elif userrace in ("E", "ELF"):
            userrace = "Elf"
            print("You are an " + userrace + "\n")
            i += 1
            return userrace
        elif userrace in ("O", "ORC"):
            userrace = "Orc"
            print("You are an " + userrace + "\n")
            i += 1
            return userrace
        elif userrace in ("D", "DWARF"):
            userrace = "Dwarf"
            print ("You are a " + userrace + "\n")
            i += 1
            return userrace
        else:
            print ("Try again, type H for human, E for elf, O for orc, and D for dwarf\n")


def generateroom():
    monsterlist = ["dragon", "Troll", "Ogre", "none"]
    treasurelist = ["chest", "gold", "diamonds", "none"]
    doorslist = ["north", "west", "east"]
    monsterchoice = random.choice(monsterlist)
    treasurechoice = random.choice(treasurelist)
    doorchoice = random.choice(doorslist)
    completeroom = [monsterchoice, treasurechoice, doorchoice]
    return completeroom


nextroom = generateroom()


def enterroom(nextroom):
    roommonster = nextroom[0]
    roomtreasure = nextroom[1]
    roomdoor = nextroom[2]
    print("You have entered a new room\n" 
          "You see a " + roommonster + "\n" +
          "You notice a " + roomtreasure + "\n" +
          "You also see a door to your " + roomdoor + "\n")


def charactercreation():
    username = namepicker()
    usergender = genderpicker()
    userrace = racepicker()
    character = [username, usergender, userrace]
    return character


def startgame():
    print("Start Game Successful - now entering character creation\n")
    character = charactercreation()
    return character


def loadgame():
    print("Load not implimented yet, please select another option\n")


def mainmenuoptions():
    print("Please select: \n 1. New Game \n 2. Load Game \n 3. Quit\n")
    menuchoice = input("Select Choice:")
    #TODO: error handling for non 1-3 inputs
    return menuchoice


def mainmenuaction(menuchoice):
    i = 0
    while i < 1:
        if menuchoice == 1:
            i += 1
            startgame()
        elif menuchoice == 2:
            loadgame() #TODO: Add loading feature
            mainmenuoptions()
        elif menuchoice == 3:
            i += 1
            print("Thank you for playing, now quitting :(")
            quit()
        else:
            print("Not a valid option, please select 1, 2, or 3\n")
            mainmenuoptions()


def whatsnext():
    print("calling next function")


print("welcome to textGame\n")
menuchoice = mainmenuoptions()
mainmenuaction(menuchoice)
    #loadGame
nextroom = generateroom()
enterroom(nextroom)
whatsnext()
#startActualGame
#enterroom(nextroom)