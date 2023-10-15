
# c=input("3rd number:")
# #find largest of three
# x=int(a)
# y=int(b)
# z=int(c)
# print("the largest num is :")
# if x>y and x>z:
#     print(x)
# elif   y>x and y>z:
#     print(y)
# else:
#     print(z)    

# #find sum of three
# print(x+y+z)    

x=input("1st number:")
c=input("enter operation:")
y=input("2nd number:")

a=int(x)
b=int(y)

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)  
elif c=="/":
    print(a/b)
else:
    print("error")          
    