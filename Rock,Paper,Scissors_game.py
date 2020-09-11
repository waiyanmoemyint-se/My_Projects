import random
draw = 0
win  = 0
lose = 0
is_end = False
prompt = "Choose Rock(r), Paper(p), Scissors(s), or 'q' to quit:"

while True:
    user_choice = input(prompt)
    while user_choice not in ['r','s','p','q']:
        user_choice = input(prompt)
    if user_choice == 'q':
        break
    else:
        computer_choice = random.choice(['r','p','s'])
        if computer_choice =='r':
            move = 'rock'
        elif computer_choice == 'p':
            move = 'paper'
        else:
            move = 'scissors'
        print("computer give a "+move)

        if computer_choice==user_choice:
            print("Draw")
            draw+=1
        elif(computer_choice=='r' and user_choice == 'p') or \
            (computer_choice == 'p' and user_choice == 's') or \
            (computer_choice == 's' and user_choice == 'r'):
            print("You win")
            win+=1
        else:
            print('Your lose')
            lose+=1
print("Your have"+ str(win)+'win'+str(draw)+"draw and"+str(lose)+'Loses')

