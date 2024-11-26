#QUESTION TITLE	Sum of Digits
#PROBLEM STATEMENT	Write a program to calculate the sum of the digits of a given positive integer 𝑁.
#CONSTRAINTS	Input:
#An integer 𝑁
#N (1 ≤ 𝑁 ≤ 10^6)

#Output:
#The sum of the digits of 𝑁.
#PUBLIC TESTCASE	Input: 123
 #Output: 6
n=int(input("Enter The Number: "))
sum=0
while n>0:
      digit=n%10
      sum=sum+digit
      n//=10
print(sum)