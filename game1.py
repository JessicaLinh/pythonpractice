print ("Welcome to Guess the word game")

word1 = input("Player 1 please enter the secret word: ")
print ("player 2, you must guess the secret word")
print ("the word length is "+str(len(word1)))

for i in range(3):

    guess = input("player 2 enter a letter: ")
    print ("letter "+guess+": count: "+str(word1.count(guess)))


word2 = input("Player 2 please enter the secret word: ")
if word1 == word2: 
    print ("player 2 wins!!")
else:
    print ("player 1 wins!!")

