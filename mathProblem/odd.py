name = input()
a,b=map(int, name.split("to"))
sum=0
for i in range(a,b+1):
    if i%2==1:
        sum+=i
print(sum)