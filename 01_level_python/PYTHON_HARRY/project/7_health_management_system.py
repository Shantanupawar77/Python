
""" Client names Harry, Rohan, Hammad 
    make 2 file for each user first for food and second for Workout 
    Total 6 files 
     """


def getdate():
    import datetime
    return datetime.datetime.now()

def log():
    print("Which client do you wan't to log -")
    print("1. Harry")
    print("2. Rohan")
    print("3. Hammad")
    print("Enter= ", end="")
    client_number = int(input())

    if client_number == 1:
        print("What you wan't to log to Harry -")
        print("1. Food")
        print("2. Workout")
        print("Which= ", end="")
        log_number = int(input())
        if log_number == 1:
            print("Log food name = ", end="")
            with open("Harry-food.txt", "a") as harry_file:
                harry_file.write('['+str(getdate())+']' + " " + input() + "\n")
        elif log_number == 2:
            print("Log workout name = ", end="")
            with open("Harry-workout.txt", "a") as harry_file:
                harry_file.write('['+str(getdate())+']' + " " + input() + "\n")

    elif client_number == 2:
        print("What you wan't to log to Rohan -")
        print("1. Food")
        print("2. Workout")
        print("Which= ", end="")
        log_number = int(input())
        if log_number == 1:
            print("Log food name = ", end="")
            with open("Rohan-food.txt", "a") as Rohan_file:
                Rohan_file.write('['+str(getdate())+']' + " " + input() + "\n")
        elif log_number == 2:
            print("Log workout name = ", end="")
            with open("Rohan-workout.txt", "a") as Rohan_file:
                Rohan_file.write('['+str(getdate())+']' + " " + input() + "\n")

    elif client_number == 3:
        print("What you wan't to log to Hammad -")
        print("1. Food")
        print("2. Workout")
        print("Which= ", end="")
        log_number = int(input())
        if log_number == 1:
            print("Log food name = ", end="")
            with open("Hammad-food.txt", "a") as Hammad_file:
                Hammad_file.write('['+str(getdate())+']' + " " + input() + "\n")
        elif log_number == 2:
            print("Log workout name = ", end="")
            with open("Hammad-workout.txt", "a") as Hammad_file:
                Hammad_file.write('['+str(getdate())+']' + " " + input() + "\n")
    else:
        print("Invalid client number!")
        print("Please chake your input")

def retrive():
    print("Client list:-")
    print("1. Harry")
    print("2. Rohan")
    print("3. Hammad")
    print("Of which client data do you wan't to see")
    print("Which= ", end="")
    client_number = int(input())
    
    if client_number == 1:
        print("Which data of Harry do you want to see")
        print("1. Food")
        print("2. Workout")
        print("Which= ", end="")
        which = int(input())
        if which == 1:
            with open("Harry-food.txt") as harry_file:
                print(harry_file.read())
        elif which == 2:
            with open("Harry-workout.txt") as harry_file:
                print(harry_file.read())
        else:
            print("Please chake your input!")
            
    elif client_number == 2:
        print("Which data of Rohan do you want to see")
        print("1. Food")
        print("2. Workout")
        print("Which= ", end="")
        which = int(input())
        if which == 1:
            with open("Rohan-food.txt") as rohan_file:
                print(rohan_file.read())
        elif which == 2:
            with open("Rohan-workout.txt") as rohan_file:
                print(rohan_file.read())
        else:
            print("Please chake your input!")
            
    elif client_number == 3:
        print("Which data of Hammad do you want to see")
        print("1. Food")
        print("2. Workout")
        print("Which= ", end="")
        which = int(input())
        if which == 1:
            with open("Hammad-food.txt") as hammad_file:
                print(hammad_file.read())
        elif which == 2:
            with open("Hammad-workout.txt") as hammad_file:
                print(hammad_file.read())
        else:
            print("Please chake your input!")
            
            
print("What you want to do -")
print("1. Log")
print("2. Retrive")
print("What= ", end="")
what = int(input())
if what == 1:
    log()
elif what == 2:
    retrive()
else:
    print("Please chake your input!")
