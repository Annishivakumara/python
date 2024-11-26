#QUESTION TITLE	Neon Number
#PROBLEM STATEMENT	Write a program to check if a given number 𝑁 is a Neon Number.
#  A Neon Number is defined as a number where the sum of the digits of its square is equal to 
# the number itself.
#CONSTRAINTS	Input:
#An integer 𝑁
#N (1 ≤ 𝑁 ≤10000)
#Output:
#Yes if 𝑁 is a Neon Number; otherwise, output No.
#PUBLIC TESTCASE
#Input: 9
#Output: Yes
n=int(input("Enter The Input: "))
sum=0
square=n**2 # 81
while square>0: # 9>0
     digits=square%10 # 81=1 and next 8
     sum=sum+digits
     square//=10
if sum==n:
    print("Neon Number: ")
else:
    print("Non Neon Number: ")