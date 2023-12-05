d=dict()
state=input("state: ")
while(state!="end"):
    capital=input("capital: ")
    d[state]=capital
    state = input("state: ")
print(sorted(d.items()))