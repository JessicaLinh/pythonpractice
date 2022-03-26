def validateWord(word):

    while True:
        if word.isalpha() and len(word) > 5 and len(word) < 12:
            return word 
        else:
            print("Sil vous plait enter a word between 6-12 letters, merci.")
            word = input("secret word: ")

def validateLetter(guess, guessedLetters):
   
    print ("guessed letters is "+guessedLetters)

    while True:
        if guess.isalpha() == True and len(guess) == 1 and guess not in guessedLetters:
            return guess    
        else: 
            print ("Enter an alphanumeric of 1 character length please. It must be a-z") 
            print ("Also ensure you have not entered a letter you've guessed before!!!")
            guess = input("player 2 enter a letter: ")

 #####################################################################           

guessedLetters = ""

print ("Welcome to Guess the word game")

word1 = input("Player 1 please enter the secret word: ")
word1 = validateWord(word1)
print ("player 2, you must guess the secret word")
print ("the word length is "+str(len(word1)))

endGame = False

while (endGame == False):

    guess = input("player 2 enter a letter: ")   
    guess = validateLetter(guess, guessedLetters)
    guessedLetters += guess     

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

print (guessedLetters)
                    

