#QUESTION TITLE	Check Prime Number
#PROBLEM STATEMENT	Write a program to check if a given integer 𝑁 
# is a prime number. A prime number is a natural number greater than 1 that has 
# no positive divisors other than 1 and itself.
#CONSTRAINTS	Input:
#An integer 𝑁 (2 ≤ 𝑁≤1000).
#Output:
#Yes if  𝑁 is a prime number; otherwise, output No.
#PUBLIC TESTCASE	Input: 7
#Output: Yes
n=int(input("Enter The Number: "))
if n>0:
   for i in range(2,n):
      if n%i==0:
        print("Not A Prime Number: ")
        break
      else:
          print( " Prime Number")
          break
else:
   print("Not A Prime")