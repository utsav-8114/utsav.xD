#following is a game of odd even
comp1=input("player1 choose among odd or even:")
comp2=input("player2 choose among odd or even:")
computer_player1=int(input("player1 choose the number you want to throw:"))
computer_player2=int(input("player2 choose the number you want to throw:"))
if (computer_player1 or computer_player2)>6:
    print("invalid number thrown please repeat!!")
else:
    print("u may continue!")
if (computer_player1+computer_player2)%2==0:
    print("the result is even!!")
else:
    print("the result is odd!!")
