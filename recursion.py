nterms=int(input())
def fibonacci(n):
    if n<=1:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
if nterms<1:
    print("invalid")
else:
    for i in range(nterms):
        print(fibonacci(i))