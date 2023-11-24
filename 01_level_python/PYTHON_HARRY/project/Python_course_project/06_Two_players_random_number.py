import random
print("Please enter the range:\n")
n1=int(input("Enter the lower bound:\n "))
n2=int(input("Enter the upper bound:\n "))
cguess1=random.randint(n1,n2)
cguess2=random.randint(n1,n2)
play_1_tri=0
play_2_tri=0

while True:
    while True:
        print("Player1:")
        pl_g_1=int(input(f"Guess the number between {n1} and {n2}:\n"))
        if(cguess1<pl_g_1):
            print("Lesser number please\n")
            play_1_tri+=1
        elif(cguess1>pl_g_1):
            print("Higher number please\n")
            play_1_tri+=1
        elif(cguess1==pl_g_1):
            print("You have enterred correct number!\n")
            play_1_tri+=1
            break
    while True:
        print("Player2:")
        pl_g_2=int(input(f"Guess the number between {n1} and {n2}:\n"))
        if(cguess2<pl_g_2):
            print("Lesser number please\n")
            play_2_tri+=1
        elif(cguess2>pl_g_2):
            print("Higher number please\n")
            play_2_tri+=1
        elif(cguess2==pl_g_2):
            print("You have enterred correct number!\n")
            play_2_tri+=1
            break
    break
if(play_1_tri>play_2_tri):
    print(f"Player 2 Win ! and you took {play_2_tri} trials\n")
elif(play_1_tri<play_2_tri):
    print(f"Player 1 Win !and you took {play_1_tri} trials\n")
else:
    print("Its a Tie\n")
print(f"Number for player1 was {cguess1} and ")
print(f"Number for player2 was {cguess2}")
