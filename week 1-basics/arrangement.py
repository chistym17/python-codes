# k=int(input())
# s=int(input())
# count=0
# for i in range(0,k+1):
#     for j in range(0,k+1):
#         for m in range(0,k+1):
#               if i+j+m==s:
#                      count+=1

# print(count)


k=int(input())
s=int(input())
count=0
for i in range(0,k+1):
    for j in range(0,k+1):
        m=s-(i+j)
        if m<=k:
            count+=1
print(count)