# #arguments
# def all_sum(*info):
#     for i in info:
#         print(i)

# all_sum("karim","benzema"," messi")

# def print_info(**info):
#     for key,info in info.items():
#         print(key,info)

# print_info(name="messi",age=40,club="psg")


# nums=[2,5,3,5,7,4,2]
# nums.pop()
# print(nums)

# things="pen","pencil","box","table"
# print(things)
# if "box" in things:
#     print(True)

# topule=1,2,3,4,5,6,7,8,0,1,4,6
# for i in enumerate(topule):
#     print(i) 

#error ->error e jate code na atkiye samne continue hois
# try:
#     result=4/2
#     print(result)
# except:
#     print("error")
# finally:
#     print("code done")

#lamda function:->
double=lambda num:num*2
sum=double(7)
print(sum)

arr=[1,2,4,5,6,7]
# double_arr=[map(double,arr)]
# print(arr)
# print(double_arr)
add=lambda x,y:x+y
print(add(3,5))
