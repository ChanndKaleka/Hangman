
from dataclasses import replace
from random import choice
from hangmanArt import stages
from hangmanWords import word_list

randomWord=choice(word_list).upper()

lengthWord=len(randomWord)
display=list()

for x in range(lengthWord):
    display.append("_")

print(f"The length of the word is {lengthWord}")
endOfGame=False
lives =6
while endOfGame != True:
    
    userGuess=input("Guess a letter: ").upper()

    for x in range(lengthWord):
        if(userGuess==randomWord[x]):
            display[x]=userGuess
    if userGuess not in randomWord:
        lives-= 1
        if(lives==0):
            endOfGame=True
            print("You lost")
            print(randomWord)
    print(display)
    
    if("_" not in display):
        print("You Win")
        endOfGame=True
    print(stages[lives])