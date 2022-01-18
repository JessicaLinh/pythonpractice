def validateLetter(guess):

    while True:
        if guess.isalpha() == True and len(guess) == 1:
            return guess    
        else: 
            print ("Enter an alphanumeric of 1 character length please. It must be a-z") 
            guess = input("player 2 enter a letter: ")

print ("Welcome to Guess the word game")

word1 = input("Player 1 please enter the secret word: ")
print ("player 2, you must guess the secret word")
print ("the word length is "+str(len(word1)))

endGame = False

while (endGame == False):

    guess = input("player 2 enter a letter: ")
    guess = validateLetter(guess)

    n = word1.count(guess)
    print ("letter "+guess+": count: "+str(n))

    yesNo = input("Do you want to guess the word now?")
    if yesNo == "Y":
        word2 = input("Player 2 please enter the secret word: ")
        if word1 == word2: 
            print ("player 2 wins!!")
        else:
            print ("player 1 wins!!")
        endGame = True

                    

