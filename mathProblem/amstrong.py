number = int(input("Enter the Number: "))
original_number=number
length=len(str(number))
result=0
while number>0:  # 153
    digit=number%10 # 3
    pow_num=digit**length #3 = 27
    result+=pow_num #0+27
    number=number//10 # 
if result==original_number:
        print("Armstrong Number ")
else:
        print("Not Amstrong ")