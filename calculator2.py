#calculator with choices
print("press 1. for addition")
print("press 2. for substraction")
print("press 3. for multiplication")
print("press 4. for division")
choice=input("enter your choice: ")
a=float(input("enter a num: "))
b=float(input("enter a num: "))
if choice=="1":
    print("the answer is:",a+b)
elif choice=="2":
    print(a-b)
elif choice=="3":
    print(a*b)
elif choice=="4":
    print(a/b)
else:
    print("invalid choice given")
