#"Check Which Digits are Divisors of the Number"
number=int (input("Enter the number: "))
count=[]
for i in  str(number):
    num=int(i)
    if num !=0 and number%num==0:
        count.append(num)
print(f"Divisor count and list {count} number is {number}")
