import sys
visited=[0]*50
sequence=[]

n = int(input())
sequence = list(map(int, input().split()))

steps=0
occured=0
if sequence==[]:
    print(steps)
    sys.exit()
    

for i in sequence:
    if visited[i]==1:
        continue
    occured=0
    for j in sequence:
        if i==j:
            occured+=1
    if occured!=i:
        steps+=abs((occured-i))
        
    visited[i]=1


print(steps)
