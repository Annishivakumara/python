#count the Digit in a number
number=int(input("Enter the Number: "))
count=0
while number > 0:
    number=number//10
    count+=1

print(f"counted digits {count}: ")