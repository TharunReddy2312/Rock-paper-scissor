import random
user_wins=0
computer_wins=0
options=["rock","scissor","paper"]
while(True):
    user_input=input("type rock/paper/scissor or Q to quit: ").lower()
    if user_input=="q":
        print("You lose!")
        break
    
    if user_input not in  options:
        print("You choose invalid options")
    randam_number=random.randint(0,2)    
    computer_pick=options[randam_number]
    print("computer picked=",computer_pick)
    
    if user_input=="rock" and computer_pick=="paper":
        print("You win!")
        user_wins+=1
    
    elif user_input=="scissor" and computer_pick=="paper":
        print("You win!")
        user_wins+=1    
    
    elif user_input=="paper" and computer_pick=="rock":
        print("You win!")
        user_wins+=1
    
    
    else:
        print("You lose!")
        computer_wins+=1
print("user_input wins",user_wins)
print("computer_input",computer_wins)
print("GoodBye")