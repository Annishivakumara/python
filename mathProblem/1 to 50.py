number=int(input("enter the Number: "))
for i in range(1,number+1):
        if  i%5==0:
               continue
        if i==49:
               break
        if i%2==0:
           print(i ,end=',')