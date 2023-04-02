import random
from playsound import playsound

def game(you,comp):
    if(you==comp):
        return 0
    elif(you=='s'):
        if(comp=='w'):
            return 1
        else:
            return -1
    elif(you=='w'):
        if(comp=='g'):
            return 1
        else:
            return -1
    elif(you=='g'):
        if(comp=='s'):
            return 1
        else:
            return -1

restart =1
score=0
while(restart==1):
    comp=random.randint(1,3)
    if(comp==1):
        comp='s'
    elif(comp==2):
        comp='w'
    elif(comp==3):
        comp='g'

    while(True):
        you = input("Entre 'S' for Snake, 'W' for Water and 'G' for Gun\n")
        you= you.lower()

        if(you == 's' or you == 'w' or you == 'g'):
            break
        else:
            print("Invalid Input\n")
            playsound('C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\game\\Sound.mp3')
    
    result=game(you,comp)

    print("Computer :",comp)
    print("You :",you)

    if(result==1):
        print("Congratulations! You won the game")
        score=score+1
    elif(result==0):
        print("Draw")
    elif(result==-1):
        print("You lost The game")
        score=score-1
    
    print("SCORE :",score)

    while(True):
        restart=input("Entre 1 for restart and 0 to end the game : ")
        if(restart=='0' or restart=='1'):
            break
        else:
            print("Invalid input")
            playsound('C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\game\\Sound.mp3')
    
    restart=int(restart)