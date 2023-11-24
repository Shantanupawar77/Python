import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

print("Comp Turn :Snake(s) Water(w) Gun(g) ?")
randno=random.randint(1,3)

if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'

you=input("Your turn :Snake(s) Water(w) Gun(g):\n")
a=gamewin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a==None:
    print("The game is draw!")
elif a:
    print("YOU win")
else:
    print("YOU lose")