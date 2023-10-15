n=int(input())
series=[]
num=0
def fib(n):
    if n<=2:
        return 1
    else:
        sum=fib(n-1)+fib(n-2)
        return sum
s=int(input())
ans=fib(s)
print(ans)