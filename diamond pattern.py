class diamond:
    def pattern(self):
        i=1
        n=5
        
        while(i<=n):
            print(" "*(n-i)+"* "*i)
            i=i+1
        n=5
        i=0 
        while(i<=n):
            print(" "*i+"* "*(n-i))
            i=i+1
d=diamond()
d.pattern()