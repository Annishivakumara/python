#"Input format:
#The first line contains a single integer n (1 ≤ n ≤ 100), which represents the number of
#  Fibonacci numbers to printed .

#Sample Input:  3
#Sample Output: 011

number=int(input("enter the Number"))
a=0
b=1
print(a,b , end=',')
for i in range(2,number):
    c=a+b
    print(c,end=',')
    a=b
    b=c