s=input()
balanced=0
count_l=0
count_r=0
balanced_string=[]
for i in s:
    if i=="L":
        count_l+=1
    elif i=="R":
        count_r+=1
    if count_r==count_l:
        balanced+=1
        balanced_string.append(s[:count_l+count_r])
        s=s[count_l+count_r:]
        count_l=0
        count_r=0



print(balanced)
for char in balanced_string:
    print(char)
    if char=='R':
        print("\n")