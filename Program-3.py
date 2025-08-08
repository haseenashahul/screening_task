a=int(input("Enter a number :"))
if a%2 !=0:
    for i in range(a):
        res = (2*i)+1
        print(res,end=' ')
else:
    for i in range(a-1):
        res = (2*i)+1
        print(res,end=' ' )
   