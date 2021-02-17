print("welcome to treasure island to find treasure.")
move = input("move right or left? ")
if move == 'left':
    action = input("swim or wait? ")
    if action == 'wait':
        which_door = input("choice which door do you prefar? ")
        if which_door == 'yellow':
            print("you win")
        elif which_door == 'blue':
            print("game over")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")