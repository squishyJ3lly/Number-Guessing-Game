from random import randint, choice
from sys import exit

winningCompliments = [
    "You are great at this!",
    "Amazing!",
    "You can do really this!"
]

gameModes = {
    "easy": {
        "name": "Easy",
        "max": 20,
        "shortcut": "ea"
    },
    "medium": {
        "name": "Medium",
        "max": 100,
        "shortcut": "m"
    },
    "hard": {
        "name": "Hard",
        "max": 500,
        "shortcut": "h"
    },
    "extreme": {
        "name": "Extreme",
        "max": 2000,
        "shortcut": "ex"
    }
}

defaultDifficulty = gameModes["medium"] # The medium difficulty
currentGameMode = defaultDifficulty

def checkIfCorrect(guessedNumber, correctNumber):
    match True:
        case _ if guessedNumber == correctNumber:
            print(f"Correct!! {choice(winningCompliments)}")
            return True
        case _ if guessedNumber > correctNumber:
            print("Too high!")
            return False
        case _ if guessedNumber < correctNumber:
            print("Too low!")
            return False
    print("[Warning] Unknown if-statement error has occurred.")
    return False

def pickGameMode():
    print("Please type in the game mode here the gamemodes are shown below ↓")
    for gameMode in gameModes.values():
        print(f"    {gameMode['name']} (numbers 1-{gameMode['max']}) you can type in '{gameMode['shortcut']}' for short")
    gameModeInput = input("Type the gamemode here: ")
    for mode in gameModes.values():
        if gameModeInput == mode["shortcut"]:
            return mode
    if gameModeInput.lower() == "d" or gameModeInput.lower() == "default":
        return defaultDifficulty
    while gameModeInput == "" or not gameModeInput.lower() in gameModes:
        print("No input detected or invalid game mode. Please retype your game mode.")
        gameModeInput = input("Type the game mode here: ")
    return gameModes[gameModeInput]

def startGame(gameMode):
    if not gameMode["name"].lower() in gameModes:
        print("Game mode input is an invalid input/game mode.")
        quitGame(1)
    guesses = 0
    correct = randint(1, gameMode["max"]) # gameMode["max"] is the maxNumber
    print(f"Generated a number 1-{gameMode['max']}. Do your best to guess it!")
    while True:
        guess = input("Your guess: ")
        if guess == "":
            print("No input detected or invalid game mode. Please retype your guess.")
            continue
        guess = int(float(guess)) # just in case the user trys to put in a float as input
        if checkIfCorrect(guess, correct):
            guesses += 1
            print(f"Took {guesses} guesses.")
            quitGame(0)
        guesses += 1

def quitGame(exitCode):
    print("Quitting Game.")
    exit(exitCode)

def main():
    print("Welcome to the number guessing game!")
    print("Type 's' and enter to start. Type 'q' to quit")
    start_input = input(">> ")
    while start_input == "":
        print("No input recieved. Please retype and try again.")
        start_input = input(">> ")
    if start_input.lower() == "s" or start_input.lower() == "start":
        currentGameMode = pickGameMode()
        startGame(currentGameMode)
    elif start_input.lower() == "q" or start_input.lower() == "quit":
        quitGame(0)
    else:
        print("Unknown error has occurred, quitting game.")
        quitGame(1)

if __name__ == "__main__":
    main()