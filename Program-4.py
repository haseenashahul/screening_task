num=[1,2,3,4,5,6,7,8,9]
dict={}
li=[]
n=int(input("Enter the count to input numbers:"))
print(f"Enter {n} numbers:")
for i in range(n):
    ele=int(input())
    li.append(ele)
print(li)


for i in num:
    dict[i] = 0   #initially count is set to 0 for all numbers
for i in num:
    for j in li:
            if j%i == 0:
                dict[i]=dict[i]+1
print(dict)

    
