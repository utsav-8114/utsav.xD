import random
user_choice=input("enter your choice:")
available_choice=["head","tail"]
friend_choice=input("enter your friend's choice:")
coin_toss=random.choice(available_choice)
print("ur choice is:",user_choice)
print("computer choice is:",friend_choice)
if coin_toss==user_choice:
    print("u won!")
else:
    print("u lost!")

    
    
    

