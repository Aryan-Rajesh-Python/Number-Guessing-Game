import random
import pyfiglet
app=pyfiglet.figlet_format("Guessing Game")
print(app)
def guessing_game():
    a=random.randint(1,20)
    c=input("Do you want to play an easy game or do ypu want to play a hard game: ")
    if(c=="easy" or c=="Easy" or c=="EASY"):
        chances=10
    elif(c=="hard" or c=="Hard" or c=="HARD"):
        chances=5
    for i in range(chances):
        b=int(input("Enter a number to guess: "))
        if(a!=b):
            if(a>b):
                chances-=1
                print("Number is too low")
            elif(a<b):
                chances-=1
                print("Number is too high")
        elif(a==b):
            print("You have won the game")
            break
        if(chances==0):
            print("You have lost the game")
            break
guessing_game()
while(True):
    opinion=input("Do you want to continue playing the game: ")
    if(opinion=="yes" or opinion=="Yes" or opinion=="YES"):
        guessing_game()
    elif(opinion=="no" or opinion=="No" or opinion=="NO"):
        print("Thank you for playing our game!")
        break
    
    