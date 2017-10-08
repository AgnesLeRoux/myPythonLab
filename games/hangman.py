import random

words = ["dog", "cat", "toto"]
wordToGuess = random.choice(words)# words[random.randint(0, len(words)-1)]
nbMissing = len(wordToGuess)
length = len(wordToGuess)
nbWrong = 0
nbWrongMax = 5
wrongLetters = set()
guessedLetters = [False for _ in range(length)]

def drawHangman(nbWrong):
    print("nbWrong "+ str(nbWrong))
    if nbWrong== 0:
        print(" # ")
    elif nbWrong == 1:
        print(" # ")
        print(" O ")
    elif nbWrong == 2:
        print(" # ")
        print(" O ")
        print(" | ")
    elif nbWrong == 3:
        print(" # ")
        print(" O ")
        print(" |\\")
    elif nbWrong==4:
        print(" # ")
        print(" O ")
        print("/|\\")
    elif nbWrong==5:
        print(" # ")
        print(" O ")
        print("/|\\")
        print("/  ")
    elif nbWrong==6:
        print(" # ")
        print(" O ")
        print("/|\\")
        print("/ \\")
    return None

def writeWord(guessedLetters, wordToGuess):
    toPrint=""
    for i in range(0, length): 
        if guessedLetters[i]:
            toPrint += wordToGuess[i]+" "
        else:
            toPrint += "- "
    print(toPrint)
    return None
    
def updateNbMissing(nbMissing,  guess):
    for i in range(0, length):
            if guess == wordToGuess[i]:
                nbMissing -=1
    return nbMissing  
    
def updateGuessedLetters(guess, guessedLetters):
    for i in range(0, length):
        if guess == wordToGuess[i]:
            guessedLetters[i] = True
    return None

def updateWrongLetters(guess, wrongLetters):
    wrongLetters.add(guess)
    return None

def playGame(nbWrong, nbMissing):
    while nbMissing >0 and nbWrong <= nbWrongMax:
        drawHangman(nbWrong)
        print("Wrong letters: "+str(wrongLetters))
        writeWord(guessedLetters, wordToGuess)
        guess = input("Your letter: ").lower()
        if guess not in wordToGuess and len(guess)==1:
            nbWrong +=1
            updateWrongLetters(guess, wrongLetters)
        else:
            nbMissing = updateNbMissing(nbMissing,  guess)
            updateGuessedLetters(guess, guessedLetters)
    if nbMissing==0:
        print("You win!! The word is "+wordToGuess)
    else:
        print("You lose! The word was "+wordToGuess)
        drawHangman(nbWrong)
        
playGame(nbWrong, nbMissing)
