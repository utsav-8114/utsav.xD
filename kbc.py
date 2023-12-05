#lets make a mini kbc with  questions!
questions=[
["what is the capital of india?","Delhi","kolkata","hyderabad","mumbai",1],
["what is the capital of westbengal?","Delhi","kolkata","hyderabad","mumbai",2],
["what is the capital of bangladesh?","Dhaka","kolkata","hyderabad","mumbai",1],
["what is the capital of pakistan?","islamabad","kolkata","hyderabad","mumbai",1],
["what is the capital of punjab?","chandigarh","kolkata","hyderabad","mumbai",1],
["what is the capital of punjab?","chandigarh","kolkata","hyderabad","mumbai",1],
["what is the capital of punjab?","chandigarh","kolkata","hyderabad","mumbai",1],
["what is the capital of punjab?","chandigarh","kolkata","hyderabad","mumbai",1],
["what is the capital of punjab?","chandigarh","kolkata","hyderabad","mumbai",1],
["what is the capital of punjab?","chandigarh","kolkata","hyderabad","mumbai",1],
]
levels=["1000","2000","3000","4000","5000","10000","20000","30000","80000","160000"]
for i in range(0,len(questions)):
    n=questions[i]
    print("question for rs",levels[i],"is:")
    print(n[i])
    print(f"a.{n[1]}       b.{n[2]}")
    print(f"c.{n[3]}       d.{n[4]}")

    ans=int(input("enter your answer:"))
    if ans==n[5]:
        print("congratulations you have won",levels[i])
    else:
        print("wrong answer!")
        break
    
    
    
    
    