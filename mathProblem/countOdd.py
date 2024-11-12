number=int(input("Enter the Number"))
count=0
for i in range(1,number+1,1):
    if i%2==1:
       count+=1
print(count)