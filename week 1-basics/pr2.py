x=int(input())
y=int(input())
mini=min(x,y)
maxi=max(x,y)
sum=0
for i in range(mini,maxi+1):
    if i%2==1:
        sum+=i
print(sum)