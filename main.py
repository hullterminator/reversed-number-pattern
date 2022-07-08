#code to print reversed numbers pattern
#code goes here
n=int(input())
i=1
while i<=n:
    p=i
    j=1
    while j<=i:
        print(p,end='')
        p-=1
        j+=1
    print()
    i+=1
