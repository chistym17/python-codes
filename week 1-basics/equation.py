x=int(input())
n=int(input())
sum=0
if n%2==0:
    for i in range(0,n+2,2):
        sum+=x**i
elif n%2!=0:
    for i in range(0,n+1,2):
        sum+=x**i
print(sum-1)
